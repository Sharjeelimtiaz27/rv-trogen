#!/usr/bin/env python3
"""
RV-TroGen Full Pipeline Batch Script
=====================================
Runs the COMPLETE trojan generation pipeline for all processors:

  STAGE 1: Generate trojan snippets  (batch_generate.py logic)
           examples/{proc}/original/*.sv  →  examples/{proc}/generated_trojans/

  STAGE 2: Integrate snippets into RTL  (prepare_multi_trojan_simulation.py)
           generated_trojans/ + original RTL  →  trojaned_rtl/  +  testbenches/

Usage:
    # Full pipeline - all processors
    python scripts/batch_full_pipeline.py

    # Single processor only
    python scripts/batch_full_pipeline.py --processor ibex

    # Stage 1 only (generate snippets, skip integration)
    python scripts/batch_full_pipeline.py --stage1-only

    # Stage 2 only (integrate, skip snippet generation)
    python scripts/batch_full_pipeline.py --stage2-only

    # Dry run (no files written, just report what would be done)
    python scripts/batch_full_pipeline.py --dry-run

    # Verbose per-module output
    python scripts/batch_full_pipeline.py --verbose

Author: Sharjeel Imtiaz (TalTech)
Date: 2026
"""

import sys
import argparse
import time
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# ── path setup ────────────────────────────────────────────────────────────────
ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

from src.generator.trojan_generator import TrojanGenerator
from src.parser import RTLParser


# ─────────────────────────────────────────────────────────────────────────────
# Configuration
# ─────────────────────────────────────────────────────────────────────────────
PROCESSORS = ['ibex', 'cva6', 'rsd']

PATTERN_DISPLAY = {
    'DoS':          'Denial of Service',
    'Integrity':    'Data Integrity',
    'Covert':       'Covert Channel',
    'Leak':         'Information Leak',
    'Privilege':    'Privilege Escalation',
    'Availability': 'Performance Degradation',
}


# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────
def bar(n, total, width=30):
    filled = int(width * n / total) if total else 0
    return '█' * filled + '░' * (width - filled)


def find_valid_modules(proc_dir: Path, verbose: bool = False):
    """Return list of .sv files that parse successfully."""
    original_dir = proc_dir / 'original'
    if not original_dir.exists():
        print(f"  ⚠️  {original_dir} not found - skipping")
        return []

    all_sv = sorted(original_dir.glob('*.sv'))
    valid, skipped = [], []

    for sv in all_sv:
        try:
            p = RTLParser(str(sv))
            p.parse()
            valid.append(sv)
        except Exception as e:
            skipped.append((sv.name, str(e)[:60]))

    if skipped and verbose:
        print(f"  ⚠️  Skipped {len(skipped)} non-module files (packages/interfaces):")
        for name, err in skipped:
            print(f"     - {name}: {err}")

    return valid


# ─────────────────────────────────────────────────────────────────────────────
# Stage 1: Generate Snippets
# ─────────────────────────────────────────────────────────────────────────────
def stage1_generate_snippets(processors: list, base_dir: Path,
                              dry_run: bool, verbose: bool) -> dict:
    """
    Run TrojanGenerator on every module for every processor.
    Outputs go to  examples/{proc}/generated_trojans/{module}/
    Returns stats dict.
    """
    print("\n" + "═" * 70)
    print("  STAGE 1 — Generate Trojan Snippets")
    print("═" * 70)

    stats = {}

    for proc in processors:
        proc_dir = base_dir / proc
        output_dir = proc_dir / 'generated_trojans'

        print(f"\n  Processor: {proc.upper()}")
        modules = find_valid_modules(proc_dir, verbose)

        if not modules:
            print(f"  ❌ No valid modules found")
            stats[proc] = {'modules': 0, 'snippets': 0, 'failed': 0}
            continue

        print(f"  Found {len(modules)} valid modules")

        if not dry_run:
            output_dir.mkdir(exist_ok=True)

        proc_snippets = 0
        proc_failed   = 0

        for i, sv in enumerate(modules, 1):
            module_name = sv.stem
            prefix = f"  [{i:3}/{len(modules)}]"

            try:
                gen = TrojanGenerator(str(sv), processor=proc)
                gen.parse_module()
                gen.find_candidates()

                if gen.candidates:
                    if not dry_run:
                        module_out = output_dir / module_name
                        files = gen.generate_trojans(str(module_out))
                        gen.generate_summary_report(str(module_out))
                        n = len(files)
                    else:
                        n = len(gen.candidates)

                    proc_snippets += n
                    if verbose:
                        print(f"{prefix} ✅ {module_name:<38} {n:2} snippets")
                    else:
                        print(f"{prefix} ✅ {module_name:<38} {n:2} snippets", end='\r')
                else:
                    if verbose:
                        print(f"{prefix} ⚪ {module_name:<38} no candidates")

            except Exception as e:
                proc_failed += 1
                print(f"{prefix} ❌ {module_name:<38} ERROR: {str(e)[:50]}")

        print(f"\n  ✔  {proc.upper()}: {proc_snippets} snippets generated "
              f"({proc_failed} failed)")
        stats[proc] = {
            'modules':  len(modules),
            'snippets': proc_snippets,
            'failed':   proc_failed,
        }

    return stats


