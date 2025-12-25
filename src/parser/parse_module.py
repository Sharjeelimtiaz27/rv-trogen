#!/usr/bin/env python3
"""
Legacy Parser Interface (Backward Compatibility)
Uses new refactored modules internally
"""

from .rtl_parser import RTLParser, Module, main

# For backward compatibility
SVParser = RTLParser

if __name__ == "__main__":
    main()