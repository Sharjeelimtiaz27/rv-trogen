#!/usr/bin/env python3
"""
Module Classifier
Classifies modules as Sequential or Combinational
"""

import re
from typing import List
from .signal_extractor import Signal


class ModuleClassifier:
    """Classifies module type and detects clock/reset"""
    
    def __init__(self, content: str, signals: List[Signal]):
        self.content = content
        self.signals = signals
        
    def is_sequential(self) -> bool:
        """Determine if module is sequential"""
        
        # Check for always_ff blocks
        if 'always_ff' in self.content:
            return True
        
        # Check for @(posedge clk) patterns
        if re.search(r'@\s*\(posedge', self.content):
            return True
        
        # Check if has clock signal
        if self.has_clock():
            return True
        
        # Otherwise combinational
        return False
    
    def has_clock(self) -> bool:
        """Check if module has clock signal"""
        for signal in self.signals:
            if 'clk' in signal.name.lower():
                return True
        return False
    
    def has_reset(self) -> bool:
        """Check if module has reset signal"""
        for signal in self.signals:
            name_lower = signal.name.lower()
            if 'rst' in name_lower or 'reset' in name_lower:
                return True
        return False
    
    def get_clock_signal(self) -> str:
        """Get clock signal name"""
        for signal in self.signals:
            if 'clk' in signal.name.lower():
                return signal.name
        return None
    
    def get_reset_signal(self) -> str:
        """Get reset signal name"""
        for signal in self.signals:
            name_lower = signal.name.lower()
            if 'rst' in name_lower or 'reset' in name_lower:
                return signal.name
        return None
    
    def get_classification_report(self) -> dict:
        """Get full classification report"""
        return {
            'is_sequential': self.is_sequential(),
            'has_clock': self.has_clock(),
            'has_reset': self.has_reset(),
            'clock_signal': self.get_clock_signal(),
            'reset_signal': self.get_reset_signal(),
            'type': 'Sequential' if self.is_sequential() else 'Combinational'
        }