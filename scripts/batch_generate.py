#!/usr/bin/env python3
"""
Enhanced Batch Trojan Generation Script with Detailed Statistics
Generates Trojans for all modules across all processors with comprehensive reporting

Usage:
    python scripts/batch_generate.py                    # All processors
    python scripts/batch_generate.py --processor ibex   # Single processor
    python scripts/batch_generate.py --dry-run          # Test without generating
    python scripts/batch_generate.py --detailed         # Show per-module breakdown
"""

import sys
import argparse
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import time

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.generator.trojan_generator import TrojanGenerator


class EnhancedBatchGenerator:
    """Enhanced batch generator with detailed statistics"""
    
    # Pattern names mapping
    PATTERN_NAMES = {
        'dos': 'DoS',
        'leak': 'Information Leakage',
        'privilege': 'Privilege Escalation',
        'integrity': 'Data Integrity',
        'availability': 'Performance Degradation',
        'covert': 'Covert Channel'
    }
    
    def __init__(self, base_dir: str = "examples"):
        """
        Initialize enhanced batch generator
        
        Args:
            base_dir: Base directory containing processor folders
        """
        self.base_dir = Path(base_dir)
        self.processors = {
            'ibex': self.base_dir / 'ibex',
            'cva6': self.base_dir / 'cva6',
            'rsd': self.base_dir / 'rsd'
        }
        
        self.global_stats = {
            'start_time': None,
            'end_time': None,
            'total_modules': 0,
            'total_trojans': 0,
            'processors': {}
        }
        
        self.detailed_results = []
    
    def find_modules(self, processor_name: str) -> list:
        """
        Find all .sv modules for a processor
        
        Args:
            processor_name: Name of processor (ibex, cva6, rsd)
            
        Returns:
            List of .sv file paths
        """
        processor_dir = self.processors[processor_name]
        original_dir = processor_dir / 'original'
        
        if not original_dir.exists():
            print(f"⚠️  Warning: {original_dir} not found")
            return []
        
        modules = list(original_dir.glob('*.sv'))
        return modules
    
    def generate_for_processor(self, processor_name: str, dry_run: bool = False, detailed: bool = False):
        """
        Generate Trojans for all modules of one processor with detailed stats
        
        Args:
            processor_name: Name of processor
            dry_run: If True, only count modules without generating
            detailed: If True, show per-module breakdown
        """
        print(f"\n{'='*80}")
        print(f"📊 PROCESSOR: {processor_name.upper()}")
        print(f"{'='*80}")
        
        # Find modules
        modules = self.find_modules(processor_name)
        
        if not modules:
            print(f"❌ No modules found for {processor_name}")
            return
        
        print(f"📁 Found {len(modules)} .sv files in examples/{processor_name}/original/")
        
        # Test parsing first
        print(f"\n🔍 Validating modules...")
        valid_modules = []
        invalid_modules = []
        
        for module_file in modules:
            try:
                # Quick parse test
                from src.parser import RTLParser
                parser = RTLParser(str(module_file))
                parser.parse()
                valid_modules.append(module_file)
            except Exception as e:
                invalid_modules.append((module_file.name, str(e)[:50]))
        
        print(f"✅ Valid modules: {len(valid_modules)}")
        if invalid_modules:
            print(f"⚠️  Skipped (packages/interfaces): {len(invalid_modules)}")
            if detailed:
                for name, error in invalid_modules:
                    print(f"    - {name}: {error}...")
        
        if dry_run:
            print(f"\n📋 DRY RUN: Would generate Trojans for {len(valid_modules)} modules")
            return
        
        # Initialize processor stats
        processor_stats = {
            'name': processor_name,
            'total_modules': len(modules),
            'valid_modules': len(valid_modules),
            'invalid_modules': len(invalid_modules),
            'modules_processed': 0,
            'modules_failed': 0,
            'modules_with_trojans': 0,
            'modules_without_trojans': 0,
            'total_trojans': 0,
            'pattern_distribution': defaultdict(int),
            'module_details': [],
            'avg_trojans_per_module': 0
        }
        
        # Generate Trojans
        print(f"\n⚙️  Generating Trojans...")
        output_dir = self.processors[processor_name] / 'generated_trojans'
        output_dir.mkdir(exist_ok=True)
        
        module_results = []
        
        for i, module_file in enumerate(valid_modules, 1):
            module_result = {
                'name': module_file.stem,
                'file': module_file.name,
                'trojans': 0,
                'patterns': [],
                'status': 'pending'
            }
            
            try:
                # Progress indicator
                progress = (i / len(valid_modules)) * 100
                print(f"  [{i:3}/{len(valid_modules)}] {progress:5.1f}% - {module_file.name:<40}", end='')
                
                # Generate
                gen = TrojanGenerator(str(module_file), processor=processor_name)
                gen.parse_module()
                gen.find_candidates()
                
                if gen.candidates:
                    # Create subdirectory for this module
                    module_output = output_dir / module_file.stem
                    generated_files = gen.generate_trojans(str(module_output))
                    gen.generate_summary_report(str(module_output))
                    
                    num_trojans = len(generated_files)
                    processor_stats['total_trojans'] += num_trojans
                    processor_stats['modules_processed'] += 1
                    processor_stats['modules_with_trojans'] += 1
                    
                    # Count pattern distribution
                    for file_path in generated_files:
                        filename = Path(file_path).stem
                        # Extract pattern from filename (e.g., T1_module_DoS.sv)
                        for pattern_key, pattern_name in self.PATTERN_NAMES.items():
                            if pattern_key.upper() in filename.upper() or pattern_name.replace(' ', '') in filename:
                                processor_stats['pattern_distribution'][pattern_name] += 1
                                module_result['patterns'].append(pattern_name)
                                break
                    
                    module_result['trojans'] = num_trojans
                    module_result['status'] = 'success'
                    print(f" ✓ ({num_trojans} Trojans)")
                else:
                    processor_stats['modules_processed'] += 1
                    processor_stats['modules_without_trojans'] += 1
                    module_result['status'] = 'no_candidates'
                    print(f" ⚠️  (No candidates)")
                
            except Exception as e:
                print(f" ✗ Error: {str(e)[:40]}")
                processor_stats['modules_failed'] += 1
                module_result['status'] = 'failed'
                module_result['error'] = str(e)
            
            module_results.append(module_result)
            processor_stats['module_details'].append(module_result)
        
        # Calculate average
        if processor_stats['modules_with_trojans'] > 0:
            processor_stats['avg_trojans_per_module'] = (
                processor_stats['total_trojans'] / processor_stats['modules_with_trojans']
            )
        
        # Store processor stats
        self.global_stats['processors'][processor_name] = processor_stats
        self.global_stats['total_modules'] += processor_stats['valid_modules']
        self.global_stats['total_trojans'] += processor_stats['total_trojans']
        
        # Print processor summary
        self.print_processor_summary(processor_name, processor_stats, detailed)
    
    def print_processor_summary(self, processor_name: str, stats: dict, detailed: bool = False):
        """Print detailed summary for one processor"""
        print(f"\n{'='*80}")
        print(f"📈 {processor_name.upper()} DETAILED SUMMARY")
        print(f"{'='*80}")
        
        print(f"\n📁 Module Statistics:")
        print(f"  Total .sv files found:        {stats['total_modules']}")
        print(f"  Valid modules (parseable):    {stats['valid_modules']}")
        print(f"  Invalid (packages/interfaces): {stats['invalid_modules']}")
        print(f"  Modules with trojans:         {stats['modules_with_trojans']}")
        print(f"  Modules without candidates:   {stats['modules_without_trojans']}")
        print(f"  Modules failed:               {stats['modules_failed']}")
        
        print(f"\n🎯 Trojan Generation:")
        print(f"  Total trojans generated:      {stats['total_trojans']}")
        print(f"  Average per module (with trojans): {stats['avg_trojans_per_module']:.1f}")
        
        if stats['pattern_distribution']:
            print(f"\n📊 Pattern Distribution:")
            total_patterns = sum(stats['pattern_distribution'].values())
            for pattern_name in sorted(stats['pattern_distribution'].keys()):
                count = stats['pattern_distribution'][pattern_name]
                percentage = (count / total_patterns * 100) if total_patterns > 0 else 0
                print(f"  {pattern_name:<25} {count:4} ({percentage:5.1f}%)")
        
        # Per-module breakdown if requested
        if detailed and stats['module_details']:
            print(f"\n📋 Per-Module Breakdown:")
            print(f"  {'Module Name':<40} {'Trojans':>8} {'Patterns'}")
            print(f"  {'-'*40} {'-'*8} {'-'*30}")
            
            for module in stats['module_details']:
                if module['status'] == 'success':
                    patterns_str = ', '.join(module['patterns'][:3])
                    if len(module['patterns']) > 3:
                        patterns_str += f" +{len(module['patterns'])-3} more"
                    print(f"  {module['name']:<40} {module['trojans']:>8} {patterns_str}")
                elif module['status'] == 'no_candidates':
                    print(f"  {module['name']:<40} {'0':>8} (no candidates)")
        
        print(f"\n📂 Output Directory:")
        output_dir = self.processors[processor_name] / 'generated_trojans'
        print(f"  {output_dir}")
    
    def generate_all(self, processors: list = None, dry_run: bool = False, detailed: bool = False):
        """
        Generate Trojans for all specified processors
        
        Args:
            processors: List of processor names, or None for all
            dry_run: If True, only validate without generating
            detailed: If True, show per-module breakdown
        """
        self.global_stats['start_time'] = datetime.now()
        
        if processors is None:
            processors = ['ibex', 'cva6', 'rsd']
        
        print("\n" + "="*80)
        print("🚀 RV-TROGEN ENHANCED BATCH TROJAN GENERATION")
        print("="*80)
        print(f"Processors: {', '.join([p.upper() for p in processors])}")
        print(f"Mode: {'DRY RUN' if dry_run else 'FULL GENERATION'}")
        print(f"Detail Level: {'VERBOSE' if detailed else 'SUMMARY'}")
        print(f"Started: {self.global_stats['start_time'].strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Generate for each processor
        for processor in processors:
            self.generate_for_processor(processor, dry_run, detailed)
        
        self.global_stats['end_time'] = datetime.now()
        
        # Overall summary
        self.print_global_summary()
        
        # Generate report file
        if not dry_run:
            self.generate_report_file()
    
    def print_global_summary(self):
        """Print overall generation summary"""
        duration = (self.global_stats['end_time'] - self.global_stats['start_time']).total_seconds()
        
        print("\n" + "="*80)
        print("🎉 BATCH GENERATION COMPLETE")
        print("="*80)
        
        print(f"\n  Generation Time: {duration:.1f} seconds")
        print(f"📊 Total Modules Processed: {self.global_stats['total_modules']}")
        print(f"🎯 Total Trojans Generated: {self.global_stats['total_trojans']}")
        
        # Detailed table
        print(f"\n📈 Processor Comparison Table:")
        print(f"{'─'*80}")
        print(f"{'Processor':<12} {'Modules':>8} {'Trojans':>8} {'Avg/Module':>12} {'Success Rate':>12}")
        print(f"{'─'*80}")
        
        for proc_name in ['ibex', 'cva6', 'rsd']:
            if proc_name in self.global_stats['processors']:
                stats = self.global_stats['processors'][proc_name]
                success_rate = (stats['modules_with_trojans'] / stats['valid_modules'] * 100) if stats['valid_modules'] > 0 else 0
                print(f"{proc_name.upper():<12} "
                      f"{stats['valid_modules']:>8} "
                      f"{stats['total_trojans']:>8} "
                      f"{stats['avg_trojans_per_module']:>12.1f} "
                      f"{success_rate:>11.1f}%")
        
        print(f"{'─'*80}")
        print(f"{'TOTAL':<12} "
              f"{self.global_stats['total_modules']:>8} "
              f"{self.global_stats['total_trojans']:>8} "
              f"{self.global_stats['total_trojans']/self.global_stats['total_modules'] if self.global_stats['total_modules'] > 0 else 0:>12.1f}")
        print(f"{'─'*80}")
        
        # Pattern distribution across all processors
        print(f"\n📊 Overall Pattern Distribution:")
        all_patterns = defaultdict(int)
        for proc_stats in self.global_stats['processors'].values():
            for pattern, count in proc_stats['pattern_distribution'].items():
                all_patterns[pattern] += count
        
        total_patterns = sum(all_patterns.values())
        for pattern_name in sorted(all_patterns.keys()):
            count = all_patterns[pattern_name]
            percentage = (count / total_patterns * 100) if total_patterns > 0 else 0
            bar_length = int(percentage / 2)
            bar = '█' * bar_length
            print(f"  {pattern_name:<25} {count:4} ({percentage:5.1f}%) {bar}")
        
        print(f"\n📂 Output Locations:")
        for proc_name in self.global_stats['processors'].keys():
            output_dir = self.processors[proc_name] / 'generated_trojans'
            print(f"  {proc_name.upper():<8} {output_dir}")
        
        print(f"\n{'='*80}")
    
    def generate_report_file(self):
        """Generate detailed report file"""
        report_path = self.base_dir / 'batch_generation_report.txt'
        
        with open(report_path, 'w') as f:
            f.write("="*80 + "\n")
            f.write("RV-TROGEN BATCH GENERATION REPORT\n")
            f.write("="*80 + "\n\n")
            
            f.write(f"Generated: {self.global_stats['end_time'].strftime('%Y-%m-%d %H:%M:%S')}\n")
            duration = (self.global_stats['end_time'] - self.global_stats['start_time']).total_seconds()
            f.write(f"Duration: {duration:.1f} seconds\n\n")
            
            f.write("SUMMARY:\n")
            f.write(f"  Total Modules: {self.global_stats['total_modules']}\n")
            f.write(f"  Total Trojans: {self.global_stats['total_trojans']}\n")
            f.write(f"  Average: {self.global_stats['total_trojans']/self.global_stats['total_modules']:.1f} trojans/module\n\n")
            
            # Per-processor details
            for proc_name, stats in self.global_stats['processors'].items():
                f.write(f"\n{'='*80}\n")
                f.write(f"{proc_name.upper()} PROCESSOR\n")
                f.write(f"{'='*80}\n\n")
                
                f.write(f"Modules Statistics:\n")
                f.write(f"  Total files: {stats['total_modules']}\n")
                f.write(f"  Valid modules: {stats['valid_modules']}\n")
                f.write(f"  Modules with trojans: {stats['modules_with_trojans']}\n")
                f.write(f"  Modules without candidates: {stats['modules_without_trojans']}\n")
                f.write(f"  Failed: {stats['modules_failed']}\n\n")
                
                f.write(f"Trojan Statistics:\n")
                f.write(f"  Total trojans: {stats['total_trojans']}\n")
                f.write(f"  Average per module: {stats['avg_trojans_per_module']:.1f}\n\n")
                
                f.write(f"Pattern Distribution:\n")
                for pattern, count in sorted(stats['pattern_distribution'].items()):
                    percentage = (count / stats['total_trojans'] * 100) if stats['total_trojans'] > 0 else 0
                    f.write(f"  {pattern:<25} {count:4} ({percentage:5.1f}%)\n")
                
                f.write(f"\nModule Details:\n")
                for module in stats['module_details']:
                    if module['status'] == 'success':
                        f.write(f"  {module['name']:<40} {module['trojans']:3} trojans\n")
        
        print(f"\n📄 Detailed report saved: {report_path}")


def main():
    """Command-line interface"""
    parser = argparse.ArgumentParser(
        description='Enhanced batch Trojan generation with detailed statistics',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate for all processors (standard output)
  python scripts/batch_generate.py

  # Generate with detailed per-module breakdown
  python scripts/batch_generate.py --detailed

  # Generate for specific processor with details
  python scripts/batch_generate.py --processor ibex --detailed

  # Dry run to see what would be generated
  python scripts/batch_generate.py --dry-run

  # Multiple processors with verbose output
  python scripts/batch_generate.py --processor ibex --processor cva6 --detailed
        """
    )
    
    parser.add_argument(
        '--processor', '-p',
        action='append',
        choices=['ibex', 'cva6', 'rsd'],
        help='Processor to generate for (can specify multiple times)'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Validate modules without generating Trojans'
    )
    
    parser.add_argument(
        '--detailed', '-d',
        action='store_true',
        help='Show detailed per-module breakdown'
    )
    
    parser.add_argument(
        '--base-dir',
        default='examples',
        help='Base directory containing processor folders (default: examples)'
    )
    
    args = parser.parse_args()
    
    # Create generator
    batch_gen = EnhancedBatchGenerator(args.base_dir)
    
    # Run generation
    batch_gen.generate_all(
        processors=args.processor,
        dry_run=args.dry_run,
        detailed=args.detailed
    )


if __name__ == "__main__":
    main()