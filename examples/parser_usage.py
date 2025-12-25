#!/usr/bin/env python3
"""
RV-TroGen Parser Usage Examples
"""

from src.parser import RTLParser, SignalExtractor, ModuleClassifier

def example_1_basic_parsing():
    """Example 1: Basic module parsing"""
    print("\n" + "="*60)
    print("Example 1: Basic Parsing")
    print("="*60)
    
    # Parse a module
    parser = RTLParser('examples/ibex/original/ibex_csr.sv')
    module = parser.parse()
    
    # Print summary
    module.print_summary()
    
    # Access specific information
    print(f"Sequential: {module.is_sequential}")
    print(f"Clock: {module.clock_signal}")
    print(f"Reset: {module.reset_signal}")


def example_2_signal_filtering():
    """Example 2: Signal filtering"""
    print("\n" + "="*60)
    print("Example 2: Signal Filtering")
    print("="*60)
    
    parser = RTLParser('examples/ibex/original/ibex_csr.sv')
    module = parser.parse()
    
    # Get all signals
    all_signals = module.get_all_signals()
    
    # Filter vector signals
    vectors = [s for s in all_signals if s.is_vector]
    print(f"\nVector signals ({len(vectors)}):")
    for sig in vectors[:5]:
        print(f"  {sig.name} [{sig.width}-bit]")
    
    # Filter by name pattern
    csr_signals = [s for s in all_signals if 'csr' in s.name.lower()]
    print(f"\nCSR-related signals ({len(csr_signals)}):")
    for sig in csr_signals[:5]:
        print(f"  {sig.name}")


def example_3_direct_extraction():
    """Example 3: Direct signal extraction"""
    print("\n" + "="*60)
    print("Example 3: Direct Signal Extraction")
    print("="*60)
    
    # Read file
    from pathlib import Path
    content = Path('examples/ibex/original/ibex_csr.sv').read_text()
    
    # Extract signals directly
    extractor = SignalExtractor(content)
    inputs = extractor.extract_inputs()
    
    print(f"\nExtracted {len(inputs)} inputs:")
    for sig in inputs[:5]:
        print(f"  {sig}")


def example_4_classification():
    """Example 4: Module classification"""
    print("\n" + "="*60)
    print("Example 4: Module Classification")
    print("="*60)
    
    from pathlib import Path
    content = Path('examples/ibex/original/ibex_csr.sv').read_text()
    
    # Classify module
    classifier = ModuleClassifier(content, [])
    report = classifier.get_classification_report()
    
    print("\nClassification Report:")
    for key, value in report.items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    # Run all examples
    example_1_basic_parsing()
    example_2_signal_filtering()
    example_3_direct_extraction()
    example_4_classification()
    
    print("\n" + "="*60)
    print("All examples complete!")
    print("="*60 + "\n")