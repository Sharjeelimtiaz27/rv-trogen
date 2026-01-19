#!/usr/bin/env python3
"""
Main Trojan Generator - FIXED VERSION
STRICT signal matching - only generates if REAL signals found
Skips patterns with no matching signals
"""

import sys
from pathlib import Path
from typing import List, Dict

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.parser import RTLParser
from src.patterns import get_all_patterns
from src.generator.sequential_gen import SequentialGenerator
from src.generator.combinational_gen import CombinationalGenerator


class TrojanGenerator:
    """
    Main Trojan Generator - STRICT MODE
    
    Only generates trojans when REAL matching signals are found
    NO fallbacks to hardcoded signal names
    """
    
    def __init__(self, rtl_file: str):
        """
        Initialize generator
        
        Args:
            rtl_file: Path to Verilog/SystemVerilog file
        """
        self.rtl_file = Path(rtl_file)
        self.module = None
        self.candidates = []
        
    def parse_module(self):
        """Parse the RTL module"""
        print(f"📄 Parsing: {self.rtl_file.name}")
        
        parser = RTLParser(str(self.rtl_file))
        self.module = parser.parse()
        
        print(f"   Module: {self.module.name}")
        print(f"   Type: {'Sequential' if self.module.is_sequential else 'Combinational'}")
        print(f"   Signals: {len(self.module.get_all_signals())}")
    
    def find_candidates(self):
        """
        Find Trojan candidates by matching signals to patterns
        
        STRICT MODE: Only adds candidate if BOTH trigger AND payload signals found
        """
        print(f"\n🎯 Finding Trojan candidates (STRICT MODE)...")
        
        patterns = get_all_patterns()
        all_signals = self.module.get_all_signals()
        
        for pattern in patterns:
            # Match trigger signals
            trigger_matches = []
            for signal in all_signals:
                signal_name_lower = signal.name.lower()
                for keyword in pattern.trigger_keywords:
                    if keyword in signal_name_lower:
                        trigger_matches.append(signal)
                        break
            
            # Match payload signals
            payload_matches = []
            for signal in all_signals:
                signal_name_lower = signal.name.lower()
                for keyword in pattern.payload_keywords:
                    if keyword in signal_name_lower:
                        payload_matches.append(signal)
                        break
            
            # STRICT: Only add if we have BOTH trigger AND payload signals
            if trigger_matches and payload_matches:
                # Calculate confidence score
                confidence = 0.0
                
                # Signal matching
                confidence += 0.4  # Has triggers
                confidence += 0.4  # Has payloads
                
                # Module type compatibility
                if pattern.preferred_module_type == 'both':
                    confidence += 0.2
                elif pattern.preferred_module_type == 'sequential' and self.module.is_sequential:
                    confidence += 0.2
                elif pattern.preferred_module_type == 'combinational' and not self.module.is_sequential:
                    confidence += 0.2
                
                self.candidates.append({
                    'pattern': pattern,
                    'confidence': confidence,
                    'trigger_signals': trigger_matches,
                    'payload_signals': payload_matches
                })
            else:
                # SKIP - Not enough signals
                print(f"   ⊘ Skipped {pattern.name}: ", end="")
                if not trigger_matches:
                    print(f"No trigger signals (need: {', '.join(pattern.trigger_keywords[:3])}...)")
                elif not payload_matches:
                    print(f"No payload signals (need: {', '.join(pattern.payload_keywords[:3])}...)")
        
        # Sort by confidence
        self.candidates.sort(key=lambda x: x['confidence'], reverse=True)
        
        print(f"   ✓ Found {len(self.candidates)} valid candidates")
        
        # Print summary
        for i, candidate in enumerate(self.candidates, 1):
            print(f"\n   [{i}] {candidate['pattern'].name}: {candidate['pattern'].category}")
            print(f"       Confidence: {candidate['confidence']:.2f}")
            print(f"       Triggers: {len(candidate['trigger_signals'])} signals → {[s.name for s in candidate['trigger_signals'][:3]]}")
            print(f"       Payloads: {len(candidate['payload_signals'])} signals → {[s.name for s in candidate['payload_signals'][:3]]}")
    
    def generate_trojans(self, output_dir: str = "generated_trojans"):
        """
        Generate Trojan code for all candidates
        
        Args:
            output_dir: Directory to save generated Trojans
        """
        if not self.candidates:
            print("\n⚠️  No candidates found. Cannot generate Trojans.")
            print("    This module may not have security-critical signals.")
            print("    Or signal names don't match pattern keywords.")
            return
        
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        print(f"\n⚙️  Generating Trojan code...")
        print(f"   Output: {output_path}/")
        
        # Choose appropriate generator based on module type
        if self.module.is_sequential:
            generator = SequentialGenerator(self.module)
            gen_type = "Sequential"
        else:
            generator = CombinationalGenerator(self.module)
            gen_type = "Combinational"
        
        print(f"   Generator: {gen_type}")
        
        generated_files = []
        
        for i, candidate in enumerate(self.candidates, 1):
            trojan_id = f"T{i}"
            pattern_name = candidate['pattern'].name
            
            try:
                # Generate Trojan code
                trojan_code = generator.generate(
                    pattern_name=pattern_name,
                    trojan_id=trojan_id,
                    trigger_signals=candidate['trigger_signals'],
                    payload_signals=candidate['payload_signals']
                )
                
                # Create filename
                filename = f"{trojan_id}_{self.module.name}_{pattern_name}.sv"
                filepath = output_path / filename
                
                # Write to file
                with open(filepath, 'w') as f:
                    f.write(trojan_code.code)
                
                generated_files.append(filepath)
                
                print(f"\n   ✓ {trojan_id}: {pattern_name} → {filename}")
                print(f"      {trojan_code.description}")
                
            except ValueError as e:
                # This should rarely happen now with STRICT matching
                print(f"\n   ✗ {trojan_id}: {pattern_name} - Skipped: {e}")
            except Exception as e:
                print(f"\n   ✗ {trojan_id}: {pattern_name} - Error: {e}")
        
        print(f"\n✅ Complete! Generated {len(generated_files)} Trojans")
        print(f"📁 Output directory: {output_path.absolute()}")
        
        return generated_files
    
    def generate_summary_report(self, output_dir: str = "generated_trojans"):
        """Generate a summary report of all Trojans"""
        output_path = Path(output_dir)
        report_file = output_path / f"{self.module.name}_trojan_summary.md"
        
        with open(report_file, 'w') as f:
            f.write(f"# Trojan Generation Summary\n\n")
            f.write(f"**Module:** {self.module.name}\n")
            f.write(f"**File:** {self.rtl_file.name}\n")
            f.write(f"**Type:** {'Sequential' if self.module.is_sequential else 'Combinational'}\n")
            f.write(f"**Total Candidates:** {len(self.candidates)}\n\n")
            
            f.write(f"---\n\n")
            f.write(f"## Generated Trojans\n\n")
            
            for i, candidate in enumerate(self.candidates, 1):
                pattern = candidate['pattern']
                f.write(f"### T{i}: {pattern.name} - {pattern.category}\n\n")
                f.write(f"**Trust-Hub Status:** {pattern.trust_hub_status}\n")
                f.write(f"**Severity:** {pattern.severity}\n")
                f.write(f"**Confidence:** {candidate['confidence']:.2f}\n")
                f.write(f"**Description:** {pattern.description}\n\n")
                
                f.write(f"**Trigger Signals ({len(candidate['trigger_signals'])}):**\n")
                for sig in candidate['trigger_signals'][:5]:  # First 5
                    f.write(f"- {sig.name}\n")
                if len(candidate['trigger_signals']) > 5:
                    f.write(f"- ... and {len(candidate['trigger_signals']) - 5} more\n")
                f.write(f"\n")
                
                f.write(f"**Payload Signals ({len(candidate['payload_signals'])}):**\n")
                for sig in candidate['payload_signals'][:5]:  # First 5
                    f.write(f"- {sig.name}\n")
                if len(candidate['payload_signals']) > 5:
                    f.write(f"- ... and {len(candidate['payload_signals']) - 5} more\n")
                f.write(f"\n")
                
                f.write(f"**Generated File:** T{i}_{self.module.name}_{pattern.name}.sv\n\n")
                f.write(f"---\n\n")
        
        print(f"📄 Summary report: {report_file}")


