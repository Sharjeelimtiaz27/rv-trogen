#!/usr/bin/env python3
"""
RV-TroGen VCD Analyzer  —  v3  (smart zoom + skip flat signals)
================================================================
Usage modes
-----------
1. SINGLE FILE (auto-finds original):
       python analyze_vcd.py --trojan path/to/ibex_cs_registers_trojan_DoS.vcd

2. DIRECTORY (processes all trojans vs original):
       python analyze_vcd.py --vcd-dir simulation_results/vcd/ibex/ibex_cs_registers

3. EXPLICIT PAIR:
       python analyze_vcd.py --original orig.vcd --trojan trojan.vcd

New features vs v2
------------------
  • Auto-detects trojan_active HIGH edge → zooms plot to ±ZOOM_MARGIN around it
  • Skips signals with ZERO differences in the plot (no more flat empty rows)
  • Last-value semantics for time-aligned comparison (handles timing skew)
  • Binary search time lookup (fast even on large VCDs)
  • Single-file mode: pass only --trojan, original is found automatically
"""

import sys
import re
import bisect
import argparse
from pathlib import Path
from collections import defaultdict

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ── Constants ────────────────────────────────────────────────────────────────
ZOOM_MARGIN_NS  = 50          # ns to show before/after trojan_active edge
MIN_DIFF_POINTS = 1           # minimum differences to include signal in plot
MAX_PLOT_SIGNALS = 8          # cap on number of subplot rows
PRIORITY_SIGNALS = [          # these appear first in plots if they differ
    'csr_we_int', 'csr_rdata_o', 'csr_rdata_int',
    'priv_mode_id_o', 'priv_lvl_q',
    'csr_mepc_o', 'mepc_q',
    'trojan_active', 'stall_active', 'trojan_counter',
]


# ══════════════════════════════════════════════════════════════════════════════
# VCD PARSER
# ══════════════════════════════════════════════════════════════════════════════
class VCDParser:
    def __init__(self, vcd_file):
        self.vcd_file = Path(vcd_file)
        self.signal_map   = {}          # symbol → {name, width}
        self.signal_values= defaultdict(list)   # name → [(time_ps, value)]
        self.timescale_ps = 1000        # default 1ns = 1000ps
        self.times        = []

    # ── timescale conversion ──────────────────────────────────────────────
    @staticmethod
    def _parse_timescale(ts_str):
        """Return timescale in picoseconds."""
        ts_str = ts_str.strip().lower().replace(' ', '')
        m = re.match(r'^(\d+)(ps|ns|us|ms|s)$', ts_str)
        if not m:
            return 1000  # default 1ns
        val  = int(m.group(1))
        unit = m.group(2)
        mult = {'ps': 1, 'ns': 1_000, 'us': 1_000_000, 'ms': 1_000_000_000, 's': 1_000_000_000_000}
        return val * mult[unit]

    def parse(self):
        print(f"  Parsing {self.vcd_file.name} …", end=' ', flush=True)
        content = self.vcd_file.read_text(encoding='utf-8', errors='ignore')
        lines   = content.splitlines()

        in_def      = True
        current_t   = 0
        ts_buf      = []
        reading_ts  = False

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # ── timescale (may span multiple lines) ──────────────────────
            if '$timescale' in line:
                reading_ts = True
                ts_buf = []
            if reading_ts:
                ts_buf.append(line)
                if '$end' in line:
                    reading_ts = False
                    ts_raw = ' '.join(ts_buf)
                    ts_raw = re.sub(r'\$timescale|\$end', '', ts_raw).strip()
                    self.timescale_ps = self._parse_timescale(ts_raw)
                continue

            if line.startswith('$var'):
                parts = line.split()
                if len(parts) >= 5:
                    self.signal_map[parts[3]] = {'name': parts[4], 'width': int(parts[2])}

            elif '$enddefinitions' in line:
                in_def = False

            elif not in_def:
                if line.startswith('#'):
                    try:
                        current_t = int(line[1:]) * self.timescale_ps
                    except ValueError:
                        pass

                elif line.startswith('b'):
                    parts = line.split()
                    if len(parts) >= 2:
                        val_str = parts[0][1:].replace('x','0').replace('z','0') \
                                              .replace('X','0').replace('Z','0')
                        sym = parts[1]
                        try:
                            v = int(val_str, 2)
                        except ValueError:
                            v = 0
                        if sym in self.signal_map:
                            self.signal_values[self.signal_map[sym]['name']].append((current_t, v))

                elif line and line[0] in '01xzXZ':
                    v   = 1 if line[0] == '1' else 0
                    sym = line[1:].strip()
                    if sym in self.signal_map:
                        self.signal_values[self.signal_map[sym]['name']].append((current_t, v))

        # Build sorted times list
        all_t = set()
        for vals in self.signal_values.values():
            for t, _ in vals:
                all_t.add(t)
        self.times = sorted(all_t)

        print(f"  {len(self.signal_map)} signals, "
              f"t=[{min(self.times) if self.times else 0}…"
              f"{max(self.times) if self.times else 0}] ps")
        return self

    # ── last-value lookup (binary search) ────────────────────────────────
    def value_at(self, sig_name, time_ps):
        """Return the signal value at or before time_ps using last-value semantics."""
        vals = self.signal_values.get(sig_name, [])
        if not vals:
            return None
        times = [t for t, _ in vals]
        idx   = bisect.bisect_right(times, time_ps) - 1
        return vals[idx][1] if idx >= 0 else None

    # ── step-plot arrays ─────────────────────────────────────────────────
    def step_arrays(self, sig_name, t_start=None, t_end=None):
        """Return (times, values) arrays clipped to [t_start, t_end]."""
        vals = self.signal_values.get(sig_name, [])
        if not vals:
            return [], []

        # Prepend initial value if t_start cuts off the beginning
        result = []
        if t_start is not None:
            iv = self.value_at(sig_name, t_start)
            if iv is not None:
                result.append((t_start, iv))

        for t, v in vals:
            if t_start is not None and t < t_start:
                continue
            if t_end is not None and t > t_end:
                break
            result.append((t, v))

        if not result:
            return [], []
        return [t for t, _ in result], [v for _, v in result]


