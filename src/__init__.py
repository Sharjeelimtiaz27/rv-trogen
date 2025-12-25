"""
RV-TroGen: Automated Hardware Trojan Generation for RISC-V

Systematic framework for generating Trust-Hub taxonomy Trojans
in RISC-V processors for security assertion validation.
"""

__version__ = "1.0.0"
__author__ = "Sharjeel Imtiaz"
__email__ = "sharjeelimtiazprof@gmail.com,sharjeel.imtiaz@taltech.ee"
__title__ = "RV-TroGen"
__description__ = "RTL-Level Hardware Trojan Generation for RISC-V Processors"

from . import parser
from . import patterns
from . import generator

__all__ = ['parser', 'patterns', 'generator']

