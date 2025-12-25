#!/usr/bin/env python3
"""
RTL Parser
Main parser orchestrator that uses SignalExtractor and ModuleClassifier
"""

import re
from pathlib import Path
from dataclasses import dataclass, field
from typing import List

from .signal_extractor import Signal, SignalExtractor
from .module_classifier import ModuleClassifier


@dataclass
class Module:
    """Represents a parsed module"""
    name: str
    file_path: Path
    inputs: List[Signal] = field(default_factory=list)
    outputs: List[Signal] = field(default_factory=list)
    internals: List[Signal] = field(default_factory=list)
    has_clock: bool = False
    has_reset: bool = False
    is_sequential: bool = False
    clock_signal: str = None
    reset_signal: str = None
    
    def get_all_signals(self) -> List[Signal]:
        """Return all signals"""
        return self.inputs + self.outputs + self.internals
    
    def print_summary(self):
        """Print module summary"""
        print(f"\n{'='*60}")
        print(f"Module: {self.name}")
        print(f"File: {self.file_path.name}")
        print(f"{'='*60}")
        print(f"Inputs:    {len(self.inputs)}")
        print(f"Outputs:   {len(self.outputs)}")
        print(f"Internals: {len(self.internals)}")
        print(f"Has Clock: {self.has_clock}")
        print(f"Has Reset: {self.has_reset}")
        print(f"Type:      {'Sequential' if self.is_sequential else 'Combinational'}")
        if self.clock_signal:
            print(f"Clock:     {self.clock_signal}")
        if self.reset_signal:
            print(f"Reset:     {self.reset_signal}")
        print(f"{'='*60}\n")


class RTLParser:
    """Main RTL Parser"""
    
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.content = self._read_file()
        self.module = None
        
    def _read_file(self) -> str:
        """Read RTL file"""
        try:
            return self.file_path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            # Try with different encoding
            return self.file_path.read_text(encoding='latin-1')
    
    def parse(self) -> Module:
        """Main parsing function"""
        
        # Extract module name
        module_name = self._extract_module_name()
        if not module_name:
            raise Exception("Could not find module declaration")
        
        # Create module object
        self.module = Module(
            name=module_name,
            file_path=self.file_path
        )
        
        # Extract signals
        self._extract_signals()
        
        # Classify module
        self._classify_module()
        
        return self.module
    
    def _extract_module_name(self) -> str:
        """Extract module name from file"""
        pattern = r'module\s+(\w+)'
        match = re.search(pattern, self.content)
        return match.group(1) if match else None
    
    def _extract_signals(self):
        """Extract all signals using SignalExtractor"""
        extractor = SignalExtractor(self.content)
        
        # Extract inputs
        self.module.inputs = extractor.extract_inputs()
        
        # Extract outputs
        self.module.outputs = extractor.extract_outputs()
        
        # Extract internals (exclude inputs/outputs by name)
        exclude_names = [s.name for s in self.module.inputs + self.module.outputs]
        self.module.internals = extractor.extract_internals(exclude_names)
    
    def _classify_module(self):
        """Classify module type"""
        all_signals = self.module.get_all_signals()
        classifier = ModuleClassifier(self.content, all_signals)
        
        # Get classification report
        report = classifier.get_classification_report()
        
        # Update module attributes
        self.module.is_sequential = report['is_sequential']
        self.module.has_clock = report['has_clock']
        self.module.has_reset = report['has_reset']
        self.module.clock_signal = report['clock_signal']
        self.module.reset_signal = report['reset_signal']


def main():
    """Command-line interface"""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python rtl_parser.py <verilog_file.sv>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    print(f"\n🔍 Parsing: {file_path}")
    
    try:
        parser = RTLParser(file_path)
        module = parser.parse()
        
        # Print summary
        module.print_summary()
        
        # Print inputs
        print("📥 INPUTS:")
        for sig in module.inputs:
            print(f"  {sig}")
        
        # Print outputs
        print("\n📤 OUTPUTS:")
        for sig in module.outputs:
            print(f"  {sig}")
        
        # Print internals (first 10)
        print(f"\n🔧 INTERNAL SIGNALS: (showing first 10 of {len(module.internals)})")
        for sig in module.internals[:10]:
            print(f"  {sig}")
        
        if len(module.internals) > 10:
            print(f"  ... and {len(module.internals) - 10} more")
        
        print("\n✅ Parsing complete!\n")
        
    except Exception as e:
        print(f"\n❌ Error: {e}\n")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()