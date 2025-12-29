#!/usr/bin/env python3
"""
RV-TroGen Installation Script
Installs the package and shows welcome banner
Usage: python install.py
"""
import subprocess
import sys
from pathlib import Path


def print_banner():
    """Print fancy installation banner"""
    banner = """
╔════════════════════════════════════════════════════════════════════════════════╗
║                                                                                ║
║   ██████╗ ██╗   ██╗        ████████╗ ██████╗    ██████╗   ██████╗ ███████╗ ███╗   ██╗ ║
║   ██╔══██╗██║   ██║        ╚══██╔══╝ ██╔══██╗ ██╔═══██╗ ██╔════╝ ██╔════╝████╗  ██║ ║
║   ██████╔╝██║   ██║ █████╗   ██║     ██████╔╝ ██║   ██║  ██║  ███╗█████╗   ██╔██╗ ██║ ║
║   ██╔══██╗╚██╗ ██╔╝╚════╝   ██║     ██╔══██╗ ██║   ██║  ██║   ██║██╔══╝   ██║╚██╗██║ ║
║   ██║  ██║ ╚████╔╝             ██║     ██║  ██║  ╚██████╔╝╚██████╔╝███████╗██║ ╚████║ ║
║   ╚═╝  ╚═╝  ╚═══╝               ╚═╝     ╚═╝  ╚═╝  ╚═════╝   ╚═════╝ ╚══════╝╚═╝  ╚═══╝  ║
║              🔧 RV-TroGen Installation Successful! 🎉                          ║
║                                                                                ║
║       RTL-Level Hardware Trojan Generation for RISC-V                         ║
║                                                                                ║
╠════════════════════════════════════════════════════════════════════════════════╣
║                                                                                ║
║  📦 Version:    1.0.0                                                          ║
║  👤 Author:     Sharjeel Imtiaz                                                ║
║  🎓 University: Tallinn University of Technology (TalTech)                     ║
║  📧 Email:      sharjeel.imtiaz@taltech.ee                                     ║
║  🔗 GitHub:     github.com/sharjeelimtiaz27/rv-trogen                          ║
║                                                                                ║
╠════════════════════════════════════════════════════════════════════════════════╣
║                                                                                ║
║  ⚡ Quick Start:                                                               ║
║                                                                                ║
║    Parse:     python -m src.parser.rtl_parser <module.sv>                     ║
║    Generate:  python scripts/generate_trojans.py <module.sv>                  ║
║    Test:      python -m pytest tests/ -v                                      ║
║    Docs:      docs/QUICK_START.md                                             ║
║                                                                                ║
║  📚 Documentation: docs/                                                       ║
║  🐛 Report Issues: github.com/sharjeelimtiaz27/rv-trogen/issues               ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝
"""
    print(banner)


def main():
    """Run pip install and show banner"""
    try:
        print("\n🔧 Installing RV-TroGen...\n")
        
        # Run pip install in editable mode
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "-e", "."],
            cwd=Path(__file__).parent,
            check=False
        )
        
        if result.returncode == 0:
            print("\n")  # Extra spacing
            print_banner()
            return 0
        else:
            print("\n❌ Installation failed! Check the error messages above.")
            return 1
            
    except Exception as e:
        print(f"\n❌ Error during installation: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())