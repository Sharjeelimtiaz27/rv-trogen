"""
Pattern Library - Hardware Trojan Patterns with Citations
6 patterns: 3 from Trust-Hub RTL benchmarks, 3 from literature
"""

from .pattern_library import (
    PatternLibrary,
    get_pattern,
    get_all_patterns,
    get_pattern_library,
    pattern_library
)

from .dos_pattern import DoSPattern, dos_pattern
from .leak_pattern import LeakPattern, leak_pattern
from .privilege_pattern import PrivilegePattern, privilege_pattern
from .integrity_pattern import IntegrityPattern, integrity_pattern
from .availability_pattern import AvailabilityPattern, availability_pattern
from .covert_pattern import CovertPattern, covert_pattern

__version__ = "1.0.0"
__author__ = "Sharjeel Imtiaz"
__email__ = "sharjeel.imtiaz@taltech.ee"

__all__ = [
    # Library access
    'PatternLibrary',
    'get_pattern',
    'get_all_patterns',
    'get_pattern_library',
    'pattern_library',
    
    # Individual patterns
    'DoSPattern',
    'LeakPattern',
    'PrivilegePattern',
    'IntegrityPattern',
    'AvailabilityPattern',
    'CovertPattern',
    
    # Pattern instances
    'dos_pattern',
    'leak_pattern',
    'privilege_pattern',
    'integrity_pattern',
    'availability_pattern',
    'covert_pattern'
]

# Pattern summary for quick reference
PATTERN_SUMMARY = """
RV-TroGen Pattern Library v1.0.0
================================

✓ Trust-Hub Verified RTL Benchmarks (3):
  - DoS (Denial of Service): AES-T1800, T1900, T500, BasicRSA-T200
  - Leak (Information Leakage): AES-T600, T1400, T800
  - Integrity (Data Corruption): AES-T2500, T2600, T2700, T2800

✓ Trust-Hub Category Adaptations (1):
  - Availability (Performance Degradation): Category exists, RTL adaptation

✓ Trust-Hub Concept Extensions (1):
  - Covert (Timing Channels): Extends Leak Information to timing domain

✓ RISC-V Specific Patterns (1):
  - Privilege (Escalation): Not in Trust-Hub (processor-specific)

Total: 6 patterns covering all major trojan categories
"""


def print_summary():
    """Print pattern library summary"""
    print(PATTERN_SUMMARY)
    pattern_library.print_summary()


def print_citations():
    """Print detailed citation report"""
    pattern_library.print_citation_report()


def get_bibtex():
    """Get BibTeX entries for all patterns"""
    return pattern_library.get_bibtex_entries()