#!/usr/bin/env python3
"""
Signal Extraction Helper
Automatically extracts signals from all modules in a processor directory
Outputs Python dict ready to paste into classify_signals.py

Usage:
    python extract_signals_helper.py examples/ibex/original ibex
    python extract_signals_helper.py examples/cva6/original cva6
    python extract_signals_helper.py examples/rsd/original rsd
"""

import sys
from pathlib import Path

# Add project to path
sys.path.insert(0, str(Path.cwd()))

from src.parser import RTLParser


def extract_signals_from_directory(directory: Path, processor_name: str):
    """
    Extract all signals from all .sv files in directory
    
    Args:
        directory: Path to processor's original modules
        processor_name: Name of processor (ibex, cva6, rsd)
    
    Returns:
        Dict of module_name -> {inputs, outputs, internals}
    """
    print(f"🔍 Scanning: {directory}")
    print(f"📊 Processor: {processor_name}\n")
    
    all_signals = {}
    sv_files = list(directory.glob("*.sv"))
    
    print(f"Found {len(sv_files)} SystemVerilog files\n")
    
    for i, sv_file in enumerate(sv_files, 1):
        try:
            print(f"[{i}/{len(sv_files)}] Parsing {sv_file.name}...", end=' ')
            
            parser = RTLParser(str(sv_file))
            module = parser.parse()
            
            # Extract signal names
            inputs = [s.name for s in module.inputs]
            outputs = [s.name for s in module.outputs]
            
            # Get internal signals if available
            try:
                internals = [s.name for s in module.get_internal_signals()]
            except:
                internals = []
            
            all_signals[module.name] = {
                'inputs': inputs,
                'outputs': outputs,
                'internals': internals
            }
            
            signal_count = len(inputs) + len(outputs) + len(internals)
            print(f"✓ ({signal_count} signals)")
            
        except Exception as e:
            print(f"✗ Error: {str(e)[:50]}")
    
    return all_signals


def format_for_classifier(processor_name: str, all_signals: dict) -> str:
    """
    Format signal dict for pasting into classify_signals.py
    
    Returns:
        Python code ready to paste
    """
    lines = []
    lines.append(f"'{processor_name}': {{")
    
    for module_name, signals in sorted(all_signals.items()):
        lines.append(f"    '{module_name}': {{")
        lines.append(f"        'inputs': {signals['inputs']},")
        lines.append(f"        'outputs': {signals['outputs']},")
        lines.append(f"        'internals': {signals['internals']}")
        lines.append(f"    }},")
    
    lines.append("},")
    
    return '\n'.join(lines)


def save_to_file(processor_name: str, formatted_output: str):
    """Save formatted output to file"""
    output_file = Path(f"signals_{processor_name}.txt")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Copy this into classify_signals.py PROCESSOR_SIGNALS dict\n\n")
        f.write(formatted_output)
    
    return output_file


def print_statistics(processor_name: str, all_signals: dict):
    """Print statistics about extracted signals"""
    print("\n" + "=" * 70)
    print(f"📊 {processor_name.upper()} EXTRACTION STATISTICS")
    print("=" * 70)
    
    total_modules = len(all_signals)
    total_inputs = sum(len(s['inputs']) for s in all_signals.values())
    total_outputs = sum(len(s['outputs']) for s in all_signals.values())
    total_internals = sum(len(s['internals']) for s in all_signals.values())
    total_signals = total_inputs + total_outputs + total_internals
    
    print(f"\nTotal Modules:        {total_modules}")
    print(f"Total Input Signals:  {total_inputs}")
    print(f"Total Output Signals: {total_outputs}")
    print(f"Total Internal Signals: {total_internals}")
    print(f"Total Signals:        {total_signals}")
    
    print(f"\nAverage signals per module: {total_signals / total_modules:.1f}")
    
    # Show modules with most signals
    signal_counts = [(name, sum(len(s[t]) for t in ['inputs', 'outputs', 'internals']))
                     for name, s in all_signals.items()]
    signal_counts.sort(key=lambda x: x[1], reverse=True)
    
    print(f"\nTop 5 modules by signal count:")
    for name, count in signal_counts[:5]:
        print(f"  {name:30} - {count:3} signals")
    
    print("\n" + "=" * 70)


def main():
    """Main extraction workflow"""
    if len(sys.argv) != 3:
        print("Usage: python extract_signals_helper.py <directory> <processor_name>")
        print("\nExamples:")
        print("  python extract_signals_helper.py examples/ibex/original ibex")
        print("  python extract_signals_helper.py examples/cva6/original cva6")
        print("  python extract_signals_helper.py examples/rsd/original rsd")
        sys.exit(1)
    
    directory = Path(sys.argv[1])
    processor_name = sys.argv[2]
    
    if not directory.exists():
        print(f"❌ Error: Directory not found: {directory}")
        sys.exit(1)
    
    print("=" * 70)
    print("SIGNAL EXTRACTION HELPER")
    print("=" * 70)
    print()
    
    # Extract signals
    all_signals = extract_signals_from_directory(directory, processor_name)
    
    if not all_signals:
        print("\n❌ No signals extracted!")
        sys.exit(1)
    
    # Format for classifier
    formatted_output = format_for_classifier(processor_name, all_signals)
    
    # Save to file
    output_file = save_to_file(processor_name, formatted_output)
    
    # Print statistics
    print_statistics(processor_name, all_signals)
    
    # Print output
    print(f"\n✅ Saved to: {output_file.absolute()}")
    print(f"\n📋 Copy the contents to classify_signals.py:")
    print("=" * 70)
    print(formatted_output)
    print("=" * 70)
    
    print("\n💡 Next steps:")
    print("1. Open classify_signals.py")
    print("2. Find PROCESSOR_SIGNALS dict (around line 75)")
    print(f"3. Paste the contents from {output_file}")
    print("4. Repeat for other processors (cva6, rsd)")
    print("5. Run: python classify_signals.py")


if __name__ == "__main__":
    main()
