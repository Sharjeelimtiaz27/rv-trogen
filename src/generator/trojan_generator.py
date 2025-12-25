"""
Minimal compatibility shim for tests.

Provides a small TrojanGenerator class so imports like:
    from src.generator.trojan_generator import TrojanGenerator
succeed during test collection.

Replace this with the real implementation when available.
"""
from typing import Any

class TrojanGenerator:
    """Tiny stub of the real TrojanGenerator used only for test-import compatibility."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        # store args/kwargs in case tests or other code introspect the instance
        self._init_args = args
        self._init_kwargs = kwargs

    def generate(self, *args: Any, **kwargs: Any) -> Any:
        """
        Stub method. Real implementation should generate trojan artifacts.
        This returns None to indicate no-op in test environments.
        """
        return None

__all__ = ["TrojanGenerator"]
