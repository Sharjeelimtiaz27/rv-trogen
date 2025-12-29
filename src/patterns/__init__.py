"""
Trust-Hub Pattern Library
6 Hardware Trojan patterns based on Trust-Hub taxonomy
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