# ══════════════════════════════════════════════════════════════════════════════
# COMPARISON ENGINE
# ══════════════════════════════════════════════════════════════════════════════
def find_differences(orig: VCDParser, troj: VCDParser,
                     max_signals: int = 60,
                     max_timepoints: int = 20_000):
    """
    Time-aligned comparison using last-value semantics.
    Returns dict: sig_name → list of (time_ps, orig_val, troj_val)

    Optimisations for large VCDs (1000+ signals):
    - Only compares a focused signal set (priority list + signals that
      changed MORE in trojaned VCD than original — likely payload targets)
    - Samples up to max_timepoints per signal to avoid multi-million loops
    """
    common = set(orig.signal_values.keys()) & set(troj.signal_values.keys())

    # ── Step 1: build candidate signal list ──────────────────────────────
    # Always include priority signals if present
    prio = [s for s in PRIORITY_SIGNALS if s in common]

    # Find signals with more change-events in trojan than original
    # (trojan payload additions show up here)
    extra = []
    for sig in common:
        if sig in prio:
            continue
        n_orig = len(orig.signal_values[sig])
        n_troj = len(troj.signal_values[sig])
        if n_troj > n_orig:
            extra.append((n_troj - n_orig, sig))
    extra.sort(reverse=True)
    extra_sigs = [s for _, s in extra[: max_signals - len(prio)]]

    candidates = prio + extra_sigs
    # Fallback: if nothing interesting found, just take all common signals up to cap
    if not candidates:
        candidates = sorted(common)[:max_signals]

    print(f"    Comparing {len(candidates)} candidate signals "
          f"(out of {len(common)} common) …", flush=True)

    # ── Step 2: compare each candidate ───────────────────────────────────
    diffs = {}
    for i, sig in enumerate(candidates):
        if i % 10 == 0:
            print(f"    [{i+1}/{len(candidates)}] comparing signals...", end=chr(13), flush=True)
        o_times = [t for t, _ in orig.signal_values[sig]]
        t_times = [t for t, _ in troj.signal_values[sig]]
        all_t   = sorted(set(o_times) | set(t_times))

        # Sample if too many time points
        if len(all_t) > max_timepoints:
            step  = len(all_t) // max_timepoints
            all_t = all_t[::step]

        sig_diffs = []
        for tp in all_t:
            ov = orig.value_at(sig, tp)
            tv = troj.value_at(sig, tp)
            if ov is not None and tv is not None and ov != tv:
                sig_diffs.append((tp, ov, tv))

        if sig_diffs:
            diffs[sig] = sig_diffs

    return diffs


