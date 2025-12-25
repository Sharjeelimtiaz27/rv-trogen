"""
Trust-Hub Pattern Library - tolerant initializer

This file will attempt to import known pattern classes, but won't fail
if some modules are missing. Missing pattern modules are ignored so test
and import-time errors don't block development of other parts (like parser).
"""

__all__ = [
    "PatternLibrary",
    "get_pattern",
    "get_all_patterns",
    # pattern class names (only include if actually importable)
]

# import pattern_library which should exist (if not, make it per earlier instructions)
from .pattern_library import PatternLibrary, get_pattern, get_all_patterns

# try to import optional pattern classes; if missing, skip them
_optional_patterns = [
    ("dos_pattern", "DoSPattern"),
    ("leak_pattern", "LeakPattern"),
    ("privilege_pattern", "PrivilegePattern"),
    ("integrity_pattern", "IntegrityPattern"),
    ("availability_pattern", "AvailabilityPattern"),
    ("covert_pattern", "CovertPattern"),
]

for module_name, class_name in _optional_patterns:
    try:
        mod = __import__(f"src.patterns.{module_name}", fromlist=[class_name])
        cls = getattr(mod, class_name)
        globals()[class_name] = cls
        __all__.append(class_name)
    except Exception:
        # missing module or class — ignore for now
        continue
