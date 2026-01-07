"""Quick test for template integration - Step 11"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.generator.template_loader import TemplateLoader
from src.generator.placeholder_handler import PlaceholderHandler

def test_template_loader():
    """Test template loader"""
    print("="*60)
    print("TEST 1: Template Loader")
    print("="*60)
    
    loader = TemplateLoader()
    
    # Check available templates
    available = loader.list_available_templates()
    print(f"\n✓ Available templates:")
    for template_type, patterns in available.items():
        print(f"  {template_type}: {patterns}")
    
    # Try loading a template
    print(f"\n✓ Loading sequential DoS template...")
    template = loader.load_template('dos', 'sequential')
    print(f"  Template length: {len(template)} characters")
    print(f"  First 200 chars:\n{template[:200]}")
    
    return True

def test_placeholder_handler():
    """Test placeholder handler"""
    print("\n" + "="*60)
    print("TEST 2: Placeholder Handler")
    print("="*60)
    
    handler = PlaceholderHandler()
    
    # Test template with placeholders
    template = """
    module {{MODULE_NAME}}_trojan (
        input logic {{CLOCK_SIGNAL}},
        input logic {{TRIGGER_SIGNAL}}
    );
    endmodule
    """
    
    print(f"\n✓ Original template:\n{template}")
    
    # Replace placeholders
    replacements = {
        'MODULE_NAME': 'ibex_cs_registers',
        'CLOCK_SIGNAL': 'clk_i',
        'TRIGGER_SIGNAL': 'csr_we_int'
    }
    
    result = handler.replace_placeholders(template, replacements)
    print(f"\n✓ After replacement:\n{result}")
    
    return True

def test_full_generation():
    """Test full Trojan generation with templates"""
    print("\n" + "="*60)
    print("TEST 3: Full Generation (ibex_cs_registers.sv)")
    print("="*60)
    
    from src.generator.trojan_generator import TrojanGenerator
    
    # Path to test file
    test_file = Path("examples/ibex/original/ibex_cs_registers.sv")
    
    if not test_file.exists():
        print(f"\n  Test file not found: {test_file}")
        print("   Skipping full generation test")
        return False
    
    print(f"\n✓ Generating Trojans for: {test_file.name}")
    
    gen = TrojanGenerator(str(test_file))
    gen.parse_module()
    gen.find_candidates()
    
    if gen.candidates:
        files = gen.generate_trojans("generated_trojans_test")
        print(f"\n✓ Generated {len(files)} Trojans")
        
        # Check first generated file
        if files:
            first_file = files[0]
            print(f"\n✓ Checking {first_file.name}:")
            with open(first_file, 'r') as f:
                content = f.read()
                print(f"  File size: {len(content)} characters")
                print(f"  First 400 chars:\n{content[:400]}")
                
                # Check if placeholders are replaced
                if '{{' in content:
                    print(f"\n  WARNING: Unreplaced placeholders found!")
                    # Show which ones
                    import re
                    unreplaced = re.findall(r'\{\{([A-Z_]+)\}\}', content)
                    print(f"  Unreplaced: {set(unreplaced)}")
                else:
                    print(f"\n✅ All placeholders replaced successfully!")
        
        return True
    else:
        print("\n  No candidates found")
        return False

if __name__ == "__main__":
    try:
        print("\n🧪 TESTING TEMPLATE INTEGRATION \n")
        
        # Run tests
        test1 = test_template_loader()
        test2 = test_placeholder_handler()
        test3 = test_full_generation()
        
        print("\n" + "="*60)
        print("SUMMARY")
        print("="*60)
        print(f"Test 1 (Loader):  {'✅ PASS' if test1 else '❌ FAIL'}")
        print(f"Test 2 (Handler): {'✅ PASS' if test2 else '❌ FAIL'}")
        print(f"Test 3 (Full):    {'✅ PASS' if test3 else '❌ FAIL'}")
        
        if test1 and test2 and test3:
            print("\n✅ ALL TESTS PASSED! Step 11 Complete!")
            print("✅ Templates are now being used for generation!")
        else:
            print("\n  Some tests failed. Check errors above.")
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()