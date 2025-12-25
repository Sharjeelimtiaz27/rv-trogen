"""
Minimal compatibility shim for tests.

Provides a lightweight CombinationalGenerator class so imports like:
    from src.generator.combinational_gen import CombinationalGenerator
succeed during pytest collection.

Replace with the real implementation when available.
"""
from typing import Any, Dict, Optional

class CombinationalGenerator:
    """Stub used only to satisfy imports during tests."""

    def __init__(self, config: Optional[Dict[str, Any]] = None) -> None:
        self.config = config or {}

    def generate(self, module_text: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Stub generate method.
        Real code should produce generator outputs; here we return a minimal dict.
        """
        return {
            "module_name": None,
            "notes": "stub - no generation performed",
            "config": self.config
        }

__all__ = ["CombinationalGenerator"]