def find_trojan_activation(troj: VCDParser):
    """
    Find the time when trojan_active goes HIGH (0→1 transition).
    Returns time_ps or None.
    """
    vals = troj.signal_values.get('trojan_active', [])
    prev = 0
    for t, v in vals:
        if prev == 0 and v == 1:
            return t
        prev = v
    return None


# ══════════════════════════════════════════════════════════════════════════════
# PLOTTING
# ══════════════════════════════════════════════════════════════════════════════

# 1-bit signals — clamp y-axis and draw as clean digital waveform
_ONE_BIT = {'trojan_active', 'stall_active', 'csr_we_int', 'csr_op_en_i',
            'priv_mode_id_o', 'illegal_csr_insn_o'}


def _is_wide_bus(sig_name: str, parser: VCDParser) -> bool:
    """Return True if signal looks like a wide bus (many unique values)."""
    vals = {v for _, v in parser.signal_values.get(sig_name, [])}
    return len(vals) > 8


def _to_us(ps_val):
    """Convert picoseconds to microseconds for readable axis labels."""
    return ps_val / 1_000_000


def make_plot(orig: VCDParser, troj: VCDParser, diffs: dict,
              trojan_name: str, output_path: Path,
              t_start=None, t_end=None, activation_t=None):
    """
    Generate a clean, publication-ready comparison plot.

    Layout
    ------
    INFO ROWS  (grey header band) — trojan-only control signals:
               trojan_active, stall_active, trojan_counter
               Drawn from trojan VCD only. No original overlay.
    DIFF ROWS  (white/blue) — signals that actually differ between
               original and trojaned simulation.
               1-bit signals get a tight [0,1] y-axis.
               Wide buses are skipped (too noisy to read).

    X-axis is always in microseconds (µs) for readability.
    Activation marker is one clean vertical orange line.
    No per-point axvspan shading (it blots everything out).
    """

    # ── decide time window (ps internally) ───────────────────────────────
    margin_ps = ZOOM_MARGIN_NS * 1000

    if activation_t is not None and t_start is None and t_end is None:
        all_diff_times = [t for sd in diffs.values() for t, _, _ in sd]
        if all_diff_times:
            t_start = max(0, min(all_diff_times) - margin_ps)
            t_end   = max(all_diff_times) + margin_ps
        else:
            t_start = max(0, activation_t - margin_ps)
            t_end   = activation_t + margin_ps * 5
        print(f"  Auto-zoom window: {t_start/1000:.0f} – {t_end/1000:.0f} ns")
    elif t_start is not None:
        t_start *= 1000
        t_end    = t_end * 1000 if t_end else None

    # ── build row list ────────────────────────────────────────────────────
    # INFO rows: trojan-only signals present in trojan VCD
    info_rows = [s for s in ('trojan_active', 'stall_active', 'trojan_counter')
                 if s in troj.signal_values]

    # DIFF rows: priority signals with differences, skip wide buses
    diff_rows = []
    for s in PRIORITY_SIGNALS:
        if s in diffs and s not in diff_rows:
            if not _is_wide_bus(s, troj):
                diff_rows.append(s)
    for s in sorted(diffs.keys()):
        if s not in diff_rows and s not in info_rows:
            if not _is_wide_bus(s, troj):
                diff_rows.append(s)
    diff_rows = diff_rows[:MAX_PLOT_SIGNALS - len(info_rows)]

    all_rows = info_rows + diff_rows
    if not all_rows:
        print("  No plottable signals (all are wide buses or no differences).")
        return None

    # ── figure setup ──────────────────────────────────────────────────────
    # Give 1-bit rows half the height of bus rows
    heights = []
    for s in all_rows:
        is_1bit = (s in _ONE_BIT or
                   (s in troj.signal_values and
                    max((v for _, v in troj.signal_values[s]), default=0) <= 1))
        heights.append(1.2 if is_1bit else 2.2)

    fig, axes = plt.subplots(len(all_rows), 1,
                             figsize=(16, sum(heights) + 1.2),
                             sharex=True,
                             gridspec_kw={'height_ratios': heights})
    if len(all_rows) == 1:
        axes = [axes]

    BG_DARK   = '#0D1117'
    BG_ROW    = '#161B22'
    BG_INFO   = '#1C2128'   # slightly lighter for info rows
    COL_ORIG  = '#58A6FF'   # blue  — original
    COL_TROJ  = '#FF7B72'   # red   — trojaned
    COL_ACT   = '#FFA500'   # orange — activation line
    COL_TEXT  = '#E6EDF3'
    COL_GRID  = '#30363D'

    fig.patch.set_facecolor(BG_DARK)

    t_start_us = _to_us(t_start) if t_start is not None else None
    t_end_us   = _to_us(t_end)   if t_end   is not None else None
    act_us     = _to_us(activation_t) if activation_t is not None else None

    title = f"Original  vs  {trojan_name} Trojan"
    if t_start_us is not None and t_end_us is not None:
        title += f"   |   {t_start_us:.1f} – {t_end_us:.1f} µs"
    fig.suptitle(title, fontsize=12, fontweight='bold',
                 color=COL_TEXT, y=1.005)

    legend_done = False

    for ax, sig in zip(axes, all_rows):
        is_info = sig in info_rows
        ax.set_facecolor(BG_INFO if is_info else BG_ROW)
        for spine in ax.spines.values():
            spine.set_edgecolor(COL_GRID)
        ax.tick_params(colors='#8B949E', labelsize=7)
        ax.grid(True, alpha=0.12, color=COL_GRID)

        def _get_us(parser, name):
            t_arr, v_arr = parser.step_arrays(name, t_start, t_end)
            return [_to_us(t) for t in t_arr], v_arr

        if is_info:
            # Info row: only trojan VCD, no original, grey label tag
            tt, tv = _get_us(troj, sig)
            if tt:
                color = '#A8B5C8' if sig == 'trojan_counter' else COL_TROJ
                lw    = 1.2 if sig == 'trojan_counter' else 1.5
                ax.step(tt, tv, color=color, linewidth=lw, where='post')
            # Label badge
            ax.set_ylabel(sig, color='#8B949E', fontsize=8,
                          rotation=0, labelpad=115, va='center',
                          fontstyle='italic')
        else:
            # Diff row: original (blue) + trojan (red dashed)
            ot, ov = _get_us(orig, sig)
            tt, tv = _get_us(troj, sig)

            if ot:
                ax.step(ot, ov, color=COL_ORIG, linewidth=1.6,
                        label='Original', where='post', zorder=3)
            if tt:
                ax.step(tt, tv, color=COL_TROJ, linewidth=1.6,
                        linestyle='--', label='Trojaned',
                        where='post', alpha=0.85, zorder=4)

            # Thin vertical tick marks at first few difference points only
            # (no axvspan — it blots out the waveform)
            if sig in diffs:
                shown = 0
                for tp, _, _ in diffs[sig]:
                    if t_start is not None and tp < t_start:
                        continue
                    if t_end is not None and tp > t_end:
                        break
                    ax.axvline(_to_us(tp), color='#FFD700',
                               alpha=0.35, linewidth=0.6, zorder=2)
                    shown += 1
                    if shown >= 200:   # draw at most 200 markers
                        break

            ax.set_ylabel(sig, color=COL_TEXT, fontsize=8.5, fontweight='bold',
                          rotation=0, labelpad=115, va='center')

            # Legend once, on first diff row
            if not legend_done:
                ax.legend(loc='upper right', fontsize=8,
                          facecolor=BG_ROW, edgecolor=COL_GRID,
                          labelcolor=COL_TEXT, framealpha=0.9)
                legend_done = True

        # 1-bit y-axis
        all_vals = ([v for _, v in troj.signal_values.get(sig, [])] +
                    [v for _, v in orig.signal_values.get(sig, [])])
        if all_vals and max(all_vals) <= 1:
            ax.set_ylim(-0.15, 1.35)
            ax.set_yticks([0, 1])
            ax.set_yticklabels(['0', '1'], color='#8B949E', fontsize=7)

        # Activation line on every row
        if act_us is not None:
            if (t_start_us is None or act_us >= t_start_us) and                (t_end_us   is None or act_us <= t_end_us):
                ax.axvline(act_us, color=COL_ACT, linewidth=1.5,
                           linestyle=':', zorder=5,
                           label='activation' if not legend_done else None)

    # x-axis
    axes[-1].set_xlabel('Time (µs)', color=COL_TEXT, fontsize=10)
    axes[-1].tick_params(axis='x', colors='#8B949E', labelsize=8)
    if t_start_us is not None and t_end_us is not None:
        axes[-1].set_xlim(t_start_us, t_end_us)

    plt.tight_layout(rect=[0.12, 0, 1, 1])

    range_tag = ''
    if t_start is not None and t_end is not None:
        range_tag = f"_{int(t_start/1000)}ns_{int(t_end/1000)}ns"
    out_file = output_path / f"waveform_{trojan_name}{range_tag}.png"
    plt.savefig(out_file, dpi=180, bbox_inches='tight',
                facecolor=BG_DARK, edgecolor='none')
    plt.close()
    print(f"  Plot saved: {out_file.name}")
    return out_file