# ─────────────────────────────────────────────────────────────────────────────
# Stage 2: Integrate Snippets into RTL
# ─────────────────────────────────────────────────────────────────────────────
def stage2_integrate_trojans(processors: list, base_dir: Path,
                              dry_run: bool, verbose: bool) -> dict:
    """
    Run prepare_multi_trojan_simulation logic for every module of every processor.
    Reads from  generated_trojans/{module}/
    Writes to   trojaned_rtl/{module}/   +   testbenches/{proc}/{module}/
    Returns stats dict.
    """
    print("\n" + "═" * 70)
    print("  STAGE 2 — Integrate Trojans into RTL")
    print("═" * 70)

    # Import here - this script may be fixed/replaced by user
    try:
        # Try importing from scripts/ first (user's local copy)
        scripts_dir = ROOT / 'scripts'
        sys.path.insert(0, str(scripts_dir))
        from prepare_multi_trojan_simulation import MultiTrojanIntegrator
        print("  ℹ️  Using prepare_multi_trojan_simulation from scripts/")
    except ImportError:
        print("  ❌ Cannot import MultiTrojanIntegrator from scripts/")
        print("     Make sure prepare_multi_trojan_simulation.py is in scripts/")
        return {}

    stats = {}

    for proc in processors:
        proc_dir   = base_dir / proc
        trojans_base = proc_dir / 'generated_trojans'

        print(f"\n  Processor: {proc.upper()}")

        if not trojans_base.exists():
            print(f"  ⚠️  {trojans_base} not found — run Stage 1 first")
            stats[proc] = {'integrated': 0, 'failed': 0}
            continue

        modules = find_valid_modules(proc_dir, verbose)
        if not modules:
            stats[proc] = {'integrated': 0, 'failed': 0}
            continue

        integrated = 0
        failed     = 0

        for i, sv in enumerate(modules, 1):
            module_name  = sv.stem
            snippets_dir = trojans_base / module_name
            prefix       = f"  [{i:3}/{len(modules)}]"

            if not snippets_dir.exists():
                if verbose:
                    print(f"{prefix} ⚪ {module_name:<38} no snippets dir")
                continue

            snippet_files = list(snippets_dir.glob('*.sv'))
            if not snippet_files:
                if verbose:
                    print(f"{prefix} ⚪ {module_name:<38} 0 snippet files")
                continue

            try:
                if not dry_run:
                    integrator = MultiTrojanIntegrator(
                        original_rtl=str(sv),
                        trojans_dir=str(snippets_dir),
                    )
                    results = integrator.process_all_trojans()
                    n = len(results) if results else len(snippet_files)
                else:
                    n = len(snippet_files)

                integrated += n
                if verbose:
                    print(f"{prefix} ✅ {module_name:<38} {n:2} trojans integrated")
                else:
                    print(f"{prefix} ✅ {module_name:<38} {n:2} trojans integrated", end='\r')

            except Exception as e:
                failed += 1
                print(f"{prefix} ❌ {module_name:<38} ERROR: {str(e)[:60]}")

        print(f"\n  ✔  {proc.upper()}: {integrated} trojans integrated "
              f"({failed} failed)")
        stats[proc] = {'integrated': integrated, 'failed': failed}

    return stats


