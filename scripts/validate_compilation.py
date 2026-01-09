#!/usr/bin/env python3
"""
Validate that all generated Trojans compile successfully
Quick compilation check without full simulation
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.validator import RemoteSimulator

def main():
    print("="*70)
    print("🔧 RV-TROGEN COMPILATION VALIDATION")
    print("="*70)
    print()
    
    # Load config
    try:
        from config.simulation_config import SIMULATION_MODE, REMOTE_SIMULATOR
    except ImportError:
        print("❌ Configuration not found!")
        print("   Run: python scripts/setup_simulation.py")
        return
    
    if SIMULATION_MODE == 'local':
        print("⚠️  Local simulation not yet implemented")
        print("   Using remote simulation...")
    
    if not REMOTE_SIMULATOR['enabled']:
        print("❌ Remote simulator not configured!")
        return
    
    # Initialize simulator
    sim = RemoteSimulator()
    
    # Connect
    if not sim.connect():
        print("❌ Could not connect to server")
        return
    
    print()
    print("📂 Finding generated Trojans...")
    print()
    
    # Find all generated Trojans
    trojans_dir = Path('examples')
    trojan_files = []
    
    for processor in ['ibex', 'cva6', 'rsd']:
        gen_dir = trojans_dir / processor / 'generated_trojans'
        if gen_dir.exists():
            files = list(gen_dir.rglob('*.sv'))
            # Exclude summary files
            files = [f for f in files if not f.name.endswith('_summary.sv')]
            trojan_files.extend(files)
    
    print(f"Found {len(trojan_files)} Trojan files")
    print()
    
    if len(trojan_files) == 0:
        print("❌ No Trojan files found!")
        print("   Run: python scripts/batch_generate.py")
        return
    
    # Test first 10 as quick validation
    print("🧪 Testing compilation (first 10 files)...")
    print()
    
    test_files = trojan_files[:10]
    
    passed = 0
    failed = 0
    errors = []
    
    remote_work_dir = f"{REMOTE_SIMULATOR['remote_work_dir']}/validation_test"
    
    for trojan_file in test_files:
        # Transfer file
        if not sim.transfer_file(str(trojan_file), remote_work_dir):
            failed += 1
            errors.append((trojan_file.name, "Transfer failed"))
            continue
        
        # Compile
        success, output = sim.compile_module(str(trojan_file), remote_work_dir)
        
        if success:
            passed += 1
        else:
            failed += 1
            errors.append((trojan_file.name, output[:100]))
    
    # Summary
    print()
    print("="*70)
    print("📊 COMPILATION VALIDATION RESULTS")
    print("="*70)
    print()
    print(f"✅ Passed: {passed}/{len(test_files)}")
    print(f"❌ Failed: {failed}/{len(test_files)}")
    print()
    
    if failed > 0:
        print("❌ Failed files:")
        for filename, error in errors:
            print(f"  - {filename}")
            print(f"    {error}")
            print()
    
    # Cleanup
    sim.cleanup(remote_work_dir)
    
    if failed == 0:
        print("🎉 All tested Trojans compile successfully!")
        print()
        print("Next step:")
        print("  python scripts/run_simulations.py")
    else:
        print("⚠️  Some Trojans failed to compile")
        print("   Check the errors above")


if __name__ == "__main__":
    main()