# ══════════════════════════════════════════════════════════════════════════════
# TEXT REPORT
# ══════════════════════════════════════════════════════════════════════════════
def write_report(orig_path, troj_path, diffs, activation_t, output_path, trojan_name):
    lines = []
    lines += ["=" * 70,
              f"RV-TroGen VCD Comparison Report — {trojan_name}",
              "=" * 70, ""]
    lines += [f"Original : {orig_path}",
              f"Trojaned : {troj_path}", ""]

    if activation_t is not None:
        lines.append(f"Trojan activation time : {activation_t} ps  ({activation_t/1000:.1f} ns)")
    else:
        lines.append("Trojan activation time : NOT DETECTED (trojan_active never went HIGH)")
    lines.append("")

    if not diffs:
        lines += ["✅ No signal differences detected.",
                  "   Possible causes:",
                  "   1. Trigger threshold not reached in simulation time",
                  "   2. Trojan payload targets a signal not in VCD",
                  "   3. Incorrect VCD pair"]
    else:
        lines.append(f"Signals with differences: {len(diffs)}")
        lines.append("")
        for sig in sorted(diffs.keys()):
            sd = diffs[sig]
            lines.append(f"  Signal: {sig}   ({len(sd)} diff points)")
            for tp, ov, tv in sd[:8]:
                xor = (ov ^ tv) if isinstance(ov, int) and isinstance(tv, int) else '?'
                lines.append(f"    {tp:12d} ps  orig=0x{ov:08X}  troj=0x{tv:08X}  XOR=0x{xor:08X}"
                             if isinstance(ov, int) else
                             f"    {tp:12d} ps  orig={ov}  troj={tv}")
            if len(sd) > 8:
                lines.append(f"    … and {len(sd)-8} more")
            lines.append("")

    out = output_path / f"report_{trojan_name}.txt"
    out.write_text('\n'.join(lines))
    print(f"  📄 Report: {out.name}")