# ─────────────────────────────────────────────────────────────────────────────
# Summary
# ─────────────────────────────────────────────────────────────────────────────
def print_summary(s1_stats: dict, s2_stats: dict, duration: float,
                  base_dir: Path, dry_run: bool):
    print("\n" + "═" * 70)
    print("  PIPELINE COMPLETE" + ("  [DRY RUN]" if dry_run else ""))
    print("═" * 70)
    print(f"\n  Total time: {duration:.1f}s\n")

    print(f"  {'Processor':<10} {'Modules':>8} {'Snippets':>10} {'Integrated':>12}")
    print(f"  {'─'*10} {'─'*8} {'─'*10} {'─'*12}")

    total_mod = total_snip = total_int = 0
    for proc in PROCESSORS:
        if proc not in s1_stats and proc not in s2_stats:
            continue
        s1 = s1_stats.get(proc, {})
        s2 = s2_stats.get(proc, {})
        m  = s1.get('modules', 0)
        sn = s1.get('snippets', 0)
        it = s2.get('integrated', 0)
        total_mod  += m
        total_snip += sn
        total_int  += it
        print(f"  {proc.upper():<10} {m:>8} {sn:>10} {it:>12}")

    print(f"  {'─'*10} {'─'*8} {'─'*10} {'─'*12}")
    print(f"  {'TOTAL':<10} {total_mod:>8} {total_snip:>10} {total_int:>12}")

    if not dry_run:
        print(f"\n  Output locations:")
        for proc in PROCESSORS:
            if proc in s1_stats:
                print(f"    {proc.upper():<8} snippets  →  {base_dir / proc / 'generated_trojans'}")
                print(f"    {proc.upper():<8} trojaned  →  {base_dir / proc / 'trojaned_rtl'}")
                print(f"    {proc.upper():<8} testbenches →  {base_dir.parent / 'testbenches' / proc}")

    print()


# ─────────────────────────────────────────────────────────────────────────────
# Entry Point
# ─────────────────────────────────────────────────────────────────────────────
def main():
    ap = argparse.ArgumentParser(
        description='RV-TroGen Full Pipeline — generate + integrate trojans for all processors',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/batch_full_pipeline.py                       # All processors, both stages
  python scripts/batch_full_pipeline.py --processor ibex      # Ibex only
  python scripts/batch_full_pipeline.py --stage1-only         # Only generate snippets
  python scripts/batch_full_pipeline.py --stage2-only         # Only integrate into RTL
  python scripts/batch_full_pipeline.py --dry-run --verbose   # Preview without writing
  python scripts/batch_full_pipeline.py --processor ibex --processor cva6
        """
    )
    ap.add_argument('--processor', '-p', action='append',
                    choices=PROCESSORS, metavar='PROC',
                    help='Processor(s) to run (ibex|cva6|rsd). Repeatable.')
    ap.add_argument('--stage1-only', action='store_true',
                    help='Only generate snippets (skip RTL integration)')
    ap.add_argument('--stage2-only', action='store_true',
                    help='Only integrate trojans (skip snippet generation)')
    ap.add_argument('--dry-run', action='store_true',
                    help='Count and validate without writing any files')
    ap.add_argument('--verbose', '-v', action='store_true',
                    help='Show per-module detail')
    ap.add_argument('--base-dir', default='examples',
                    help='Base examples directory (default: examples)')
    args = ap.parse_args()

    processors = args.processor or PROCESSORS
    base_dir   = ROOT / args.base_dir
    t0         = time.time()

    print()
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║           RV-TroGen Full Pipeline Batch Script                  ║")
    print("╚══════════════════════════════════════════════════════════════════╝")
    print(f"  Processors : {', '.join(p.upper() for p in processors)}")
    print(f"  Stages     : {'Stage 1 only' if args.stage1_only else 'Stage 2 only' if args.stage2_only else 'Stage 1 + Stage 2'}")
    print(f"  Mode       : {'DRY RUN (no files written)' if args.dry_run else 'FULL GENERATION'}")
    print(f"  Base dir   : {base_dir}")
    print(f"  Started    : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    s1_stats = {}
    s2_stats = {}

    if not args.stage2_only:
        s1_stats = stage1_generate_snippets(processors, base_dir,
                                            args.dry_run, args.verbose)

    if not args.stage1_only:
        s2_stats = stage2_integrate_trojans(processors, base_dir,
                                            args.dry_run, args.verbose)

    print_summary(s1_stats, s2_stats, time.time() - t0, base_dir, args.dry_run)


if __name__ == '__main__':
    main()