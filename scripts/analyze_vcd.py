#!/usr/bin/env python3
"""
VCD Waveform Analyzer and Comparator
Visualizes VCD files and compares original vs Trojan behavior
NOW WITH TIME RANGE FILTERING!
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
        print(f"Parsing {self.vcd_file}...")
        
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
            print(f"  Found {len(signal_map)} signals")
        else:
            print(f"  ⚠️  WARNING: No signals found! VCD file may be empty.")
            
        if self.times:
            print(f"  Time range: {min(self.times)} - {max(self.times)} {self.timescale}")
        else:
            print(f"  ⚠️  WARNING: No time values found! Simulation may not have run.")
        
        return signal_map
    
    def filter_time_range(self, start_time=None, end_time=None):
        """Filter signal values to only include specified time range"""
        if start_time is None and end_time is None:
            return  # No filtering needed
        
        print(f"  Filtering to time range: {start_time or 'start'} - {end_time or 'end'}")
        
        for sig_name in self.signal_values:
            filtered = []
            for time, value in self.signal_values[sig_name]:
                if start_time is not None and time < start_time:
                    continue
                if end_time is not None and time > end_time:
                    continue
                filtered.append((time, value))
            self.signal_values[sig_name] = filtered
        
        # Filter times list
        self.times = [t for t in self.times if (start_time is None or t >= start_time) and (end_time is None or t <= end_time)]

def compare_vcds(original_vcd, trojan_vcd, output_dir='simulation_results/analysis', start_time=None, end_time=None):
    """Compare two VCD files and generate visualizations"""
    
    print("="*70)
    print("VCD WAVEFORM COMPARISON")
    print("="*70)
    
    if start_time is not None or end_time is not None:
        print(f"🔍 TIME RANGE FILTER ACTIVE:")
        if start_time is not None:
            print(f"   Start: {start_time} ns")
        if end_time is not None:
            print(f"   End: {end_time} ns")
    print()
    
    # Parse both VCDs
    orig_parser = VCDParser(original_vcd)
    orig_signals = orig_parser.parse()
    orig_parser.filter_time_range(start_time, end_time)
    
    print()
    
    trojan_parser = VCDParser(trojan_vcd)
    trojan_signals = trojan_parser.parse()
    trojan_parser.filter_time_range(start_time, end_time)
    
    print()
    
    # Check if VCDs are empty
    if not orig_signals:
        print("❌ ERROR: Original VCD has no signals!")
        print("   The VCD file may be empty or corrupted.")
        return
    
    if not trojan_signals:
        print("❌ ERROR: Trojan VCD has no signals!")
        print("   The VCD file may be empty or corrupted.")
        return
    
    print("="*70)
    print("SIGNAL COMPARISON")
    print("="*70)
    print()
    
    # Find common signals
    orig_names = set(orig_parser.signal_values.keys())
    trojan_names = set(trojan_parser.signal_values.keys())
    common_signals = orig_names & trojan_names
    
    print(f"Original VCD signals: {len(orig_names)}")
    print(f"Trojan VCD signals: {len(trojan_names)}")
    print(f"Common signals: {len(common_signals)}")
    print()
    
    if common_signals:
        print("Common signal names:")
        for sig in sorted(list(common_signals)[:20]):  # Show first 20
            print(f"  - {sig}")
        if len(common_signals) > 20:
            print(f"  ... and {len(common_signals)-20} more")
        print()
    
    if not common_signals:
        print("❌ No common signals found!")
        print()
        print("Original signals:")
        for sig in sorted(list(orig_names)[:10]):
            print(f"  - {sig}")
        print()
        print("Trojan signals:")
        for sig in sorted(list(trojan_names)[:10]):
            print(f"  - {sig}")
        return
    
    # Compare signal values
    differences = {}
    
    for sig_name in sorted(common_signals):
        orig_values = orig_parser.signal_values[sig_name]
        trojan_values = trojan_parser.signal_values[sig_name]
        
        # Build time-indexed dictionaries
        orig_dict = {t: v for t, v in orig_values}
        trojan_dict = {t: v for t, v in trojan_values}
        
        # Find all time points
        all_times = sorted(set(list(orig_dict.keys()) + list(trojan_dict.keys())))
        
        # Find differences
        diffs = []
        for time in all_times:
            orig_val = orig_dict.get(time)
            trojan_val = trojan_dict.get(time)
            
            if orig_val is not None and trojan_val is not None and orig_val != trojan_val:
                diffs.append((time, orig_val, trojan_val))
        
        if diffs:
            differences[sig_name] = diffs
            print(f"Signal: {sig_name}")
            print(f"  Differences found: {len(diffs)} time points")
            
            # Show first few differences
            for i, (time, orig_val, trojan_val) in enumerate(diffs[:5]):
                if isinstance(orig_val, int) and isinstance(trojan_val, int):
                    print(f"    Time {time}: Original=0x{orig_val:08x}, Trojan=0x{trojan_val:08x}")
                else:
                    print(f"    Time {time}: Original={orig_val}, Trojan={trojan_val}")
            
            if len(diffs) > 5:
                print(f"    ... and {len(diffs)-5} more differences")
            print()
    
    if not differences:
        print("✅ No differences found - signals are identical!")
        print("   This might mean:")
        print("   1. Trojan trigger didn't activate in this time range")
        print("   2. Trojan payload didn't execute")
        print("   3. Time range is before trigger activation")
        print()
    else:
        print(f"🎯 Total signals with differences: {len(differences)}")
        print()
    
    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Generate text report
    suffix = f"_{start_time}_{end_time}" if (start_time or end_time) else ""
    report_file = output_path / f'comparison_report{suffix}.txt'
    with open(report_file, 'w') as f:
        f.write("VCD WAVEFORM COMPARISON REPORT\n")
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
                
                for time, orig_val, trojan_val in differences[sig_name]:
                    f.write(f"    Time {time:6d} ns: ")
                    if isinstance(orig_val, int) and isinstance(trojan_val, int):
                        f.write(f"Original=0x{orig_val:08x}  ")
                        f.write(f"Trojan=0x{trojan_val:08x}  ")
                        f.write(f"(XOR=0x{orig_val ^ trojan_val:08x})")
                    else:
                        f.write(f"Original={orig_val}  Trojan={trojan_val}")
                    f.write("\n")
                f.write("\n")
        else:
            f.write("No differences found between waveforms.\n")
    
    print(f"📄 Saved: {report_file}")
    
    # Try to create plot if matplotlib available
    try:
        # Plot key signals (handle both flat and hierarchical names)
        plot_signals = ['wr_data_i', 'wr_en_i', 'rd_data_o', 'clk_i', 'rst_ni']
        
        # Try to match signals (exact match or ends with the name)
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
                
                # Get values
                orig_values = orig_parser.signal_values[sig_name]
                trojan_values = trojan_parser.signal_values[sig_name]
                
                # Plot original (blue)
                times_orig = [t for t, v in orig_values]
                vals_orig = [v for t, v in orig_values]
                ax.step(times_orig, vals_orig, 'b-', label='Original', linewidth=2, where='post')
                
                # Plot trojan (red)
                times_trojan = [t for t, v in trojan_values]
                vals_trojan = [v for t, v in trojan_values]
                ax.step(times_trojan, vals_trojan, 'r--', label='Trojan', linewidth=2, alpha=0.7, where='post')
                
                # Highlight differences
                if sig_name in differences:
                    for time, orig_val, trojan_val in differences[sig_name]:
                        ax.axvline(x=time, color='yellow', alpha=0.3, linewidth=3)
                
                # Use short name for label
                short_name = sig_name.split('.')[-1] if '.' in sig_name else sig_name
                ax.set_ylabel(short_name, fontsize=10, fontweight='bold')
                ax.legend(loc='upper right')
                ax.grid(True, alpha=0.3)
            
            axes[-1].set_xlabel('Time (ns)', fontsize=10, fontweight='bold')
            
            title = 'Original vs Trojan Waveform Comparison'
            if start_time is not None or end_time is not None:
                title += f'\nTime Range: {start_time or "start"} - {end_time or "end"} ns'
            fig.suptitle(title, fontsize=14, fontweight='bold')
            
            plt.tight_layout()
            
            output_file = output_path / f'waveform_comparison{suffix}.png'
            plt.savefig(output_file, dpi=300, bbox_inches='tight')
            print(f"📊 Saved: {output_file}")
            plt.close()
        else:
            print(f"⚠️  Could not find standard signals ({', '.join(plot_signals)}) in VCD")
            print(f"   Available signals: {', '.join(list(common_signals)[:10])}")
    except Exception as e:
        print(f"⚠️  Could not generate plot: {e}")
    
    print()
    print("="*70)
    print("ANALYSIS COMPLETE!")
    print("="*70)
    print(f"\n✅ Results saved in: {output_path}")

def main():
    parser = argparse.ArgumentParser(
        description='VCD Waveform Analyzer - Compare original and trojan waveforms',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Analyze full waveforms
  python analyze_vcd.py

  # Analyze specific time range (zoom into trigger region)
  python analyze_vcd.py --start 9000 --end 12000
  
  # Analyze from specific time to end
  python analyze_vcd.py --start 10000
  
  # Analyze from beginning to specific time
  python analyze_vcd.py --end 15000
        """
    )
    
    parser.add_argument('--start', type=int, help='Start time in ns (e.g., 9000)')
    parser.add_argument('--end', type=int, help='End time in ns (e.g., 12000)')
    parser.add_argument('--vcd-dir', default='simulation_results/vcd', help='Directory containing VCD files')
    
    args = parser.parse_args()
    
    print()
    print("="*70)
    print("RV-TROGEN VCD ANALYZER")
    print("="*70)
    print()
    
    # Find VCD files
    vcd_dir = Path(args.vcd_dir)
    
    if not vcd_dir.exists():
        print(f"❌ Error: {vcd_dir} not found!")
        print("Please download VCD files from server first.")
        print()
        print("Commands to download:")
        print("  scp sharjeel@ekleer.pld.ttu.ee:/path/to/*.vcd simulation_results/vcd/")
        return
    
    vcd_files = list(vcd_dir.glob('*.vcd'))
    
    if len(vcd_files) == 0:
        print(f"❌ No VCD files found in {vcd_dir}")
        return
    
    print(f"Found {len(vcd_files)} VCD files:")
    for vcd in vcd_files:
        size = vcd.stat().st_size
        print(f"  - {vcd.name} ({size:,} bytes)")
    print()
    
    # Check for empty VCD files
    for vcd in vcd_files:
        if vcd.stat().st_size < 500:
            print(f"⚠️  WARNING: {vcd.name} is suspiciously small ({vcd.stat().st_size} bytes)")
            print(f"   This VCD file may be empty or incomplete.")
            print()
    
    # Find original and trojan VCDs
    original_vcd = None
    trojan_vcd = None
    
    for vcd in vcd_files:
        if 'trojan' in vcd.name.lower():
            trojan_vcd = vcd
        else:
            original_vcd = vcd
    
    if original_vcd and trojan_vcd:
        print(f"Comparing:")
        print(f"  Original: {original_vcd.name}")
        print(f"  Trojan:   {trojan_vcd.name}")
        if args.start or args.end:
            print(f"  Time Range: {args.start or 'start'} - {args.end or 'end'} ns")
        print()
        
        compare_vcds(str(original_vcd), str(trojan_vcd), start_time=args.start, end_time=args.end)
    else:
        print("❌ Could not find both original and trojan VCD files")
        print("   Expected filenames to contain 'trojan' for trojan VCD")

if __name__ == "__main__":
    main()