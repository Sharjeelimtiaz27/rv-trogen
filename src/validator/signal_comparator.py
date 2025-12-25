"""
Stub SignalComparator so imports succeed during tests.
"""
from typing import Any, Dict, List, Optional

class SignalComparator:
    """
    Minimal comparator API:
      - compare(ref_signals, test_signals) -> dict
    """
    def __init__(self, tolerance: Optional[float] = None) -> None:
        self.tolerance = tolerance

    def compare(self, ref_signals: Dict[str, Any], test_signals: Dict[str, Any]) -> Dict[str, Any]:
        # trivial comparison: return counts
        return {
            "ref_count": len(ref_signals) if ref_signals else 0,
            "test_count": len(test_signals) if test_signals else 0,
            "match": ref_signals == test_signals
        }

__all__ = ["SignalComparator"]