def main():
    """Command-line interface"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Generate hardware Trojans for RTL modules (STRICT MODE)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate Trojans for a module
  python trojan_generator.py examples/ibex/original/ibex_cs_registers.sv

  # Custom output directory
  python trojan_generator.py module.sv --output my_trojans/

  # Generate without summary report
  python trojan_generator.py module.sv --no-report
        """
    )
    
    parser.add_argument('rtl_file', help='Path to RTL file (.sv or .v)')
    parser.add_argument('--output', '-o', default='generated_trojans',
                       help='Output directory (default: generated_trojans)')
    parser.add_argument('--no-report', action='store_true',
                       help='Skip generating summary report')
    
    args = parser.parse_args()
    
    # Check file exists
    if not Path(args.rtl_file).exists():
        print(f"❌ Error: File not found: {args.rtl_file}")
        sys.exit(1)
    
    # Generate Trojans
    print("="*60)
    print("TROJAN GENERATOR (STRICT MODE)")
    print("="*60)
    
    gen = TrojanGenerator(args.rtl_file)
    
    # Step 1: Parse
    gen.parse_module()
    
    # Step 2: Find candidates (STRICT)
    gen.find_candidates()
    
    # Step 3: Generate
    if gen.candidates:
        gen.generate_trojans(args.output)
        
        # Step 4: Summary report
        if not args.no_report:
            gen.generate_summary_report(args.output)
    else:
        print("\n⚠️  No Trojan candidates found for this module.")
        print("    Possible reasons:")
        print("    - Signal names don't match pattern keywords")
        print("    - Module doesn't have security-critical signals")
        print("    - Try different module (e.g., CSR, PMP, controller)")
    
    print("\n" + "="*60)


if __name__ == "__main__":
    main()