# ══════════════════════════════════════════════════════════════════════════════
# AUTO-FIND ORIGINAL VCD
# ══════════════════════════════════════════════════════════════════════════════
def find_original(trojan_vcd: Path) -> Path | None:
    """
    Given a trojaned VCD, find the original VCD.
    Heuristic: look in same directory for a VCD that does NOT contain 'trojan'
    in its name but shares a common prefix.
    """
    d = trojan_vcd.parent
    candidates = [f for f in d.glob('*.vcd')
                  if 'trojan' not in f.name.lower() and f != trojan_vcd]
    if not candidates:
        # broader: any non-trojan VCD in same dir
        candidates = [f for f in d.glob('*.vcd') if f != trojan_vcd]
    if len(candidates) == 1:
        return candidates[0]
    if len(candidates) > 1:
        # prefer the one whose stem is a prefix of the trojan file stem
        stem = trojan_vcd.stem.lower().split('_trojan')[0]
        for c in candidates:
            if c.stem.lower() == stem or c.stem.lower().startswith(stem):
                return c
        return candidates[0]
    return None


# ══════════════════════════════════════════════════════════════════════════════
# MAIN ENTRY POINTS
# ══════════════════════════════════════════════════════════════════════════════
def process_pair(orig_path: Path, troj_path: Path, output_path: Path,
                 t_start_ns=None, t_end_ns=None, auto_zoom=True):
    """Compare one original/trojan pair and produce plot + report."""
    trojan_name = re.sub(r'.*_trojan_?', '', troj_path.stem, flags=re.IGNORECASE) or troj_path.stem

    print(f"\n{'─'*60}")
    print(f"  Trojan : {trojan_name}")
    print(f"  Orig   : {orig_path.name}")

    orig = VCDParser(orig_path).parse()
    troj = VCDParser(troj_path).parse()

    activation_t = find_trojan_activation(troj)
    if activation_t is not None:
        print(f"  ⚡ trojan_active ↑ at {activation_t} ps  ({activation_t/1000:.1f} ns)")
    else:
        print("  ⚠️  trojan_active not found / never fired")

    diffs = find_differences(orig, troj)
    print(f"  Signals with differences: {len(diffs)}"
          + (f"  ({', '.join(sorted(diffs.keys()))})" if diffs else ""))

    output_path.mkdir(parents=True, exist_ok=True)

    # Determine time window
    if t_start_ns is not None or t_end_ns is not None:
        # User-specified range (convert ns→ps inside make_plot)
        ts, te = t_start_ns, t_end_ns
        zoom = False
    elif auto_zoom and (activation_t is not None or diffs):
        ts, te = None, None
        zoom = True
    else:
        ts, te = None, None
        zoom = False

    make_plot(orig, troj, diffs, trojan_name, output_path,
              t_start=ts, t_end=te,
              activation_t=activation_t if zoom else None)

    write_report(orig_path, troj_path, diffs, activation_t, output_path, trojan_name)

    return len(diffs) > 0


