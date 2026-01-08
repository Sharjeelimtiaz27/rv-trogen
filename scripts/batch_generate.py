#!/usr/bin/env python3
"""
Batch Trojan Generation Script
Generates Trojans for all modules across all processors

Usage:
    python scripts/batch_generate.py                    # All processors
    python scripts/batch_generate.py --processor ibex   # Single processor
    python scripts/batch_generate.py --dry-run          # Test without generating
"""

import sys
import argparse
from pathlib import Path
from datetime import datetime
import time

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.generator.trojan_generator import TrojanGenerator


class BatchTrojanGenerator:
    """Batch generator for multiple processors"""
    
    def __init__(self, base_dir: str = "examples"):
        """
        Initialize batch generator
        
        Args:
            base_dir: Base directory containing processor folders
        """
        self.base_dir = Path(base_dir)
        self.processors = {
            'ibex': self.base_dir / 'ibex',
            'cva6': self.base_dir / 'cva6',
            'rsd': self.base_dir / 'rsd'
        }
        
        self.stats = {
            'total_modules': 0,
            'successful': 0,
            'failed': 0,
            'total_trojans': 0,
            'start_time': None,
            'end_time': None,
            'by_processor': {}
        }
    
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
    
    def generate_for_processor(self, processor_name: str, dry_run: bool = False):
        """
        Generate Trojans for all modules of one processor
        
        Args:
            processor_name: Name of processor
            dry_run: If True, only count modules without generating
        """
        print(f"\n{'='*70}")
        print(f"📊 PROCESSOR: {processor_name.upper()}")
        print(f"{'='*70}")
        
        # Find modules
        modules = self.find_modules(processor_name)
        
        if not modules:
            print(f"❌ No modules found for {processor_name}")
            return
        
        print(f"Found {len(modules)} .sv files")
        
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
        
        if dry_run:
            print(f"\n📋 DRY RUN: Would generate {len(valid_modules) * 6} Trojans")
            return
        
        # Generate Trojans
        print(f"\n⚙️  Generating Trojans...")
        output_dir = self.processors[processor_name] / 'generated_trojans'
        output_dir.mkdir(exist_ok=True)
        
        processor_stats = {
            'modules_processed': 0,
            'modules_failed': 0,
            'trojans_generated': 0
        }
        
        for i, module_file in enumerate(valid_modules, 1):
            try:
                # Progress indicator
                progress = (i / len(valid_modules)) * 100
                print(f"  [{i}/{len(valid_modules)}] {progress:5.1f}% - {module_file.name}", end='')
                
                # Generate
                gen = TrojanGenerator(str(module_file))
                gen.parse_module()
                gen.find_candidates()
                
                if gen.candidates:
                    # Create subdirectory for this module
                    module_output = output_dir / module_file.stem
                    generated_files = gen.generate_trojans(str(module_output))
                    gen.generate_summary_report(str(module_output))
                    
                    processor_stats['trojans_generated'] += len(generated_files)
                    processor_stats['modules_processed'] += 1
                    print(f" ✓ ({len(generated_files)} Trojans)")
                else:
                    print(f" ⚠️  (No candidates)")
                    processor_stats['modules_processed'] += 1
                
            except Exception as e:
                print(f" ✗ Error: {str(e)[:40]}")
                processor_stats['modules_failed'] += 1
        
        # Processor summary
        print(f"\n{'='*70}")
        print(f"📈 {processor_name.upper()} SUMMARY:")
        print(f"{'='*70}")
        print(f"  Modules processed: {processor_stats['modules_processed']}")
        print(f"  Modules failed:    {processor_stats['modules_failed']}")
        print(f"  Trojans generated: {processor_stats['trojans_generated']}")
        
        self.stats['by_processor'][processor_name] = processor_stats
        self.stats['successful'] += processor_stats['modules_processed']
        self.stats['failed'] += processor_stats['modules_failed']
        self.stats['total_trojans'] += processor_stats['trojans_generated']
    
    def generate_all(self, processors: list = None, dry_run: bool = False):
        """
        Generate Trojans for all specified processors
        
        Args:
            processors: List of processor names, or None for all
            dry_run: If True, only validate without generating
        """
        self.stats['start_time'] = datetime.now()
        
        if processors is None:
            processors = ['ibex', 'cva6', 'rsd']
        
        print("\n" + "="*70)
        print("🚀 RV-TROGEN BATCH TROJAN GENERATION")
        print("="*70)
        print(f"Processors: {', '.join(processors)}")
        print(f"Mode: {'DRY RUN' if dry_run else 'FULL GENERATION'}")
        print(f"Started: {self.stats['start_time'].strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Generate for each processor
        for processor in processors:
            self.generate_for_processor(processor, dry_run)
        
        self.stats['end_time'] = datetime.now()
        
        # Overall summary
        self.print_summary()
    
    def print_summary(self):
        """Print overall generation summary"""
        duration = (self.stats['end_time'] - self.stats['start_time']).total_seconds()
        
        print("\n" + "="*70)
        print("🎉 BATCH GENERATION COMPLETE")
        print("="*70)
        
        print(f"\n⏱️  Time: {duration:.1f} seconds ({duration/60:.1f} minutes)")
        print(f"✅ Successful: {self.stats['successful']} modules")
        print(f"❌ Failed: {self.stats['failed']} modules")
        print(f"🎯 Total Trojans: {self.stats['total_trojans']}")
        
        print(f"\n📊 By Processor:")
        for proc, stats in self.stats['by_processor'].items():
            print(f"  {proc.upper():8} - {stats['modules_processed']:3} modules, "
                  f"{stats['trojans_generated']:4} Trojans")
        
        print(f"\n📁 Output locations:")
        for proc in self.stats['by_processor'].keys():
            output_dir = self.processors[proc] / 'generated_trojans'
            print(f"  {proc}: {output_dir}")
        
        print(f"\n{'='*70}")


def main():
    """Command-line interface"""
    parser = argparse.ArgumentParser(
        description='Batch generate hardware Trojans for RISC-V processors',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate for all processors
  python scripts/batch_generate.py

  # Generate for specific processor
  python scripts/batch_generate.py --processor ibex

  # Dry run (validate only)
  python scripts/batch_generate.py --dry-run

  # Multiple processors
  python scripts/batch_generate.py --processor ibex --processor cva6
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
        '--base-dir',
        default='examples',
        help='Base directory containing processor folders (default: examples)'
    )
    
    args = parser.parse_args()
    
    # Create generator
    batch_gen = BatchTrojanGenerator(args.base_dir)
    
    # Run generation
    batch_gen.generate_all(
        processors=args.processor,
        dry_run=args.dry_run
    )


if __name__ == "__main__":
    main()