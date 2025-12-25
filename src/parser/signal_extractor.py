#!/usr/bin/env python3
"""
Signal Extractor
Extracts signals (inputs, outputs, internals) from RTL files
"""

import re
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Signal:
    """Represents a signal in the module"""
    name: str
    signal_type: str  # 'input', 'output', 'logic', 'wire', 'reg'
    width: int
    is_vector: bool
    
    def __repr__(self):
        if self.is_vector:
            return f"{self.signal_type} [{self.width-1}:0] {self.name}"
        else:
            return f"{self.signal_type} {self.name}"


class SignalExtractor:
    """Extracts signals from RTL content"""
    
    def __init__(self, content: str):
        self.content = content
        
    def extract_inputs(self) -> List[Signal]:
        """Extract input ports"""
        pattern = r'input\s+(?:logic\s+|wire\s+)?(?:\[(\d+):(\d+)\]\s+)?(\w+)'
        return self._extract_signals(pattern, 'input')
    
    def extract_outputs(self) -> List[Signal]:
        """Extract output ports"""
        pattern = r'output\s+(?:logic\s+|wire\s+)?(?:\[(\d+):(\d+)\]\s+)?(\w+)'
        return self._extract_signals(pattern, 'output')
    
    def extract_internals(self, exclude_names: List[str] = None) -> List[Signal]:
        """Extract internal signals (logic, wire, reg)"""
        if exclude_names is None:
            exclude_names = []
        
        patterns = [
            (r'logic\s+(?:\[(\d+):(\d+)\]\s+)?(\w+)', 'logic'),
            (r'wire\s+(?:\[(\d+):(\d+)\]\s+)?(\w+)', 'wire'),
            (r'reg\s+(?:\[(\d+):(\d+)\]\s+)?(\w+)', 'reg')
        ]
        
        all_internals = []
        found_names = set()
        
        for pattern, sig_type in patterns:
            for match in re.finditer(pattern, self.content):
                name = match.group(3)
                
                # Skip if already found or in exclude list
                if name in found_names or name in exclude_names:
                    continue
                
                found_names.add(name)
                
                if match.group(1):  # Has bit range
                    width = int(match.group(1)) - int(match.group(2)) + 1
                    is_vector = True
                else:
                    width = 1
                    is_vector = False
                
                signal = Signal(
                    name=name,
                    signal_type=sig_type,
                    width=width,
                    is_vector=is_vector
                )
                
                all_internals.append(signal)
        
        return all_internals
    
    def _extract_signals(self, pattern: str, sig_type: str) -> List[Signal]:
        """Generic signal extraction"""
        signals = []
        
        for match in re.finditer(pattern, self.content):
            if match.group(1):  # Has bit range
                width = int(match.group(1)) - int(match.group(2)) + 1
                is_vector = True
            else:
                width = 1
                is_vector = False
            
            name = match.group(3)
            
            signal = Signal(
                name=name,
                signal_type=sig_type,
                width=width,
                is_vector=is_vector
            )
            
            signals.append(signal)
        
        return signals