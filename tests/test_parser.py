#!/usr/bin/env python3
"""
Unit Tests for RTL Parser
"""

import pytest
from pathlib import Path
import sys

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.parser import RTLParser, SignalExtractor, ModuleClassifier, Signal


class TestSignalExtractor:
    """Test SignalExtractor class"""
    
    def test_extract_simple_input(self):
        """Test extracting simple input"""
        content = """
        module test (
            input clk_i,
            input rst_ni
        );
        endmodule
        """
        
        extractor = SignalExtractor(content)
        inputs = extractor.extract_inputs()
        
        assert len(inputs) == 2
        assert inputs[0].name == 'clk_i'
        assert inputs[0].signal_type == 'input'
        assert inputs[0].width == 1
        assert inputs[0].is_vector == False
    
    def test_extract_vector_input(self):
        """Test extracting vector input"""
        content = """
        module test (
            input [31:0] data_i
        );
        endmodule
        """
        
        extractor = SignalExtractor(content)
        inputs = extractor.extract_inputs()
        
        assert len(inputs) == 1
        assert inputs[0].name == 'data_i'
        assert inputs[0].width == 32
        assert inputs[0].is_vector == True
    
    def test_extract_logic_input(self):
        """Test extracting logic input"""
        content = """
        module test (
            input logic [15:0] addr_i
        );
        endmodule
        """
        
        extractor = SignalExtractor(content)
        inputs = extractor.extract_inputs()
        
        assert len(inputs) == 1
        assert inputs[0].name == 'addr_i'
        assert inputs[0].width == 16
    
    def test_extract_outputs(self):
        """Test extracting outputs"""
        content = """
        module test (
            output valid_o,
            output [7:0] data_o
        );
        endmodule
        """
        
        extractor = SignalExtractor(content)
        outputs = extractor.extract_outputs()
        
        assert len(outputs) == 2
        assert outputs[0].name == 'valid_o'
        assert outputs[1].name == 'data_o'
        assert outputs[1].width == 8
    
    def test_extract_internals(self):
        """Test extracting internal signals"""
        content = """
        module test;
            logic [31:0] counter;
            wire valid;
            reg [7:0] state;
        endmodule
        """
        
        extractor = SignalExtractor(content)
        internals = extractor.extract_internals()
        
        names = [s.name for s in internals]
        assert 'counter' in names
        assert 'valid' in names
        assert 'state' in names


class TestModuleClassifier:
    """Test ModuleClassifier class"""
    
    def test_detect_sequential_always_ff(self):
        """Test sequential detection with always_ff"""
        content = """
        module test;
            always_ff @(posedge clk) begin
                counter <= counter + 1;
            end
        endmodule
        """
        
        classifier = ModuleClassifier(content, [])
        assert classifier.is_sequential() == True
    
    def test_detect_sequential_posedge(self):
        """Test sequential detection with @(posedge)"""
        content = """
        module test;
            always @(posedge clk) begin
                data <= data_in;
            end
        endmodule
        """
        
        classifier = ModuleClassifier(content, [])
        assert classifier.is_sequential() == True
    
    def test_detect_combinational(self):
        """Test combinational detection"""
        content = """
        module test;
            always_comb begin
                result = a + b;
            end
        endmodule
        """
        
        classifier = ModuleClassifier(content, [])
        assert classifier.is_sequential() == False
    
    def test_detect_clock_signal(self):
        """Test clock signal detection"""
        signals = [
            Signal('clk_i', 'input', 1, False),
            Signal('data_i', 'input', 32, True)
        ]
        
        classifier = ModuleClassifier("", signals)
        assert classifier.has_clock() == True
        assert classifier.get_clock_signal() == 'clk_i'
    
    def test_detect_reset_signal(self):
        """Test reset signal detection"""
        signals = [
            Signal('rst_ni', 'input', 1, False),
            Signal('data_i', 'input', 32, True)
        ]
        
        classifier = ModuleClassifier("", signals)
        assert classifier.has_reset() == True
        assert classifier.get_reset_signal() == 'rst_ni'


class TestRTLParser:
    """Test RTLParser class"""
    
    def test_parse_simple_module(self, tmp_path):
        """Test parsing a simple module"""
        # Create temporary test file
        test_file = tmp_path / "test.sv"
        test_file.write_text("""
module simple_test (
    input clk_i,
    input rst_ni,
    input [31:0] data_i,
    output [31:0] data_o
);
    logic [31:0] register_q;
    
    always_ff @(posedge clk_i or negedge rst_ni) begin
        if (!rst_ni) begin
            register_q <= 32'h0;
        end else begin
            register_q <= data_i;
        end
    end
    
    assign data_o = register_q;
endmodule
        """)
        
        # Parse
        parser = RTLParser(str(test_file))
        module = parser.parse()
        
        # Verify
        assert module.name == 'simple_test'
        assert len(module.inputs) == 3
        assert len(module.outputs) == 1
        assert module.is_sequential == True
        assert module.has_clock == True
        assert module.has_reset == True
    
    def test_extract_module_name(self, tmp_path):
        """Test module name extraction"""
        test_file = tmp_path / "test.sv"
        test_file.write_text("module my_module; endmodule")
        
        parser = RTLParser(str(test_file))
        name = parser._extract_module_name()
        
        assert name == 'my_module'
    
    @pytest.mark.skipif(
        not Path("examples/ibex/original/ibex_cs_registers.sv").exists(),
        reason="Ibex CSR file not available"
    )
    def test_parse_real_ibex_csr(self):
        """Test parsing real Ibex CSR module"""
        parser = RTLParser("examples/ibex/original/ibex_cs_registers.sv")
        module = parser.parse()
        
        assert module.name == 'ibex_cs_registers'
        assert len(module.inputs) > 10
        assert len(module.outputs) > 5
        assert module.is_sequential == True
        assert module.has_clock == True
        assert module.has_reset == True


class TestBackwardCompatibility:
    """Test backward compatibility"""
    
    def test_svparser_alias(self):
        """Test SVParser alias exists"""
        from src.parser.parse_module import SVParser
        assert SVParser is RTLParser


# Run tests
if __name__ == "__main__":
    pytest.main([__file__, "-v"])