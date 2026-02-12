#!/usr/bin/env python3
"""
Detailed Diagnostic - Why Only 2 Patterns Generate
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path.cwd()))

print("="*80)
print("DETAILED PATTERN GENERATION DIAGNOSTIC")
print("="*80)

# Test template loading for all 6 patterns
print("\n1. TESTING TEMPLATE LOADING:")
print("-" * 80)

from src.generator.template_loader import TemplateLoader

loader = TemplateLoader()

patterns = ['dos', 'leak', 'privilege', 'integrity', 'availability', 'covert']
types = ['sequential', 'combinational']

for pattern in patterns:
    for type in types:
        try:
            template = loader.load_template(pattern, type)
            print(f"✅ {pattern:15} {type:15} - Loaded ({len(template)} chars)")
        except FileNotFoundError as e:
            print(f"❌ {pattern:15} {type:15} - NOT FOUND")
        except Exception as e:
            print(f"❌ {pattern:15} {type:15} - ERROR: {str(e)[:40]}")

# Test actual generation for each pattern
print("\n2. TESTING ACTUAL GENERATION (ibex_alu):")
print("-" * 80)

from src.generator.trojan_generator import TrojanGenerator
from src.generator.sequential_gen import SequentialGenerator
from src.generator.combinational_gen import CombinationalGenerator

test_file = "examples/ibex/original/ibex_alu.sv"
if not Path(test_file).exists():
    print(f"❌ Test file not found: {test_file}")
else:
    gen = TrojanGenerator(test_file)
    gen.parse_module()
    gen.find_candidates()
    
    print(f"\nModule: {gen.module.name}")
    print(f"Type: {'Sequential' if gen.module.is_sequential else 'Combinational'}")
    print(f"Candidates: {len(gen.candidates)}")
    
    # Try to generate each candidate
    if gen.module.is_sequential:
        generator = SequentialGenerator(gen.module)
    else:
        generator = CombinationalGenerator(gen.module)
    
    print(f"\n{'='*80}")
    print("Attempting generation for each candidate:")
    print(f"{'='*80}\n")
    
    for i, candidate in enumerate(gen.candidates, 1):
        pattern_name = candidate['pattern'].name
        print(f"[{i}] Pattern: {pattern_name}")
        
        try:
            trojan_code = generator.generate(
                pattern_name=pattern_name,
                trojan_id=f"TEST{i}",
                trigger_signals=candidate['trigger_signals'],
                payload_signals=candidate['payload_signals']
            )
            
            print(f"    ✅ SUCCESS - Generated {len(trojan_code.code)} characters")
            print(f"    Description: {trojan_code.description}")
            
            # Check if placeholders are still there
            if '{{' in trojan_code.code:
                print(f"    ⚠️  WARNING: Placeholders still in code!")
                # Count placeholders
                import re
                placeholders = re.findall(r'\{\{(\w+)\}\}', trojan_code.code)
                print(f"    Unreplaced: {set(placeholders)}")
            
        except FileNotFoundError as e:
            print(f"    ❌ FAILED: Template not found")
            print(f"    Error: {str(e)}")
        except Exception as e:
            print(f"    ❌ FAILED: {str(e)[:60]}")
            import traceback
            traceback.print_exc()
        
        print()

# Check template directory structure
print("\n3. CHECKING DIRECTORY STRUCTURE:")
print("-" * 80)

import os

base_dir = Path("templates/trojan_templates")
if base_dir.exists():
    print(f"✅ Base directory exists: {base_dir}")
    
    for type_dir in ['sequential', 'combinational']:
        type_path = base_dir / type_dir
        if type_path.exists():
            print(f"\n  📁 {type_dir}/")
            templates = list(type_path.glob("*_template.sv"))
            for template in templates:
                size = template.stat().st_size
                print(f"     ✅ {template.name:<30} ({size} bytes)")
        else:
            print(f"\n  ❌ {type_dir}/ NOT FOUND")
else:
    print(f"❌ Base directory NOT FOUND: {base_dir}")

print("\n" + "="*80)
print("SUMMARY:")
print("="*80)

print("""
If you see:
- ✅ All templates load successfully
- ✅ All patterns generate successfully  
- BUT still only get 2 patterns in batch generation

Then the issue is in the batch generation script or signal matching logic.

If you see:
- ❌ Some templates missing
- ❌ Some patterns fail to generate

Then those are the specific issues to fix.
""")

print("="*80)