"""
Minimal compatibility shim for tests.

Provides a tiny VCDAnalyzer class so imports like:
    from src.validator.vcd_analyzer import VCDAnalyzer
succeed during pytest collection.

This stub performs no real VCD parsing — it only exposes the minimal API
other modules/tests might import. Replace with the real analyzer later.
"""
from typing import Any, Dict, Optional

class VCDAnalyzer:
    """
    Stubbed VCD analyzer.

    Public surface:
      - __init__(path: Optional[str] = None)
      - load(path: str) -> bool
      - get_signals() -> Dict[str, Any]
      - summary() -> Dict[str, Any]
    """

    def __init__(self, path: Optional[str] = None) -> None:
        self.path = path
        self._signals = {}
        self._loaded = False

    def load(self, path: str) -> bool:
        """
        Pretend to load a VCD file; record the path and mark as loaded.
        Returns True on "success".
        """
        self.path = path
        self._loaded = True
        self._signals = {}
        return True

    def get_signals(self) -> Dict[str, Any]:
        """
        Return a minimal signals dict. Real implementation should return
        structured info parsed from the VCD file.
        """
        return self._signals

    def summary(self) -> Dict[str, Any]:
        """
        Return a small summary dict so code that introspects analyzer output
        can proceed during tests.
        """
        return {
            "path": self.path,
            "loaded": self._loaded,
            "signal_count": len(self._signals)
        }

__all__ = ["VCDAnalyzer"]
