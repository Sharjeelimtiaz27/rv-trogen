#!/usr/bin/env python3
"""
Pattern Library - Unified Access to All Trust-Hub Patterns
"""

from typing import List, Dict, Optional
from dataclasses import dataclass

from .dos_pattern import DoSPattern, dos_pattern
from .leak_pattern import LeakPattern, leak_pattern
from .privilege_pattern import PrivilegePattern, privilege_pattern
from .integrity_pattern import IntegrityPattern, integrity_pattern
from .availability_pattern import AvailabilityPattern, availability_pattern
from .covert_pattern import CovertPattern, covert_pattern


class PatternLibrary:
    """
    Unified access to all Trust-Hub Trojan patterns
    
    Usage:
        library = PatternLibrary()
        all_patterns = library.get_all_patterns()
        dos = library.get_pattern('DoS')
    """
    
    def __init__(self):
        """Initialize pattern library"""
        self.patterns = {
            'DoS': dos_pattern,
            'Leak': leak_pattern,
            'Privilege': privilege_pattern,
            'Integrity': integrity_pattern,
            'Availability': availability_pattern,
            'Covert': covert_pattern
        }
    
    def get_pattern(self, name: str):
        """
        Get pattern by name
        
        Args:
            name: Pattern name (DoS, Leak, Privilege, Integrity, Availability, Covert)
        
        Returns:
            Pattern object or None
        """
        return self.patterns.get(name)
    
    def get_all_patterns(self) -> List:
        """Get all patterns as list"""
        return list(self.patterns.values())
    
    def get_pattern_names(self) -> List[str]:
        """Get all pattern names"""
        return list(self.patterns.keys())
    
    def get_patterns_by_severity(self, severity: str) -> List:
        """
        Get patterns by severity level
        
        Args:
            severity: 'Critical', 'High', 'Medium', 'Low'
        
        Returns:
            List of matching patterns
        """
        return [p for p in self.patterns.values() if p.severity == severity]
    
    def get_patterns_by_module_type(self, module_type: str) -> List:
        """
        Get patterns suitable for module type
        
        Args:
            module_type: 'sequential', 'combinational', or 'both'
        
        Returns:
            List of suitable patterns
        """
        suitable = []
        for pattern in self.patterns.values():
            if pattern.preferred_module_type == 'both':
                suitable.append(pattern)
            elif pattern.preferred_module_type == module_type:
                suitable.append(pattern)
        return suitable
    
    def print_summary(self):
        """Print summary of all patterns"""
        print("\n" + "="*80)
        print("TRUST-HUB PATTERN LIBRARY")
        print("="*80)
        print(f"{'Pattern':<15} {'Category':<25} {'Severity':<10} {'Source':<20}")
        print("-"*80)
        
        for name, pattern in self.patterns.items():
            print(f"{name:<15} {pattern.category:<25} {pattern.severity:<10} {pattern.trust_hub_source:<20}")
        
        print("="*80)
        print(f"Total Patterns: {len(self.patterns)}")
        print("="*80 + "\n")


# Create default library instance
pattern_library = PatternLibrary()


def get_pattern(name: str):
    """Convenience function to get pattern by name"""
    return pattern_library.get_pattern(name)


def get_all_patterns() -> List:
    """Convenience function to get all patterns"""
    return pattern_library.get_all_patterns()


def get_pattern_library() -> PatternLibrary:
    """Get pattern library instance"""
    return pattern_library


if __name__ == "__main__":
    # Demo
    library = PatternLibrary()
    library.print_summary()
    
    print("\nCritical Patterns:")
    for p in library.get_patterns_by_severity('Critical'):
        print(f"  - {p.name}: {p.description}")
    
    print("\nSequential Patterns:")
    for p in library.get_patterns_by_module_type('sequential'):
        print(f"  - {p.name}")