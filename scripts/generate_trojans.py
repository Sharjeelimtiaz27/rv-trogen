#!/usr/bin/env python3
"""
RV-TroGen - Hardware Trojan Generator
Simple wrapper for easy command-line usage

Usage: python generate_trojans.py examples/ibex/original/<module>.sv
Output: examples/ibex/generated_trojans/<module_name>/

Author: Sharjeel Imtiaz
Repository: https://github.com/sharjeelimtiaz27/rv-trogen
"""

import sys
from pathlib import Path

def main():
    """
    Main wrapper that organizes output into module-specific folders
    
    Input:  examples/ibex/original/ibex_cs_registers.sv
    Output: examples/ibex/generated_trojans/ibex_cs_registers/
    """
    
    # Check arguments
    if len(sys.argv) < 2:
        print("="*70)
        print("RV-TroGen - Hardware Trojan Generator")
        print("="*70)
        print("\nUsage: python generate_trojans.py <rtl_file.sv>\n")
        print("Examples:")
        print("  python generate_trojans.py examples/ibex/original/ibex_cs_registers.sv")
        print("  python generate_trojans.py examples/ibex/original/ibex_pmp.sv")
        print("\nOutput:")
        print("  examples/ibex/generated_trojans/<module_name>/")
        print("="*70)
        sys.exit(1)
    
    input_file = Path(sys.argv[1])
    
    # Check file exists
    if not input_file.exists():
        print(f"❌ Error: File not found: {input_file}")
        print(f"\nMake sure the file path is correct.")
        sys.exit(1)
    
    # Extract module name (without .sv extension)
    module_name = input_file.stem
    
    # Determine output directory based on input location
    # Input:  examples/ibex/original/ibex_cs_registers.sv
    # Output: examples/ibex/generated_trojans/ibex_cs_registers/
    
    if 'examples' in input_file.parts:
        # Find the examples directory index
        parts = list(input_file.parts)
        examples_idx = parts.index('examples')
        
        # Get processor name (e.g., 'ibex', 'cva6', 'rsd')
        if len(parts) > examples_idx + 1:
            processor_name = parts[examples_idx + 1]
        else:
            processor_name = 'unknown'
        
        # Build output path: examples/<processor>/generated_trojans/<module_name>/
        output_dir = Path('examples') / processor_name / 'generated_trojans' / module_name
    else:
        # Default: generated_trojans/<module_name>/ in current directory
        output_dir = Path('generated_trojans') / module_name
    
    # Create output directory (with all parent directories)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Add --output argument to sys.argv for the generator
    sys.argv.append('--output')
    sys.argv.append(str(output_dir))
    
    # Show user where output will go
    print(f"📂 Input:  {input_file}")
    print(f"📁 Output: {output_dir}/")
    print()
    
    # Import and run the main generator
    from src.generator.trojan_generator import main as gen_main
    gen_main()

if __name__ == "__main__":
    main()