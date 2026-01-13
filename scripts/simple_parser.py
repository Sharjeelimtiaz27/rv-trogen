#!/usr/bin/env python3
"""
Simple Regex-Based Module Parser
Reliably extracts module name, parameters, and ports from SystemVerilog
"""

import re
from pathlib import Path
from dataclasses import dataclass
from typing import List, Dict, Optional


@dataclass
class Signal:
    """Signal information"""
    name: str
    direction: str  # 'input' or 'output'
    width: int      # Bit width (1 for single bit)
    is_vector: bool
    
    def __repr__(self):
        if self.is_vector:
            return f"{self.direction} [{self.width-1}:0] {self.name}"
        return f"{self.direction} {self.name}"


@dataclass
class Module:
    """Parsed module information"""
    name: str
    parameters: Dict[str, str]
    inputs: List[Signal]
    outputs: List[Signal]
    clock_signal: Optional[str] = None
    reset_signal: Optional[str] = None
    is_sequential: bool = True
    
    def get_all_signals(self):
        return self.inputs + self.outputs


class SimpleModuleParser:
    """
    Simple regex-based parser for SystemVerilog modules
    Handles parameterized modules correctly
    """
    
    def __init__(self, filepath: str):
        self.filepath = Path(filepath)
        self.content = self.filepath.read_text()
        
    def parse(self) -> Module:
        """Parse the module and return Module object"""
        
        # Extract module name and parameters
        module_name, parameters = self._parse_module_header()
        
        # Extract ports
        inputs, outputs = self._parse_ports(parameters)
        
        # Detect clock and reset
        clock_signal = self._detect_clock(inputs)
        reset_signal = self._detect_reset(inputs)
        is_sequential = clock_signal is not None
        
        return Module(
            name=module_name,
            parameters=parameters,
            inputs=inputs,
            outputs=outputs,
            clock_signal=clock_signal,
            reset_signal=reset_signal,
            is_sequential=is_sequential
        )
    
    def _parse_module_header(self):
        """Extract module name and parameters"""
        
        # Match: module name #(parameters) (
        pattern = r'module\s+(\w+)\s*(?:#\s*\((.*?)\))?\s*\('
        match = re.search(pattern, self.content, re.DOTALL)
        
        if not match:
            raise ValueError("Could not find module declaration")
        
        module_name = match.group(1)
        param_section = match.group(2)
        
        # Parse parameters
        parameters = {}
        if param_section:
            parameters = self._parse_parameters(param_section)
        
        return module_name, parameters
    
    def _parse_parameters(self, param_section: str) -> Dict[str, str]:
        """Parse parameter declarations"""
        parameters = {}
        
        # Match: parameter type Name = Value
        param_pattern = r'parameter\s+(?:int\s+unsigned\s+)?(?:bit\s+)?(?:\[.*?\]\s+)?(\w+)\s*=\s*([^,\)]+)'
        
        for match in re.finditer(param_pattern, param_section):
            param_name = match.group(1)
            param_value = match.group(2).strip()
            
            # Evaluate simple expressions
            if "'" in param_value:
                # It's a literal like 32 or 1'b0
                parameters[param_name] = param_value
            else:
                # Try to evaluate as integer
                try:
                    parameters[param_name] = str(eval(param_value))
                except:
                    parameters[param_name] = param_value
        
        return parameters
    
    def _parse_ports(self, parameters: Dict[str, str]) -> tuple:
        """Parse input/output port declarations"""
        
        inputs = []
        outputs = []
        
        # Find port list (between module declaration and );)
        port_pattern = r'module\s+\w+.*?\((.*?)\);'
        match = re.search(port_pattern, self.content, re.DOTALL)
        
        if not match:
            return inputs, outputs
        
        port_section = match.group(1)
        
        # Match port declarations
        # Handles: input logic [Width-1:0] name,
        #         output logic name,
        #         input logic [31:0] name
        port_decl_pattern = r'(input|output)\s+logic\s*(?:\[([^\]]+)\])?\s*(\w+)'
        
        for match in re.finditer(port_decl_pattern, port_section):
            direction = match.group(1)
            width_expr = match.group(2)
            signal_name = match.group(3)
            
            # Calculate width
            if width_expr:
                width = self._eval_width(width_expr, parameters)
                is_vector = True
            else:
                width = 1
                is_vector = False
            
            signal = Signal(
                name=signal_name,
                direction=direction,
                width=width,
                is_vector=is_vector
            )
            
            if direction == 'input':
                inputs.append(signal)
            else:
                outputs.append(signal)
        
        return inputs, outputs
    
    def _eval_width(self, width_expr: str, parameters: Dict[str, str]) -> int:
        """Evaluate width expression like 'Width-1:0' or '31:0'"""
        
        # Extract high part (before :)
        high_part = width_expr.split(':')[0].strip()
        
        # Replace parameter names with values
        for param_name, param_value in parameters.items():
            high_part = high_part.replace(param_name, param_value)
        
        # Evaluate expression
        try:
            high_val = eval(high_part)
            return high_val + 1  # Width is high_val + 1
        except:
            # Fallback to 32 if can't evaluate
            return 32
    
    def _detect_clock(self, inputs: List[Signal]) -> Optional[str]:
        """Detect clock signal"""
        clock_keywords = ['clk', 'clock']
        for sig in inputs:
            if any(kw in sig.name.lower() for kw in clock_keywords):
                return sig.name
        return None
    
    def _detect_reset(self, inputs: List[Signal]) -> Optional[str]:
        """Detect reset signal"""
        reset_keywords = ['rst', 'reset']
        for sig in inputs:
            if any(kw in sig.name.lower() for kw in reset_keywords):
                return sig.name
        return None


def test_parser():
    """Test the parser"""
    test_sv = """
module ibex_csr #(
  parameter int unsigned    Width      = 32,
  parameter bit             ShadowCopy = 1'b0,
  parameter bit [Width-1:0] ResetValue = '0
 ) (
  input  logic             clk_i,
  input  logic             rst_ni,
  input  logic [Width-1:0] wr_data_i,
  input  logic             wr_en_i,
  output logic [Width-1:0] rd_data_o,
  output logic             rd_error_o
);
endmodule
"""
    
    # Save test file
    Path('/tmp/test_module.sv').write_text(test_sv)
    
    # Parse
    parser = SimpleModuleParser('/tmp/test_module.sv')
    module = parser.parse()
    
    print(f"Module: {module.name}")
    print(f"Parameters: {module.parameters}")
    print(f"Inputs:")
    for sig in module.inputs:
        print(f"  {sig}")
    print(f"Outputs:")
    for sig in module.outputs:
        print(f"  {sig}")
    print(f"Clock: {module.clock_signal}")
    print(f"Reset: {module.reset_signal}")


if __name__ == '__main__':
    test_parser()