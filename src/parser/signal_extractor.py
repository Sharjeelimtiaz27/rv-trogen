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
    
    # Keywords that should never be signal names
    RESERVED_KEYWORDS = {
        'logic', 'reg', 'wire', 'input', 'output', 'inout',
        'parameter', 'localparam', 'genvar', 'integer',
        'signed', 'unsigned', 'bit', 'byte', 'shortint',
        'int', 'longint', 'time', 'real', 'realtime'
    }
    
    def __init__(self, content: str):
        self.content = content
        # Remove comments for cleaner parsing
        self.content = self._remove_comments(content)
        
    def _remove_comments(self, content: str) -> str:
        """Remove single-line and multi-line comments"""
        # Remove single-line comments
        content = re.sub(r'//.*?$', '', content, flags=re.MULTILINE)
        # Remove multi-line comments
        content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
        return content
    
    def extract_inputs(self) -> List[Signal]:
        """Extract input ports"""
        return self._extract_ports('input')
    
    def extract_outputs(self) -> List[Signal]:
        """Extract output ports"""
        return self._extract_ports('output')
    
    def _extract_ports(self, port_type: str) -> List[Signal]:
        """Extract ports (input/output) handling multi-line declarations"""
        signals = []
        
        # Pattern to match port declarations including multi-line
        # Matches: input [logic/wire] [width] name1, name2, ...
        pattern = rf'{port_type}\s+(?:logic\s+|wire\s+|reg\s+)?(?:\[(\d+):(\d+)\]\s+)?([^;]+);'
        
        for match in re.finditer(pattern, self.content, re.MULTILINE | re.DOTALL):
            # Extract width if present
            if match.group(1) and match.group(2):
                width = int(match.group(1)) - int(match.group(2)) + 1
                is_vector = True
            else:
                width = 1
                is_vector = False
            
            # Extract all signal names (handling comma-separated lists)
            names_str = match.group(3)
            # Split by comma and clean up
            names = [n.strip() for n in re.split(r'[,\s]+', names_str) if n.strip()]
            
            for name in names:
                # Skip if it's a type keyword or empty
                if not name or name in self.RESERVED_KEYWORDS:
                    continue
                
                # Skip if it looks like a type keyword (contains brackets or keywords)
                if any(keyword in name for keyword in ['[', ']', 'logic', 'wire', 'reg']):
                    continue
                
                signal = Signal(
                    name=name,
                    signal_type=port_type,
                    width=width,
                    is_vector=is_vector
                )
                
                signals.append(signal)
        
        return signals
    
    def extract_internals(self, exclude_names: List[str] = None) -> List[Signal]:
        """Extract internal signals (logic, wire, reg)"""
        if exclude_names is None:
            exclude_names = []
        
        patterns = [
            (r'logic\s+(?:\[(\d+):(\d+)\]\s+)?([^;,]+);', 'logic'),
            (r'wire\s+(?:\[(\d+):(\d+)\]\s+)?([^;,]+);', 'wire'),
            (r'reg\s+(?:\[(\d+):(\d+)\]\s+)?([^;,]+);', 'reg')
        ]
        
        all_internals = []
        found_names = set()
        
        for pattern, sig_type in patterns:
            for match in re.finditer(pattern, self.content):
                # Extract width if present
                if match.group(1) and match.group(2):
                    width = int(match.group(1)) - int(match.group(2)) + 1
                    is_vector = True
                else:
                    width = 1
                    is_vector = False
                
                # Extract all signal names (handling comma-separated lists)
                names_str = match.group(3)
                names = [n.strip() for n in re.split(r'[,\s]+', names_str) if n.strip()]
                
                for name in names:
                    # Skip if already found, in exclude list, or is a keyword
                    if (name in found_names or 
                        name in exclude_names or 
                        name in self.RESERVED_KEYWORDS or
                        not name):
                        continue
                    
                    # Skip if it looks like it contains brackets or keywords
                    if any(keyword in name for keyword in ['[', ']', '(', ')']):
                        continue
                    
                    found_names.add(name)
                    
                    signal = Signal(
                        name=name,
                        signal_type=sig_type,
                        width=width,
                        is_vector=is_vector
                    )
                    
                    all_internals.append(signal)
        
        return all_internals
    
    def _extract_signals(self, pattern: str, sig_type: str) -> List[Signal]:
        """Generic signal extraction (deprecated, use _extract_ports)"""
        signals = []
        
        for match in re.finditer(pattern, self.content):
            if match.group(1):  # Has bit range
                width = int(match.group(1)) - int(match.group(2)) + 1
                is_vector = True
            else:
                width = 1
                is_vector = False
            
            name = match.group(3)
            
            # Skip reserved keywords
            if name in self.RESERVED_KEYWORDS:
                continue
            
            signal = Signal(
                name=name,
                signal_type=sig_type,
                width=width,
                is_vector=is_vector
            )
            
            signals.append(signal)
        
        return signals