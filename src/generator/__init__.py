"""
Trojan Code Generator
Generates SystemVerilog Trojan code based on Trust-Hub patterns
"""

from .sequential_gen import SequentialGenerator, SequentialTrojanCode
from .combinational_gen import CombinationalGenerator, CombinationalTrojanCode

__all__ = [
    'SequentialGenerator',
    'CombinationalGenerator',
    'SequentialTrojanCode',
    'CombinationalTrojanCode'
]