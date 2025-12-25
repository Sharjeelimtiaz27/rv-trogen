"""
Minimal compatibility shim for tests.

Provides a lightweight QuestaSimulator class so imports like:
    from src.validator.simulator import QuestaSimulator
succeed during pytest collection.

This is a NO-OP stub — replace with the real simulator integration later.
"""
from typing import Any, Dict, Optional

class QuestaSimulator:
    """
    Stub class that mirrors the minimal interface other modules may expect.

    Real implementation typically invokes Questa/ModelSim or another simulator.
    This stub provides:
      - an __init__ that accepts config
      - a run or simulate method that accepts a testbench/module and returns a result dict
    """
    def __init__(self, config: Optional[Dict[str, Any]] = None) -> None:
        self.config = config or {}
        self.last_run = None

    def simulate(self, top_module: str, tb_file: Optional[str] = None, timeout: int = 5) -> Dict[str, Any]:
        """
        Run a no-op simulation and return a minimal result dict so tests/imports that
        introspect simulator outputs won't break.
        """
        self.last_run = {
            "top_module": top_module,
            "tb_file": tb_file,
            "timeout": timeout,
            "status": "stubbed",
            "notes": "No simulation performed — QuestaSimulator stub in tests."
        }
        return self.last_run

    # Backwards-compatible alias if code expects `run` instead of `simulate`
    def run(self, *args, **kwargs) -> Dict[str, Any]:
        return self.simulate(*args, **kwargs)

__all__ = ["QuestaSimulator"]