def run_batch(vcd_dir: Path, output_path: Path, t_start_ns=None, t_end_ns=None):
    """Process all trojaned VCDs in a directory."""
    vcd_files = sorted(vcd_dir.glob('*.vcd'))
    originals  = [f for f in vcd_files if 'trojan' not in f.name.lower()]
    trojaned   = [f for f in vcd_files if 'trojan' in f.name.lower()]

    if not originals:
        print("❌ No original VCD found (no file without 'trojan' in name)")
        return
    original = originals[0]
    print(f"  Original VCD: {original.name}")
    print(f"  Trojaned VCDs found: {len(trojaned)}")

    results = {}
    for troj in trojaned:
        ok = process_pair(original, troj, output_path, t_start_ns, t_end_ns)
        name = re.sub(r'.*_trojan_?', '', troj.stem, flags=re.IGNORECASE) or troj.stem
        results[name] = ok

    print(f"\n{'='*60}")
    print("BATCH SUMMARY")
    print(f"{'='*60}")
    for name, has_diffs in results.items():
        status = "✅ differences detected" if has_diffs else "⚠️  no differences"
        print(f"  {name:<20} {status}")


# ══════════════════════════════════════════════════════════════════════════════
# CLI
# ══════════════════════════════════════════════════════════════════════════════
def main():
    ap = argparse.ArgumentParser(
        description='RV-TroGen VCD Analyzer v3 — smart zoom, no flat signals',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Single trojaned file — auto-finds original in same directory
  python analyze_vcd.py --trojan results/ibex_cs_registers_trojan_DoS.vcd

  # Directory — compares all trojaned VCDs against the original in that dir
  python analyze_vcd.py --vcd-dir simulation_results/vcd/ibex/ibex_cs_registers

  # Explicit pair with manual time window
  python analyze_vcd.py --original orig.vcd --trojan troj.vcd --start 150 --end 600

  # Directory, disable auto-zoom (show full time range)
  python analyze_vcd.py --vcd-dir results/ --no-zoom
"""
    )
    ap.add_argument('--trojan',   help='Path to a single trojaned VCD file')
    ap.add_argument('--original', help='Path to original VCD (optional if --trojan given)')
    ap.add_argument('--vcd-dir',  help='Directory containing VCD files (batch mode)')
    ap.add_argument('--output',   default='simulation_results/analysis',
                                  help='Output directory for plots/reports')
    ap.add_argument('--start',    type=float, help='Manual start time in ns')
    ap.add_argument('--end',      type=float, help='Manual end time in ns')
    ap.add_argument('--no-zoom',  action='store_true',
                                  help='Disable auto-zoom (show full waveform)')
    args = ap.parse_args()

    print()
    print("=" * 60)
    print("  RV-TroGen VCD Analyzer  v3")
    print("=" * 60)

    auto_zoom = not args.no_zoom

    def derive_output(vcd_path: Path) -> Path:
        """
        Mirror the VCD directory into analysis/.
        e.g. simulation_results/vcd/ibex/ibex_cs_registers/
          →  simulation_results/analysis/ibex/ibex_cs_registers/
        """
        if args.output != 'simulation_results/analysis':
            return Path(args.output)          # user gave explicit --output
        parts = vcd_path.parts
        if 'vcd' in parts:
            idx  = list(parts).index('vcd')
            tail = parts[idx + 1:]            # e.g. ('ibex', 'ibex_cs_registers')
            base = Path(*parts[:idx])         # e.g. simulation_results
            return base / 'analysis' / Path(*tail) if tail else Path(args.output)
        return Path(args.output)

    # ── mode 1: single trojan file ────────────────────────────────────────
    if args.trojan and not args.vcd_dir:
        troj_path = Path(args.trojan)
        if not troj_path.exists():
            print(f"❌ File not found: {troj_path}")
            sys.exit(1)

        if args.original:
            orig_path = Path(args.original)
        else:
            orig_path = find_original(troj_path)
            if orig_path is None:
                print(f"❌ Could not auto-find original VCD in {troj_path.parent}")
                print("   Use --original <path> to specify it manually.")
                sys.exit(1)
            print(f"  Auto-found original: {orig_path.name}")

        out = derive_output(troj_path.parent)
        process_pair(orig_path, troj_path, out,
                     args.start, args.end, auto_zoom)

    # ── mode 2: directory batch ───────────────────────────────────────────
    elif args.vcd_dir:
        vcd_dir = Path(args.vcd_dir)
        if not vcd_dir.exists():
            print(f"❌ Directory not found: {vcd_dir}")
            sys.exit(1)
        out = derive_output(vcd_dir)
        run_batch(vcd_dir, out, args.start, args.end)

    # ── mode 3: explicit pair ─────────────────────────────────────────────
    elif args.original and args.trojan:
        out = derive_output(Path(args.trojan).parent)
        process_pair(Path(args.original), Path(args.trojan), out,
                     args.start, args.end, auto_zoom)

    else:
        ap.print_help()
        print("\n❌ Provide --trojan FILE, --vcd-dir DIR, or --original + --trojan")
        sys.exit(1)

    print(f"\n✅ Done — outputs in: {out}")


if __name__ == '__main__':
    main()