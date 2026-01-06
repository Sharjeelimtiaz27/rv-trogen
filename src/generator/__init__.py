"""
Hardware Trojan Generator Module

Automatically generates hardware Trojans for RISC-V processors based on
Trust-Hub patterns and RISC-V security literature.
"""

from .trojan_generator import TrojanGenerator
from .sequential_gen import SequentialGenerator
from .combinational_gen import CombinationalGenerator

__all__ = [
    'TrojanGenerator',
    'SequentialGenerator', 
    'CombinationalGenerator'
]

__version__ = '1.0.0'