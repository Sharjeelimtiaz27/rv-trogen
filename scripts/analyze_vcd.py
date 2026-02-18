#!/usr/bin/env python3
"""
VCD Waveform Analyzer and Comparator - MULTI-TROJAN VERSION
Compares original VCD with ALL trojan variants (DoS, Integrity, Covert, Leak, Privilege, Availability)
WITH TIME RANGE FILTERING & PROCESSOR/MODULE-SPECIFIC OUTPUT

Author: Sharjeel Imtiaz (TalTech)
Date: February 2026
"""

import sys
from pathlib import Path
import matplotlib.pyplot as plt
from collections import defaultdict
import argparse

sys.path.insert(0, str(Path(__file__).parent.parent))

class VCDParser:
    """Simple VCD file parser"""
    
    def __init__(self, vcd_file):
        self.vcd_file = vcd_file
        self.signals = {}
        self.timescale = "1ns"
        self.signal_values = defaultdict(list)
        self.times = []
        
    def parse(self):
        """Parse VCD file"""
        print(f"  Parsing {Path(self.vcd_file).name}...")
        
        with open(self.vcd_file, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        
        # Phase 1: Parse signal definitions
        signal_map = {}
        in_definitions = True
        current_time = 0
        
        for line in lines:
            line = line.strip()
            
            if not line:
                continue
                
            if line.startswith('$timescale'):
                parts = line.split()
                if len(parts) >= 2:
                    self.timescale = parts[1]
                    
            elif line.startswith('$var'):
                # $var wire 32 ! wr_data_i [31:0] $end
                parts = line.split()
                if len(parts) >= 5:
                    var_type = parts[1]
                    width = int(parts[2])
                    symbol = parts[3]
                    name = parts[4]
                    signal_map[symbol] = {
                        'name': name,
                        'width': width,
                        'type': var_type
                    }
                    
            elif line.startswith('$enddefinitions'):
                in_definitions = False
                
            elif not in_definitions and line.startswith('#'):
                # Timestamp
                try:
                    current_time = int(line[1:])
                    if current_time not in self.times:
                        self.times.append(current_time)
                except:
                    pass
                    
            elif not in_definitions and len(line) > 0:
                # Signal value change
                if line.startswith('b'):
                    # Binary value: b10101010 !
                    parts = line.split()
                    if len(parts) >= 2:
                        value_str = parts[0][1:]  # Remove 'b'
                        symbol = parts[1]
                        try:
                            # Handle x and z
                            value_str = value_str.replace('x', '0').replace('z', '0').replace('X', '0').replace('Z', '0')
                            value = int(value_str, 2)
                        except:
                            value = 0
                            
                        if symbol in signal_map:
                            sig_name = signal_map[symbol]['name']
                            self.signal_values[sig_name].append((current_time, value))
                            
                elif line[0] in '01xzXZ':
                    # Single bit: 0! or 1!
                    try:
                        value = 1 if line[0] in '1' else 0
                        symbol = line[1:].strip()
                        if symbol in signal_map:
                            sig_name = signal_map[symbol]['name']
                            self.signal_values[sig_name].append((current_time, value))
                    except:
                        pass
        
        if signal_map:
            print(f"    ✓ Found {len(signal_map)} signals")
        else:
            print(f"    ⚠️  WARNING: No signals found!")
            
        if self.times:
            print(f"    ✓ Time range: {min(self.times)} - {max(self.times)} {self.timescale}")
        else:
            print(f"    ⚠️  WARNING: No time values found!")
        
        return signal_map
    
    def filter_time_range(self, start_time=None, end_time=None):
        """Filter signal values to only include specified time range"""
        if start_time is None and end_time is None:
            return
        
        for sig_name in self.signal_values:
            filtered = []
            for time, value in self.signal_values[sig_name]:
                if start_time is not None and time < start_time:
                    continue
                if end_time is not None and time > end_time:
                    continue
                filtered.append((time, value))
            self.signal_values[sig_name] = filtered
        
        self.times = [t for t in self.times if (start_time is None or t >= start_time) and (end_time is None or t <= end_time)]


def compare_two_vcds(original_vcd, trojan_vcd, trojan_name, orig_parser, output_path, start_time, end_time):
    """Compare original with one specific trojan VCD"""
    
    print(f"\n{'─'*70}")
    print(f"  Comparing: ORIGINAL vs {trojan_name.upper()}")
    print(f"{'─'*70}")
    
    # Parse trojan VCD
    trojan_parser = VCDParser(trojan_vcd)
    trojan_signals = trojan_parser.parse()
    trojan_parser.filter_time_range(start_time, end_time)
    
    if not trojan_signals:
        print(f"    ❌ ERROR: {trojan_name} VCD has no signals!")
        return None
    
    # Find common signals
    orig_names = set(orig_parser.signal_values.keys())
    trojan_names = set(trojan_parser.signal_values.keys())
    common_signals = orig_names & trojan_names
    
    if not common_signals:
        print(f"    ❌ No common signals found!")
        return None
    
    # Compare signal values
    differences = {}
    
    for sig_name in sorted(common_signals):
        orig_values = orig_parser.signal_values[sig_name]
        trojan_values = trojan_parser.signal_values[sig_name]
        
        orig_dict = {t: v for t, v in orig_values}
        trojan_dict = {t: v for t, v in trojan_values}
        
        all_times = sorted(set(list(orig_dict.keys()) + list(trojan_dict.keys())))
        
        diffs = []
        for time in all_times:
            orig_val = orig_dict.get(time)
            trojan_val = trojan_dict.get(time)
            
            if orig_val is not None and trojan_val is not None and orig_val != trojan_val:
                diffs.append((time, orig_val, trojan_val))
        
        if diffs:
            differences[sig_name] = diffs
    
    if differences:
        print(f"    ✓ Found differences in {len(differences)} signal(s)")
        for sig_name in list(differences.keys())[:3]:
            print(f"      - {sig_name}: {len(differences[sig_name])} differences")
        if len(differences) > 3:
            print(f"      ... and {len(differences)-3} more signals")
    else:
        print(f"    ⚪ No differences found (trojan may not have activated)")
    
    # Generate text report
    suffix = f"_{start_time}_{end_time}" if (start_time or end_time) else ""
    report_file = output_path / f'comparison_{trojan_name}{suffix}.txt'
    
    with open(report_file, 'w') as f:
        f.write(f"VCD COMPARISON REPORT: ORIGINAL vs {trojan_name.upper()}\n")
        f.write("="*70 + "\n\n")
        f.write(f"Original VCD: {original_vcd}\n")
        f.write(f"Trojan VCD: {trojan_vcd}\n")
        if start_time is not None or end_time is not None:
            f.write(f"Time Range: {start_time or 'start'} - {end_time or 'end'} ns\n")
        f.write(f"\nTotal signals compared: {len(common_signals)}\n")
        f.write(f"Signals with differences: {len(differences)}\n\n")
        
        if differences:
            f.write("DETAILED DIFFERENCES:\n")
            f.write("="*70 + "\n\n")
            
            for sig_name in sorted(differences.keys()):
                f.write(f"Signal: {sig_name}\n")
                f.write(f"  Number of differences: {len(differences[sig_name])}\n")
                f.write(f"  Time points with differences:\n")
                
                for time, orig_val, trojan_val in differences[sig_name][:50]:  # Limit to first 50
                    f.write(f"    Time {time:6d} ns: ")
                    if isinstance(orig_val, int) and isinstance(trojan_val, int):
                        f.write(f"Original=0x{orig_val:08x}  ")
                        f.write(f"Trojan=0x{trojan_val:08x}  ")
                        f.write(f"(XOR=0x{orig_val ^ trojan_val:08x})")
                    else:
                        f.write(f"Original={orig_val}  Trojan={trojan_val}")
                    f.write("\n")
                
                if len(differences[sig_name]) > 50:
                    f.write(f"    ... and {len(differences[sig_name])-50} more differences\n")
                f.write("\n")
        else:
            f.write("No differences found between waveforms.\n")
    
    print(f"    📄 Report saved: {report_file.name}")
    
    # Generate plot
    try:
        plot_signals = ['wr_data_i', 'wr_en_i', 'rd_data_o', 'clk_i', 'rst_ni']
        available_signals = []
        
        for target in plot_signals:
            for sig in common_signals:
                if sig == target or sig.endswith('.' + target) or sig.endswith('/' + target):
                    available_signals.append(sig)
                    break
        
        if available_signals:
            fig, axes = plt.subplots(len(available_signals), 1, figsize=(15, 3*len(available_signals)))
            if len(available_signals) == 1:
                axes = [axes]
            
            for idx, sig_name in enumerate(available_signals):
                ax = axes[idx]
                
                orig_values = orig_parser.signal_values[sig_name]
                trojan_values = trojan_parser.signal_values[sig_name]
                
                times_orig = [t for t, v in orig_values]
                vals_orig = [v for t, v in orig_values]
                ax.step(times_orig, vals_orig, 'b-', label='Original', linewidth=2, where='post')
                
                times_trojan = [t for t, v in trojan_values]
                vals_trojan = [v for t, v in trojan_values]
                ax.step(times_trojan, vals_trojan, 'r--', label=trojan_name, linewidth=2, alpha=0.7, where='post')
                
                if sig_name in differences:
                    for time, orig_val, trojan_val in differences[sig_name]:
                        ax.axvline(x=time, color='yellow', alpha=0.3, linewidth=3)
                
                short_name = sig_name.split('.')[-1] if '.' in sig_name else sig_name
                ax.set_ylabel(short_name, fontsize=10, fontweight='bold')
                ax.legend(loc='upper right')
                ax.grid(True, alpha=0.3)
            
            axes[-1].set_xlabel('Time (ns)', fontsize=10, fontweight='bold')
            
            title = f'Original vs {trojan_name.upper()} Trojan'
            if start_time is not None or end_time is not None:
                title += f'\nTime Range: {start_time or "start"} - {end_time or "end"} ns'
            fig.suptitle(title, fontsize=14, fontweight='bold')
            
            plt.tight_layout()
            
            output_file = output_path / f'waveform_{trojan_name}{suffix}.png'
            plt.savefig(output_file, dpi=300, bbox_inches='tight')
            print(f"    📊 Plot saved: {output_file.name}")
            plt.close()
    except Exception as e:
        print(f"    ⚠️  Could not generate plot: {e}")
    
    return {
        'trojan_name': trojan_name,
        'differences': len(differences),
        'signals_affected': list(differences.keys())
    }


def compare_all_vcds(original_vcd, trojan_vcds, processor='ibex', module='ibex_csr', start_time=None, end_time=None):
    """Compare original with ALL trojan VCDs"""
    
    print("\n" + "="*70)
    print("  RV-TROGEN MULTI-TROJAN VCD ANALYSIS")
    print("="*70)
    print(f"\n  Processor: {processor.upper()}")
    print(f"  Module: {module}")
    
    if start_time is not None or end_time is not None:
        print(f"\n  🔍 TIME RANGE FILTER:")
        if start_time is not None:
            print(f"     Start: {start_time} ns")
        if end_time is not None:
            print(f"     End: {end_time} ns")
    
    print(f"\n  Original VCD: {Path(original_vcd).name}")
    print(f"  Trojan VCDs: {len(trojan_vcds)} files")
    for tv in trojan_vcds:
        print(f"    - {tv['name']}")
    
    # Parse original VCD once
    print(f"\n{'─'*70}")
    print("  Parsing ORIGINAL VCD")
    print(f"{'─'*70}")
    
    orig_parser = VCDParser(original_vcd)
    orig_signals = orig_parser.parse()
    orig_parser.filter_time_range(start_time, end_time)
    
    if not orig_signals:
        print("  ❌ ERROR: Original VCD has no signals!")
        return
    
    # Create output directory
    output_path = Path(f'simulation_results/analysis/{processor}/{module}')
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Compare with each trojan
    results = []
    for trojan_info in trojan_vcds:
        result = compare_two_vcds(
            original_vcd, 
            trojan_info['path'], 
            trojan_info['name'],
            orig_parser,
            output_path,
            start_time,
            end_time
        )
        if result:
            results.append(result)
    
    # Generate summary report
    suffix = f"_{start_time}_{end_time}" if (start_time or end_time) else ""
    summary_file = output_path / f'SUMMARY_ALL_TROJANS{suffix}.txt'
    
    with open(summary_file, 'w') as f:
        f.write("="*70 + "\n")
        f.write("MULTI-TROJAN COMPARISON SUMMARY\n")
        f.write("="*70 + "\n\n")
        f.write(f"Processor: {processor.upper()}\n")
        f.write(f"Module: {module}\n")
        f.write(f"Original VCD: {original_vcd}\n")
        if start_time is not None or end_time is not None:
            f.write(f"Time Range: {start_time or 'start'} - {end_time or 'end'} ns\n")
        f.write(f"\nTotal Trojans Analyzed: {len(results)}\n\n")
        
        f.write("="*70 + "\n")
        f.write("TROJAN COMPARISON RESULTS\n")
        f.write("="*70 + "\n\n")
        
        for result in results:
            f.write(f"Trojan: {result['trojan_name'].upper()}\n")
            f.write(f"  Signals with differences: {result['differences']}\n")
            if result['signals_affected']:
                f.write(f"  Affected signals:\n")
                for sig in result['signals_affected'][:10]:
                    f.write(f"    - {sig}\n")
                if len(result['signals_affected']) > 10:
                    f.write(f"    ... and {len(result['signals_affected'])-10} more\n")
            else:
                f.write(f"  Status: No differences detected (trojan may not have activated)\n")
            f.write("\n")
        
        f.write("="*70 + "\n")
        f.write("ANALYSIS COMPLETE\n")
        f.write("="*70 + "\n")
    
    print(f"\n{'='*70}")
    print("  ANALYSIS COMPLETE!")
    print(f"{'='*70}")
    print(f"\n  📁 Results saved in: {output_path}")
    print(f"  📄 Summary report: {summary_file.name}")
    print(f"\n  Individual reports and plots generated for each trojan:")
    for result in results:
        print(f"    ✓ {result['trojan_name'].upper()}: {result['differences']} signal(s) affected")
    print()


def main():
    parser = argparse.ArgumentParser(
        description='VCD Multi-Trojan Analyzer - Compare original with ALL trojan variants',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Analyze all trojans in directory
  python scripts/analyze_vcd.py --vcd-dir simulation_results/vcd/ibex/ibex_csr

  # Analyze specific time range (zoom into trigger region)
  python scripts/analyze_vcd.py --vcd-dir simulation_results/vcd/ibex/ibex_csr --start 30100 --end 30200
  
  # Manually specify processor and module
  python scripts/analyze_vcd.py --processor ibex --module ibex_csr --start 10000 --end 15000
        """
    )
    
    parser.add_argument('--start', type=int, help='Start time in ns (e.g., 30100)')
    parser.add_argument('--end', type=int, help='End time in ns (e.g., 30200)')
    parser.add_argument('--vcd-dir', default='simulation_results/vcd/ibex/ibex_csr', 
                       help='Directory containing VCD files')
    parser.add_argument('--processor', default=None, 
                       help='Processor name (auto-detect if not specified)')
    parser.add_argument('--module', default=None, 
                       help='Module name (auto-detect if not specified)')
    
    args = parser.parse_args()
    
    print()
    print("="*70)
    print("  RV-TROGEN VCD ANALYZER - MULTI-TROJAN VERSION")
    print("="*70)
    print()
    
    # Find VCD files
    vcd_dir = Path(args.vcd_dir)
    
    if not vcd_dir.exists():
        print(f"❌ Error: {vcd_dir} not found!")
        print("\nPlease download VCD files from server first.")
        print("\nCommands to download:")
        print(f"  scp sharjeel@ekleer.pld.ttu.ee:/path/to/*.vcd {vcd_dir}/")
        return
    
    # Auto-detect processor and module from path
    processor = args.processor
    module = args.module
    
    if processor is None or module is None:
        parts = vcd_dir.parts
        if 'vcd' in parts:
            vcd_idx = parts.index('vcd')
            if len(parts) > vcd_idx + 1:
                processor = processor or parts[vcd_idx + 1]
            if len(parts) > vcd_idx + 2:
                module = module or parts[vcd_idx + 2]
    
    processor = processor or 'ibex'
    module = module or 'ibex_csr'
    
    # Find all VCD files
    vcd_files = list(vcd_dir.glob('*.vcd'))
    
    if len(vcd_files) == 0:
        print(f"❌ No VCD files found in {vcd_dir}")
        return
    
    print(f"Found {len(vcd_files)} VCD files:")
    for vcd in vcd_files:
        size = vcd.stat().st_size
        print(f"  - {vcd.name} ({size:,} bytes)")
    print()
    
    # Identify original and trojan VCDs
    original_vcd = None
    trojan_vcds = []
    
    trojan_patterns = ['DoS', 'Integrity', 'Covert', 'Leak', 'Privilege', 'Availability']
    
    for vcd in vcd_files:
        vcd_name = vcd.name
        
        # Check if it's a trojan VCD
        is_trojan = False
        trojan_type = None
        
        for pattern in trojan_patterns:
            if pattern.lower() in vcd_name.lower():
                is_trojan = True
                trojan_type = pattern
                break
        
        if is_trojan and trojan_type:
            trojan_vcds.append({
                'path': str(vcd),
                'name': trojan_type
            })
        else:
            # Assume it's the original
            if original_vcd is None:
                original_vcd = str(vcd)
    
    if not original_vcd:
        print("❌ Could not find original VCD file!")
        print("   Expected a VCD without trojan pattern names (DoS, Integrity, etc.)")
        return
    
    if not trojan_vcds:
        print("❌ Could not find any trojan VCD files!")
        print("   Expected VCD filenames containing: DoS, Integrity, Covert, Leak, Privilege, or Availability")
        return
    
    # Sort trojans by name
    trojan_vcds.sort(key=lambda x: x['name'])
    
    # Run comparison
    compare_all_vcds(
        original_vcd, 
        trojan_vcds, 
        processor=processor, 
        module=module,
        start_time=args.start, 
        end_time=args.end
    )


if __name__ == "__main__":
    main()