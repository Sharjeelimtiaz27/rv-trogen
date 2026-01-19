#!/usr/bin/env python3
"""
Pattern Library - Unified Access to All Trojan Patterns
Updated with correct Trust-Hub citations and literature sources
"""

from typing import List, Dict, Optional
from dataclasses import dataclass

from .dos_pattern import DoSPattern, dos_pattern
from .leak_pattern import LeakPattern, leak_pattern
from .privilege_pattern import PrivilegePattern, privilege_pattern
from .integrity_pattern import IntegrityPattern, integrity_pattern
from .availability_pattern import AvailabilityPattern, availability_pattern
from .covert_pattern import CovertPattern, covert_pattern


class PatternLibrary:
    """
    Unified access to all Trojan patterns with proper citations
    
    Citation Status:
        ✓ 3 Verified RTL Trust-Hub Benchmarks (DoS, Leak, Integrity)
        ✓ 1 Trust-Hub Category (Availability - gate-level only)
        ✓ 1 Related Trust-Hub Category (Covert - power only)
        ✓ 1 RISC-V Specific (Privilege - not in Trust-Hub)
    
    Usage:
        library = PatternLibrary()
        all_patterns = library.get_all_patterns()
        dos = library.get_pattern('DoS')
        
        # Get citation information
        library.print_summary()
        library.print_citation_report()
    """
    
    def __init__(self):
        """Initialize pattern library"""
        self.patterns = {
            'DoS': dos_pattern,
            'Leak': leak_pattern,
            'Privilege': privilege_pattern,
            'Integrity': integrity_pattern,
            'Availability': availability_pattern,
            'Covert': covert_pattern
        }
    
    def get_pattern(self, name: str):
        """
        Get pattern by name
        
        Args:
            name: Pattern name (DoS, Leak, Privilege, Integrity, Availability, Covert)
        
        Returns:
            Pattern object or None
        """
        return self.patterns.get(name)
    
    def get_all_patterns(self) -> List:
        """Get all patterns as list"""
        return list(self.patterns.values())
    
    def get_pattern_names(self) -> List[str]:
        """Get all pattern names"""
        return list(self.patterns.keys())
    
    def get_patterns_by_severity(self, severity: str) -> List:
        """
        Get patterns by severity level
        
        Args:
            severity: 'Critical', 'High', 'Medium', 'Low'
        
        Returns:
            List of matching patterns
        """
        return [p for p in self.patterns.values() if p.severity == severity]
    
    def get_patterns_by_module_type(self, module_type: str) -> List:
        """
        Get patterns suitable for module type
        
        Args:
            module_type: 'sequential', 'combinational', or 'both'
        
        Returns:
            List of suitable patterns
        """
        suitable = []
        for pattern in self.patterns.values():
            if pattern.preferred_module_type == 'both':
                suitable.append(pattern)
            elif pattern.preferred_module_type == module_type:
                suitable.append(pattern)
        return suitable
    
    def get_verified_trust_hub_patterns(self) -> List:
        """Get patterns with verified Trust-Hub RTL benchmarks"""
        return [p for p in self.patterns.values() 
                if p.trust_hub_status == "Verified RTL Benchmarks"]
    
    def get_literature_based_patterns(self) -> List:
        """Get patterns based on literature (not direct Trust-Hub)"""
        return [p for p in self.patterns.values() 
                if "N/A" in p.trust_hub_benchmarks or "gate-level" in p.trust_hub_status]
    
    def print_summary(self):
        """Print summary of all patterns"""
        print("\n" + "="*100)
        print("PATTERN LIBRARY - CITATION SUMMARY")
        print("="*100)
        print(f"{'Pattern':<15} {'Category':<25} {'Severity':<10} {'Trust-Hub Status':<45}")
        print("-"*100)
        
        for name, pattern in self.patterns.items():
            status = pattern.trust_hub_status[:43] + ".." if len(pattern.trust_hub_status) > 45 else pattern.trust_hub_status
            print(f"{name:<15} {pattern.category:<25} {pattern.severity:<10} {status:<45}")
        
        print("="*100)
        print(f"Total Patterns: {len(self.patterns)}")
        print(f"Verified RTL Benchmarks: {len(self.get_verified_trust_hub_patterns())}")
        print(f"Literature-Based: {len(self.get_literature_based_patterns())}")
        print("="*100 + "\n")
    
    def print_citation_report(self):
        """Print detailed citation report for paper"""
        print("\n" + "="*100)
        print("CITATION REPORT FOR PAPER")
        print("="*100)
        
        print("\n1. VERIFIED TRUST-HUB RTL BENCHMARKS:")
        print("-" * 100)
        for pattern in self.get_verified_trust_hub_patterns():
            print(f"\n{pattern.name} - {pattern.category}")
            print(f"  Category: {pattern.trust_hub_category}")
            print(f"  Benchmarks: {pattern.trust_hub_benchmarks}")
            print(f"  Adaptation: {pattern.adaptation_note}")
        
        print("\n\n2. LITERATURE-BASED PATTERNS:")
        print("-" * 100)
        for pattern in self.get_literature_based_patterns():
            print(f"\n{pattern.name} - {pattern.category}")
            print(f"  Trust-Hub Status: {pattern.trust_hub_status}")
            print(f"  Citations:")
            for citation in pattern.rtl_citations:
                print(f"    - {citation}")
            print(f"  Adaptation: {pattern.adaptation_note}")
        
        print("\n" + "="*100)
        print("SUMMARY FOR PAPER:")
        print("-" * 100)
        print("✓ 3 patterns adapted from Trust-Hub RTL benchmarks (DoS, Leak, Integrity)")
        print("✓ 1 pattern adapted from Trust-Hub category (Availability - RTL implementation)")
        print("✓ 1 pattern extending Trust-Hub concept (Covert - timing channels)")
        print("✓ 1 pattern from RISC-V literature (Privilege - processor-specific)")
        print("="*100 + "\n")
    
    def get_bibtex_entries(self) -> str:
        """Generate BibTeX entries for all patterns"""
        bibtex = """
% Trust-Hub Benchmarks
@misc{trusthub_dos,
  title = {{Trust-Hub AES-T1800, T1900, T500: Denial of Service Trojans}},
  howpublished = {\\url{https://trust-hub.org}},
  note = {Accessed: January 2025}
}

@misc{trusthub_leak,
  title = {{Trust-Hub AES-T600, T1400, T800: Information Leakage Trojans}},
  howpublished = {\\url{https://trust-hub.org}},
  note = {Accessed: January 2025}
}

@misc{trusthub_integrity,
  title = {{Trust-Hub AES-T2500-T2800: Data Integrity Trojans}},
  howpublished = {\\url{https://trust-hub.org}},
  note = {Accessed: January 2025}
}

% Performance Degradation
@inproceedings{boraten2016mitigation,
  title={Mitigation of Denial of Service Attack with Hardware Trojans in NoC Architectures},
  author={Boraten, Tayfun and Kodi, Avinash Karanth},
  booktitle={IEEE International Parallel and Distributed Processing Symposium (IPDPS)},
  pages={1091--1100},
  year={2016}
}

@inproceedings{jin2008hardware,
  title={Hardware Trojan Detection Using Path Delay Fingerprint},
  author={Jin, Yier and Makris, Yiorgos},
  booktitle={IEEE International Workshop on Hardware-Oriented Security and Trust (HOST)},
  year={2008}
}

% Privilege Escalation
@misc{bailey2017riscv,
  author = {Bailey, David A.},
  title = {{The RISC-V Files: Supervisor to Machine Privilege Escalation}},
  year = {2017},
  howpublished = {Security Mouse Blog},
  url = {http://blog.securitymouse.com/2017/04/the-risc-v-files-supervisor-machine.html}
}

@inproceedings{dessouky2017lophi,
  title={LO-PHI: Low-Observable Physical Host Instrumentation for Malware Analysis},
  author={Dessouky, Ghada and others},
  booktitle={Network and Distributed System Security Symposium (NDSS)},
  year={2017}
}

@article{clercq2017survey,
  title={A Survey on Hardware-based Control Flow Integrity (CFI)},
  author={De Clercq, Roel and Verbauwhede, Ingrid},
  journal={ACM Computing Surveys},
  volume={51},
  number={6},
  year={2017}
}

% Covert Channels
@inproceedings{kocher1996timing,
  title={Timing Attacks on Implementations of Diffie-Hellman, RSA, DSS, and Other Systems},
  author={Kocher, Paul C},
  booktitle={Annual International Cryptology Conference (CRYPTO)},
  pages={104--113},
  year={1996}
}

@inproceedings{lipp2021tapeout,
  title={Tapeout of a RISC-V Crypto Chip with Hardware Trojans},
  author={Lipp, Moritz and others},
  booktitle={ACM International Conference on Computing Frontiers (CF)},
  year={2021},
  doi={10.1145/3457388.3458869}
}

@inproceedings{lin2009trojan,
  title={Trojan Side-Channels: Lightweight Hardware Trojans through Side-Channel Engineering},
  author={Lin, Lang and others},
  booktitle={Cryptographic Hardware and Embedded Systems (CHES)},
  pages={382--395},
  year={2009}
}
"""
        return bibtex


# Create default library instance
pattern_library = PatternLibrary()


def get_pattern(name: str):
    """Convenience function to get pattern by name"""
    return pattern_library.get_pattern(name)


def get_all_patterns() -> List:
    """Convenience function to get all patterns"""
    return pattern_library.get_all_patterns()


def get_pattern_library() -> PatternLibrary:
    """Get pattern library instance"""
    return pattern_library


if __name__ == "__main__":
    # Demo
    library = PatternLibrary()
    library.print_summary()
    library.print_citation_report()
    
    print("\nCritical Patterns:")
    for p in library.get_patterns_by_severity('Critical'):
        print(f"  - {p.name}: {p.description}")
    
    print("\nSequential Patterns:")
    for p in library.get_patterns_by_module_type('sequential'):
        print(f"  - {p.name}")