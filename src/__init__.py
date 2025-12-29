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


def print_banner():
    """Print fancy installation banner"""
    banner = """

╔════════════════════════════════════════════════════════════════════════════════╗
║                                                                          										 ║
║   ██████╗ ██╗   ██╗        ████████╗ ██████╗    ██████╗   ██████╗ ███████╗ ███╗   ██╗ ║
║   ██╔══██╗██║   ██║        ╚══██╔══╝ ██╔══██╗ ██╔═══██╗ ██╔════╝ ██╔════╝████╗  ██║ ║
║   ██████╔╝██║   ██║ █████╗   ██║     ██████╔╝ ██║   ██║  ██║  ███╗█████╗   ██╔██╗ ██║ ║
║   ██╔══██╗╚██╗ ██╔╝╚════╝   ██║     ██╔══██╗ ██║   ██║  ██║   ██║██╔══╝   ██║╚██╗██║ ║
║   ██║  ██║ ╚████╔╝             ██║     ██║  ██║  ╚██████╔╝╚██████╔╝███████╗██║ ╚████║ ║
║   ╚═╝  ╚═╝  ╚═══╝               ╚═╝     ╚═╝  ╚═╝  ╚═════╝   ╚═════╝ ╚══════╝╚═╝  ╚═══╝  ║
║              					🔧 RV-TroGen Installation Successful! 🎉             						   ║
║                                                                   												║
║       					RTL-Level Hardware Trojan Generation for RISC-V            								║
║                                                                   												║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                   												║
║  📦 Version:    1.0.0                                            										   ║
║  👤 Author:     Sharjeel Imtiaz                                   										║
║  🎓 University: Tallinn University of Technology (TalTech)        										║
║  📧 Email:      sharjeel.imtiaz@taltech.ee                        										║
║  🔗 GitHub:     github.com/sharjeelimtiaz27/rv-trogen             										║
║                                                                   												║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                   												║
║  ⚡ Quick Start:                                                  												║
║                                                                   												║
║    Parse:     python -m src.parser.rtl_parser <module.sv>        												║
║    Generate:  python scripts/generate_trojans.py <module.sv>     												║
║    Test:      python -m pytest tests/ -v                          												║
║    Docs:      docs/QUICK_START.md                                 												║
║                                                                   												║
║  📚 Documentation: docs/                                          									   ║
║  🐛 Report Issues: github.com/sharjeelimtiaz27/rv-trogen/issues  										   ║
║                                                                   												║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""
    print(banner)