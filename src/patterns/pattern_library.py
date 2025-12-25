# src/patterns/pattern_library.py
"""
Pattern library singleton and helpers.
Provides:
- PatternLibrary (registry)
- get_pattern(name)
- get_all_patterns()
This is a resilient, minimal implementation safe to import while other
pattern modules are still under development.
"""

from typing import Any, Dict, List

class PatternLibrary:
    """Simple in-memory registry for pattern classes / objects."""

    def __init__(self) -> None:
        self._registry: Dict[str, Any] = {}
        # attempt auto-registration of common pattern modules (tolerant)
        self._auto_register_known()

    def register(self, name: str, thing: Any) -> None:
        """Register a class or instance under name (overwrites)."""
        self._registry[name] = thing

    def get(self, name: str, default: Any = None) -> Any:
        return self._registry.get(name, default)

    def names(self) -> List[str]:
        return sorted(self._registry.keys())

    def _auto_register_known(self) -> None:
        known = {
            "dos": ("src.patterns.dos_pattern", "DoSPattern"),
            "leak": ("src.patterns.leak_pattern", "LeakPattern"),
            "privilege": ("src.patterns.privilege_pattern", "PrivilegePattern"),
            "integrity": ("src.patterns.integrity_pattern", "IntegrityPattern"),
            "availability": ("src.patterns.availability_pattern", "AvailabilityPattern"),
            "covert": ("src.patterns.covert_pattern", "CovertPattern"),
        }
        for key, (modpath, clsname) in known.items():
            try:
                mod = __import__(modpath, fromlist=[clsname])
                cls = getattr(mod, clsname, None)
                if cls is not None:
                    self.register(key, cls)
            except Exception:
                # Ignore missing modules or import errors (they can be added later)
                continue

# module-level singleton
_default_lib = PatternLibrary()

def get_pattern(name: str):
    """Return the registered pattern class/object or None."""
    return _default_lib.get(name)

def get_all_patterns() -> List[str]:
    """Return sorted list of registered pattern names."""
    return _default_lib.names()
