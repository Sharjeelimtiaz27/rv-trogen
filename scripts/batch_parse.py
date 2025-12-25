#!/usr/bin/env python3
"""
Batch Parser for Multiple RTL Modules
Parse all modules in a directory or specific list
"""

import sys
from pathlib import Path
from typing import List, Dict
import json

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.parser import RTLParser


class BatchParser:
    """Parse multiple RTL files"""
    
    def __init__(self, output_dir: str = "parsed_results"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.results = []
        
    def parse_directory(self, directory: str, pattern: str = "*.sv") -> List:
        """
        Parse all .sv files in a directory
        
        Args:
            directory: Path to directory
            pattern: File pattern (default: *.sv, can use *.v for Verilog)
        
        Returns:
            List of parsed Module objects
        """
        dir_path = Path(directory)
        
        if not dir_path.exists():
            print(f"❌ Directory not found: {directory}")
            return []
        
        # Find all matching files
        files = list(dir_path.glob(pattern))
        
        if not files:
            print(f"❌ No {pattern} files found in {directory}")
            return []
        
        print(f"\n🔍 Found {len(files)} files to parse\n")
        
        modules = []
        errors = []
        
        for i, file_path in enumerate(files, 1):
            print(f"[{i}/{len(files)}] Parsing: {file_path.name}...", end=" ")
            
            try:
                parser = RTLParser(str(file_path))
                module = parser.parse()
                modules.append(module)
                print("✅")
                
            except Exception as e:
                print(f"❌ Error: {e}")
                errors.append((file_path.name, str(e)))
        
        # Summary
        print(f"\n{'='*60}")
        print(f"✅ Successfully parsed: {len(modules)}/{len(files)}")
        if errors:
            print(f"❌ Failed: {len(errors)}")
            for filename, error in errors:
                print(f"   - {filename}: {error}")
        print(f"{'='*60}\n")
        
        self.results = modules
        return modules
    
    def parse_file_list(self, file_paths: List[str]) -> List:
        """
        Parse specific list of files
        
        Args:
            file_paths: List of file paths
        
        Returns:
            List of parsed Module objects
        """
        print(f"\n🔍 Parsing {len(file_paths)} files\n")
        
        modules = []
        
        for i, file_path in enumerate(file_paths, 1):
            print(f"[{i}/{len(file_paths)}] {Path(file_path).name}...", end=" ")
            
            try:
                parser = RTLParser(file_path)
                module = parser.parse()
                modules.append(module)
                print("✅")
            except Exception as e:
                print(f"❌ {e}")
        
        self.results = modules
        return modules
    
    def filter_security_critical(self, modules: List = None) -> List:
        """
        Filter security-critical modules
        
        Security-critical modules include:
        - CSR (Control & Status Registers)
        - PMP (Physical Memory Protection)
        - Controller (Instruction control)
        - Privilege/Exception handlers
        - Debug modules
        - Memory protection units
        """
        if modules is None:
            modules = self.results
        
        security_keywords = [
            'csr', 'cs_registers',  # CSR
            'pmp',                   # PMP
            'controller',            # Main controller
            'privilege', 'priv',     # Privilege
            'exception', 'exc',      # Exception handling
            'debug',                 # Debug module
            'mpu',                   # Memory protection
            'secure', 'security',    # Security features
            'crypto', 'aes', 'rsa',  # Cryptographic
        ]
        
        security_modules = []
        
        for module in modules:
            module_name_lower = module.name.lower()
            
            # Check if module name contains security keywords
            if any(keyword in module_name_lower for keyword in security_keywords):
                security_modules.append(module)
        
        return security_modules
    
    def generate_summary_report(self, modules: List = None) -> Dict:
        """Generate summary statistics"""
        if modules is None:
            modules = self.results
        
        if not modules:
            return {}
        
        summary = {
            'total_modules': len(modules),
            'sequential': sum(1 for m in modules if m.is_sequential),
            'combinational': sum(1 for m in modules if not m.is_sequential),
            'with_clock': sum(1 for m in modules if m.has_clock),
            'with_reset': sum(1 for m in modules if m.has_reset),
            'total_inputs': sum(len(m.inputs) for m in modules),
            'total_outputs': sum(len(m.outputs) for m in modules),
            'total_internals': sum(len(m.internals) for m in modules),
            'modules': []
        }
        
        for module in modules:
            summary['modules'].append({
                'name': module.name,
                'file': module.file_path.name,
                'type': 'Sequential' if module.is_sequential else 'Combinational',
                'inputs': len(module.inputs),
                'outputs': len(module.outputs),
                'internals': len(module.internals),
                'has_clock': module.has_clock,
                'has_reset': module.has_reset
            })
        
        return summary
    
    def save_summary_json(self, filename: str = "parse_summary.json"):
        """Save summary as JSON"""
        summary = self.generate_summary_report()
        
        output_path = self.output_dir / filename
        
        with open(output_path, 'w') as f:
            json.dump(summary, f, indent=2)
        
        print(f"📄 Summary saved to: {output_path}")
        
    def print_summary(self, modules: List = None):
        """Print summary to console"""
        if modules is None:
            modules = self.results
        
        summary = self.generate_summary_report(modules)
        
        print(f"\n{'='*60}")
        print(f"PARSING SUMMARY")
        print(f"{'='*60}")
        print(f"Total Modules:    {summary['total_modules']}")
        print(f"Sequential:       {summary['sequential']}")
        print(f"Combinational:    {summary['combinational']}")
        print(f"With Clock:       {summary['with_clock']}")
        print(f"With Reset:       {summary['with_reset']}")
        print(f"Total Signals:    {summary['total_inputs'] + summary['total_outputs'] + summary['total_internals']}")
        print(f"  - Inputs:       {summary['total_inputs']}")
        print(f"  - Outputs:      {summary['total_outputs']}")
        print(f"  - Internals:    {summary['total_internals']}")
        print(f"{'='*60}\n")


def main():
    """Command-line interface"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Batch parse RTL modules',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Parse all .sv files in a directory
  python scripts/batch_parse.py --dir examples/ibex/original

  # Parse specific files
  python scripts/batch_parse.py --files module1.sv module2.sv

  # Parse and filter security-critical only
  python scripts/batch_parse.py --dir examples/ibex/original --security-only

  # Save results to JSON
  python scripts/batch_parse.py --dir examples/ibex/original --save-json
        """
    )
    
    parser.add_argument('--dir', '-d', help='Directory containing RTL files')
    parser.add_argument('--files', '-f', nargs='+', help='Specific files to parse')
    parser.add_argument('--pattern', '-p', default='*.sv', help='File pattern (default: *.sv)')
    parser.add_argument('--security-only', '-s', action='store_true', 
                       help='Show only security-critical modules')
    parser.add_argument('--save-json', '-j', action='store_true',
                       help='Save summary as JSON')
    parser.add_argument('--output-dir', '-o', default='parsed_results',
                       help='Output directory (default: parsed_results)')
    
    args = parser.parse_args()
    
    # Create batch parser
    batch = BatchParser(output_dir=args.output_dir)
    
    # Parse files
    if args.dir:
        modules = batch.parse_directory(args.dir, args.pattern)
    elif args.files:
        modules = batch.parse_file_list(args.files)
    else:
        parser.print_help()
        return
    
    if not modules:
        print("❌ No modules parsed successfully")
        return
    
    # Filter security-critical if requested
    if args.security_only:
        security_modules = batch.filter_security_critical(modules)
        print(f"\n🔐 Security-Critical Modules: {len(security_modules)}/{len(modules)}\n")
        
        for module in security_modules:
            module.print_summary()
        
        modules = security_modules
    else:
        # Print all modules
        for module in modules:
            module.print_summary()
    
    # Print summary
    batch.print_summary(modules)
    
    # Save JSON if requested
    if args.save_json:
        batch.save_summary_json()


if __name__ == "__main__":
    main()