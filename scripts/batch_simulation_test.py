#!/usr/bin/env python3
"""
Batch Simulation Tester
Tests multiple generated trojans for compilation and simulation success
Validates that trojans work as expected
"""

import subprocess
import sys
from pathlib import Path
from datetime import datetime
import json

class BatchSimulationTester:
    """Test multiple trojans for compilation success"""
    
    def __init__(self):
        self.results = {
            'tested': 0,
            'compilation_success': 0,
            'compilation_failed': 0,
            'details': []
        }
        
    def test_trojan_compilation(self, module_path: Path, pattern: str = "DoS"):
        """Test if a trojan compiles successfully"""
        
        module_name = module_path.stem
        print(f"\n{'='*70}")
        print(f"Testing: {module_name} - {pattern} Pattern")
        print(f"{'='*70}")
        
        result = {
            'module': module_name,
            'pattern': pattern,
            'module_path': str(module_path),
            'timestamp': datetime.now().isoformat(),
            'preparation': None,
            'compilation': None,
            'status': 'UNKNOWN'
        }
        
        try:
            # Step 1: Prepare simulation
            print("\n[1/2] Preparing simulation files...")
            prep_cmd = ['python', 'scripts/prepare_simulation.py', str(module_path)]
            prep_result = subprocess.run(
                prep_cmd,
                capture_output=True,
                text=True,
                timeout=60
            )
            
            if prep_result.returncode != 0:
                result['preparation'] = {
                    'status': 'FAILED',
                    'returncode': prep_result.returncode,
                    'stdout': prep_result.stdout,
                    'stderr': prep_result.stderr
                }
                result['status'] = 'PREP_FAILED'
                self.results['compilation_failed'] += 1
                print("   ✗ Preparation FAILED")
                return result
            
            result['preparation'] = {
                'status': 'SUCCESS',
                'returncode': 0
            }
            print("   ✓ Preparation SUCCESS")
            
            # Check if trojaned file was created
            trojaned_file = Path(f'examples/ibex/trojaned_rtl/{module_name}_trojan.sv')
            testbench_file = Path(f'testbenches/ibex/tb_{module_name}_trojan.sv')
            
            if not trojaned_file.exists():
                result['status'] = 'NO_TROJAN_FILE'
                self.results['compilation_failed'] += 1
                print(f"   ✗ Trojaned file not found: {trojaned_file}")
                return result
                
            if not testbench_file.exists():
                result['status'] = 'NO_TESTBENCH'
                self.results['compilation_failed'] += 1
                print(f"   ✗ Testbench not found: {testbench_file}")
                return result
            
            # Step 2: Test compilation (if vlog available)
            print("\n[2/2] Testing compilation...")
            
            # Check if vlog is available
            vlog_check = subprocess.run(
                ['where', 'vlog'] if sys.platform == 'win32' else ['which', 'vlog'],
                capture_output=True,
                text=True
            )
            
            if vlog_check.returncode != 0:
                result['compilation'] = {
                    'status': 'SKIPPED',
                    'reason': 'vlog not found in PATH'
                }
                result['status'] = 'COMPILATION_SKIPPED'
                print("   ⊘ Compilation SKIPPED (vlog not available)")
                print("   ℹ  Run manually: vlog +acc file.sv testbench.sv")
                return result
            
            # Try to compile
            compile_cmd = [
                'vlog',
                '+acc',
                str(trojaned_file),
                str(testbench_file)
            ]
            
            compile_result = subprocess.run(
                compile_cmd,
                capture_output=True,
                text=True,
                timeout=120
            )
            
            # Parse compilation output
            stdout = compile_result.stdout
            stderr = compile_result.stderr
            
            # Check for errors
            has_errors = 'Errors:' in stdout or 'Error:' in stdout or 'ERROR' in stdout
            error_count = 0
            warning_count = 0
            
            # Extract error/warning counts
            if 'Errors:' in stdout:
                import re
                error_match = re.search(r'Errors:\s*(\d+)', stdout)
                warning_match = re.search(r'Warnings:\s*(\d+)', stdout)
                if error_match:
                    error_count = int(error_match.group(1))
                if warning_match:
                    warning_count = int(warning_match.group(1))
            
            result['compilation'] = {
                'status': 'SUCCESS' if error_count == 0 else 'FAILED',
                'returncode': compile_result.returncode,
                'errors': error_count,
                'warnings': warning_count,
                'stdout': stdout,
                'stderr': stderr
            }
            
            if error_count == 0:
                result['status'] = 'SUCCESS'
                self.results['compilation_success'] += 1
                print(f"   ✓ Compilation SUCCESS (Errors: {error_count}, Warnings: {warning_count})")
            else:
                result['status'] = 'COMPILATION_FAILED'
                self.results['compilation_failed'] += 1
                print(f"   ✗ Compilation FAILED (Errors: {error_count}, Warnings: {warning_count})")
            
        except subprocess.TimeoutExpired:
            result['status'] = 'TIMEOUT'
            self.results['compilation_failed'] += 1
            print("   ✗ TIMEOUT")
            
        except Exception as e:
            result['status'] = 'ERROR'
            result['error'] = str(e)
            self.results['compilation_failed'] += 1
            print(f"   ✗ ERROR: {e}")
        
        finally:
            self.results['tested'] += 1
            self.results['details'].append(result)
        
        return result
    
    def test_multiple_modules(self, modules: list, pattern: str = "DoS"):
        """Test multiple modules"""
        
        print("\n" + "="*70)
        print("BATCH SIMULATION TESTING")
        print("="*70)
        print(f"Testing {len(modules)} modules")
        print(f"Pattern: {pattern}")
        print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        for i, module_path in enumerate(modules, 1):
            print(f"\n[{i}/{len(modules)}] {module_path.name}")
            self.test_trojan_compilation(module_path, pattern)
        
        # Print summary
        self.print_summary()
        
        # Save results
        self.save_results()
    
    def print_summary(self):
        """Print test summary"""
        
        print("\n" + "="*70)
        print("TEST SUMMARY")
        print("="*70)
        print(f"Total Tested:          {self.results['tested']}")
        print(f"Compilation Success:   {self.results['compilation_success']}")
        print(f"Compilation Failed:    {self.results['compilation_failed']}")
        
        if self.results['tested'] > 0:
            success_rate = (self.results['compilation_success'] / self.results['tested']) * 100
            print(f"Success Rate:          {success_rate:.1f}%")
        
        print("\n" + "="*70)
        print("DETAILED RESULTS")
        print("="*70)
        
        for result in self.results['details']:
            status_icon = {
                'SUCCESS': '✓',
                'PREP_FAILED': '✗',
                'COMPILATION_FAILED': '✗',
                'COMPILATION_SKIPPED': '⊘',
                'NO_TROJAN_FILE': '✗',
                'NO_TESTBENCH': '✗',
                'TIMEOUT': '✗',
                'ERROR': '✗',
                'UNKNOWN': '?'
            }.get(result['status'], '?')
            
            print(f"{status_icon} {result['module']:<30} {result['status']}")
            
            if result.get('compilation'):
                comp = result['compilation']
                if comp['status'] == 'SUCCESS':
                    print(f"   Errors: {comp.get('errors', 0)}, Warnings: {comp.get('warnings', 0)}")
    
    def save_results(self, filename: str = 'simulation_test_results.json'):
        """Save results to JSON file"""
        
        output_dir = Path('simulation_results')
        output_dir.mkdir(exist_ok=True)
        
        output_file = output_dir / filename
        
        with open(output_file, 'w') as f:
            json.dump(self.results, f, indent=2)
        
        print(f"\n📁 Results saved to: {output_file}")


