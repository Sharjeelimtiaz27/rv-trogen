# examples/parse_example.py
"""
Usage:
  python examples/parse_example.py path/to/file.sv
"""

import sys
from pathlib import Path
from src.parser import parse_modules

def summarize_module(m):
    print(f"Module: {m['name']}")
    print(f"  Ports: {len(m['signals'].get('ports', []))}")
    decls = m['signals'].get('decls', [])
    print(f"  Declarations: {sum(len(d['names']) for d in decls)}")
    cls = m.get("classification", {})
    print(f"  Sequential: {cls.get('is_sequential')}, Combinational: {cls.get('is_combinational')}")
    print("-" * 40)

def main(path):
    p = Path(path)
    if not p.exists():
        print("File not found:", p)
        return
    mods = parse_modules(p.read_text(encoding="utf8"))
    print(f"Found {len(mods)} modules in {p.name}")
    for m in mods:
        summarize_module(m)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python examples/parse_example.py path/to/file.sv")
    else:
        main(sys.argv[1])
