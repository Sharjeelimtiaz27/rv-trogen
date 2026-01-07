"""
Hardware Trojan Generator Module

Automatically generates hardware Trojans for RISC-V processors based on
Trust-Hub patterns and RISC-V security literature.
"""

from .trojan_generator import TrojanGenerator
from .sequential_gen import SequentialGenerator
from .combinational_gen import CombinationalGenerator
from .template_loader import TemplateLoader
from .placeholder_handler import PlaceholderHandler

__all__ = [
    'TrojanGenerator',
    'SequentialGenerator', 
    'CombinationalGenerator',
    'TemplateLoader',
    'PlaceholderHandler',
]

__version__ = '1.0.0'