def main():
    """Main execution"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Batch test trojan compilation',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('--modules', nargs='+', help='Specific modules to test')
    parser.add_argument('--quick', action='store_true', help='Quick test (5 modules)')
    parser.add_argument('--pattern', default='DoS', help='Pattern to test (default: DoS)')
    
    args = parser.parse_args()
    
    # Default test set
    test_modules = [
        'examples/ibex/original/ibex_csr.sv',
        'examples/ibex/original/ibex_alu.sv',
        'examples/ibex/original/ibex_controller.sv',
        'examples/ibex/original/ibex_decoder.sv',
        'examples/ibex/original/ibex_register_file_ff.sv',
        'examples/ibex/original/ibex_multdiv_fast.sv',
        'examples/ibex/original/ibex_load_store_unit.sv'
    ]
    
    if args.quick:
        test_modules = test_modules[:5]  # First 5 modules
    
    if args.modules:
        test_modules = args.modules
    
    # Convert to Path objects
    modules = [Path(m) for m in test_modules]
    
    # Verify modules exist
    valid_modules = []
    for module in modules:
        if module.exists():
            valid_modules.append(module)
        else:
            print(f"⚠️  Module not found: {module}")
    
    if not valid_modules:
        print("❌ No valid modules found!")
        return 1
    
    # Run tests
    tester = BatchSimulationTester()
    tester.test_multiple_modules(valid_modules, args.pattern)
    
    # Return 0 if all successful, 1 otherwise
    return 0 if tester.results['compilation_failed'] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
