#!/usr/bin/env python3
"""
Parse and Rank RISC-V Modules by Security Criticality
Ranks modules based on security-relevant signals and keywords
"""

import sys
import argparse
from pathlib import Path
from typing import List, Dict, Tuple

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.parser.rtl_parser import RTLParser


# Security keywords for ranking
SECURITY_KEYWORDS = {
    # Privilege and mode
    'privilege': 10, 'priv': 10, 'mode': 8,
    'csr': 10, 'mstatus': 10, 'mtvec': 8, 'mepc': 8, 'mcause': 8,
    
    # Memory protection
    'pmp': 10, 'pma': 10, 'protection': 8, 'access': 5, 'permission': 8,
    
    # Control and state
    'control': 6, 'state': 6, 'status': 7, 'enable': 4,
    
    # Security-specific
    'secure': 10, 'trust': 10, 'crypto': 10, 'key': 10, 'debug': 7,
    
    # Critical operations
    'write': 4, 'read': 3, 'execute': 6, 'fetch': 5, 'decode': 5,
    
    # Exceptions and interrupts
    'exception': 7, 'interrupt': 7, 'trap': 7, 'fault': 7,
}

# Module name keywords
MODULE_KEYWORDS = {
    'csr': 15, 'pmp': 15, 'control': 10, 'decoder': 8,
    'alu': 5, 'register': 7, 'fetch': 7, 'execute': 7,
}


class SecurityRanker:
    """Ranks modules by security criticality"""
    
    def __init__(self):
        self.modules: List[Tuple[str, int, object]] = []
    
    def calculate_score(self, module) -> int:
        """Calculate security score for a module"""
        score = 0
        
        # Score from module name
        module_name_lower = module.name.lower()
        for keyword, points in MODULE_KEYWORDS.items():
            if keyword in module_name_lower:
                score += points
        
        # Score from signals
        all_signals = module.get_all_signals()
        for signal in all_signals:
            signal_name_lower = signal.name.lower()
            for keyword, points in SECURITY_KEYWORDS.items():
                if keyword in signal_name_lower:
                    score += points
        
        # Bonus for sequential modules
        if module.is_sequential:
            score += 10
        
        # Bonus for having clock and reset
        if module.has_clock and module.has_reset:
            score += 5
        
        # Bonus for large number of signals
        signal_count = len(all_signals)
        if signal_count > 20:
            score += 10
        elif signal_count > 10:
            score += 5
        
        return score
    
    def add_module(self, file_path: str, module):
        """Add module to ranking"""
        score = self.calculate_score(module)
        self.modules.append((file_path, score, module))
    
    def get_ranked_modules(self, top_n: int = None) -> List[Tuple[str, int, object]]:
        """Get modules ranked by score"""
        ranked = sorted(self.modules, key=lambda x: x[1], reverse=True)
        if top_n:
            ranked = ranked[:top_n]
        return ranked
    
    def print_ranking(self, top_n: int = None):
        """Print ranking results"""
        ranked = self.get_ranked_modules(top_n)
        
        if not ranked:
            print("No modules found.")
            return
        
        print("\n" + "="*70)
        print("🔒 SECURITY-CRITICAL MODULE RANKING")
        print("="*70)
        
        if top_n:
            print(f"\nTop {len(ranked)} modules:")
        else:
            print(f"\nAll {len(ranked)} modules ranked:")
        
        print()
        
        for i, (file_path, score, module) in enumerate(ranked, 1):
            print(f"{i}. {module.name} (Score: {score}/100)")
            print(f"   File: {Path(file_path).name}")
            print(f"   Type: {'Sequential' if module.is_sequential else 'Combinational'}")
            print(f"   Signals: {len(module.get_all_signals())} total")
            print()
        
        print("="*70)


def parse_directory(directory: str, ranker: SecurityRanker) -> int:
    """Parse all .sv files in directory"""
    dir_path = Path(directory)
    
    if not dir_path.exists():
        print(f"Error: Directory not found: {directory}")
        return 0
    
    sv_files = list(dir_path.glob('*.sv')) + list(dir_path.glob('**/*.sv'))
    
    if not sv_files:
        print(f"No .sv files found in {directory}")
        return 0
    
    print(f"\nParsing {len(sv_files)} files from {directory}...\n")
    
    parsed_count = 0
    for sv_file in sv_files:
        try:
            parser = RTLParser(str(sv_file))
            module = parser.parse()
            
            if module:
                ranker.add_module(str(sv_file), module)
                parsed_count += 1
                print(f"  ✓ {module.name}")
            else:
                print(f"  ⚠ Could not parse: {sv_file.name}")
                
        except Exception as e:
            print(f"  ✗ Error: {sv_file.name}")
    
    print(f"\nParsed {parsed_count}/{len(sv_files)} modules")
    return parsed_count


def main():
    parser = argparse.ArgumentParser(
        description='Rank RISC-V modules by security criticality',
        epilog="""
Examples:
  python scripts/parse_and_rank.py examples/ibex/original --top 5
  python scripts/parse_and_rank.py my_processor/rtl --top 10
        """
    )
    
    parser.add_argument('directory', help='Directory containing .sv files')
    parser.add_argument('--top', type=int, help='Show top N modules')
    
    args = parser.parse_args()
    
    ranker = SecurityRanker()
    parsed_count = parse_directory(args.directory, ranker)
    
    if parsed_count == 0:
        return 1
    
    ranker.print_ranking(top_n=args.top)
    return 0


if __name__ == '__main__':
    sys.exit(main())