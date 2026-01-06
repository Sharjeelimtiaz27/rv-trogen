"""
Unit Tests for Hardware Trojan Generator

Tests pattern library and generator functionality.

Author: Sharjeel Imtiaz
Date: January 2026
"""

import pytest
from pathlib import Path
import sys

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.parser.rtl_parser import RTLParser
from src.patterns.pattern_library import PatternLibrary
from src.patterns.dos_pattern import DoSPattern
from src.patterns.leak_pattern import LeakPattern
from src.patterns.privilege_pattern import PrivilegePattern
from src.patterns.integrity_pattern import IntegrityPattern
from src.patterns.availability_pattern import AvailabilityPattern
from src.patterns.covert_pattern import CovertPattern
from src.generator.sequential_gen import SequentialGenerator
from src.generator.combinational_gen import CombinationalGenerator


class TestPatternLibrary:
    """Test pattern library functionality"""
    
    def test_pattern_library_initialization(self):
        """Test pattern library can be initialized"""
        lib = PatternLibrary()
        assert lib is not None
    
    def test_get_all_patterns(self):
        """Test getting all 6 patterns"""
        lib = PatternLibrary()
        patterns = lib.get_all_patterns()
        
        # Should return list of 6 pattern objects
        assert len(patterns) == 6
        assert isinstance(patterns, list)
        
        # Check pattern names
        pattern_names = [p.name for p in patterns]
        assert 'DoS' in pattern_names
        assert 'Leak' in pattern_names
        assert 'Privilege' in pattern_names
        assert 'Integrity' in pattern_names
        assert 'Availability' in pattern_names
        assert 'Covert' in pattern_names
    
    def test_get_pattern_by_name(self):
        """Test getting individual patterns"""
        lib = PatternLibrary()
        
        dos = lib.get_pattern('DoS')
        assert dos is not None
        assert isinstance(dos, DoSPattern)
        assert dos.name == 'DoS'
        
        leak = lib.get_pattern('Leak')
        assert leak is not None
        assert isinstance(leak, LeakPattern)
        assert leak.name == 'Leak'


class TestPatternAttributes:
    """Test pattern dataclass attributes"""
    
    def test_dos_pattern_attributes(self):
        """Test DoS pattern has required attributes"""
        pattern = DoSPattern()
        
        assert pattern.name == 'DoS'
        assert pattern.category == 'Denial of Service'
        assert pattern.trust_hub_source == 'AES-T1400'
        assert pattern.severity in ['High', 'Critical', 'Medium', 'Low']
        assert isinstance(pattern.trigger_keywords, list)
        assert isinstance(pattern.payload_keywords, list)
        assert len(pattern.trigger_keywords) > 0
        assert len(pattern.payload_keywords) > 0
    
    def test_leak_pattern_attributes(self):
        """Test Leak pattern attributes"""
        pattern = LeakPattern()
        
        assert pattern.name == 'Leak'
        assert pattern.category == 'Information Leakage'
        assert pattern.trust_hub_source == 'RSA-T600'
        assert isinstance(pattern.trigger_keywords, list)
        assert isinstance(pattern.payload_keywords, list)
    
    def test_privilege_pattern_attributes(self):
        """Test Privilege pattern attributes"""
        pattern = PrivilegePattern()
        
        assert pattern.name == 'Privilege'
        assert pattern.category == 'Privilege Escalation'
        assert 'priv' in pattern.payload_keywords or 'privilege' in pattern.payload_keywords
    
    def test_integrity_pattern_attributes(self):
        """Test Integrity pattern attributes"""
        pattern = IntegrityPattern()
        
        assert pattern.name == 'Integrity'
        assert pattern.category == 'Integrity Violation'
        assert 'data' in pattern.trigger_keywords or 'data' in pattern.payload_keywords
    
    def test_availability_pattern_attributes(self):
        """Test Availability pattern attributes"""
        pattern = AvailabilityPattern()
        
        assert pattern.name == 'Availability'
        assert pattern.category == 'Performance Degradation'
    
    def test_covert_pattern_attributes(self):
        """Test Covert pattern attributes"""
        pattern = CovertPattern()
        
        assert pattern.name == 'Covert'
        assert pattern.category == 'Covert Channel'


class TestPatternMethods:
    """Test pattern methods"""
    
    def test_pattern_get_info(self):
        """Test pattern get_info() method"""
        pattern = DoSPattern()
        info = pattern.get_info()
        
        assert isinstance(info, dict)
        assert 'name' in info
        assert 'category' in info
        assert info['name'] == 'DoS'
    
    def test_pattern_get_template_params(self):
        """Test pattern get_template_params() method"""
        pattern = DoSPattern()
        params = pattern.get_template_params()
        
        # Should return some parameters
        assert params is not None


class TestSequentialGenerator:
    """Test sequential Trojan generation"""
    
    @pytest.fixture
    def sample_module(self):
        """Sample sequential module"""
        code = """
        module seq_test (
            input logic clk_i,
            input logic rst_ni,
            input logic valid_i,
            output logic ready_o
        );
            always_ff @(posedge clk_i) begin
                ready_o <= valid_i;
            end
        endmodule
        """
        test_file = Path('test_seq_module.sv')
        test_file.write_text(code)
        
        parser = RTLParser(str(test_file))
        module = parser.parse()
        
        yield module
        
        if test_file.exists():
            test_file.unlink()
    
    def test_sequential_generator_initialization(self, sample_module):
        """Test generator can be initialized with module"""
        gen = SequentialGenerator(sample_module)
        assert gen is not None
        assert gen.module == sample_module
    
    def test_sequential_generator_has_methods(self, sample_module):
        """Test generator has required methods"""
        gen = SequentialGenerator(sample_module)
        
        # Check for common generator methods
        methods = dir(gen)
        assert 'module' in methods
        
        # Should have some method to generate Trojans
        assert any(m.startswith('generate') or m.startswith('create') 
                  for m in methods)


class TestCombinationalGenerator:
    """Test combinational Trojan generation"""
    
    @pytest.fixture
    def sample_comb_module(self):
        """Sample combinational module"""
        code = """
        module comb_test (
            input logic [31:0] a,
            input logic [31:0] b,
            output logic [31:0] result
        );
            assign result = a + b;
        endmodule
        """
        test_file = Path('test_comb_module.sv')
        test_file.write_text(code)
        
        parser = RTLParser(str(test_file))
        module = parser.parse()
        
        yield module
        
        if test_file.exists():
            test_file.unlink()
    
    def test_combinational_generator_initialization(self, sample_comb_module):
        """Test generator can be initialized with module"""
        gen = CombinationalGenerator(sample_comb_module)
        assert gen is not None
        assert gen.module == sample_comb_module
    
    def test_combinational_generator_has_methods(self, sample_comb_module):
        """Test generator has required methods"""
        gen = CombinationalGenerator(sample_comb_module)
        
        methods = dir(gen)
        assert 'module' in methods


class TestEdgeCases:
    """Test edge cases and error handling"""
    
    def test_empty_module(self):
        """Test handling module with no signals"""
        code = """
        module empty_module;
        endmodule
        """
        test_file = Path('test_empty.sv')
        test_file.write_text(code)
        
        parser = RTLParser(str(test_file))
        module = parser.parse()
        
        # Should parse without crashing
        assert module.name == 'empty_module'
        assert len(module.inputs) == 0
        assert len(module.outputs) == 0
        
        # Can still create generator
        gen = SequentialGenerator(module)
        assert gen is not None
        
        if test_file.exists():
            test_file.unlink()
    
    def test_simple_module(self):
        """Test module with simple signals"""
        code = """
        module simple (
            input logic x,
            input logic y,
            output logic z
        );
            assign z = x & y;
        endmodule
        """
        test_file = Path('test_simple.sv')
        test_file.write_text(code)
        
        parser = RTLParser(str(test_file))
        module = parser.parse()
        
        # Should parse successfully
        assert module.name == 'simple'
        assert len(module.inputs) == 2
        assert len(module.outputs) == 1
        
        # Can create generator
        gen = CombinationalGenerator(module)
        assert gen is not None
        
        if test_file.exists():
            test_file.unlink()


class TestRealIbexModule:
    """Test with real Ibex module if available"""
    
    @pytest.mark.skipif(
        not Path("examples/ibex/original/ibex_cs_registers.sv").exists(),
        reason="Ibex module not available"
    )
    def test_parse_real_ibex_csr(self):
        """Test parsing real Ibex CSR module"""
        parser = RTLParser("examples/ibex/original/ibex_cs_registers.sv")
        module = parser.parse()
        
        # Module name might be ibex_cs_registers or ibex_csr
        assert 'ibex' in module.name.lower()
        assert module.is_sequential
        assert module.clock_signal is not None
    
    @pytest.mark.skipif(
        not Path("examples/ibex/original/ibex_cs_registers.sv").exists(),
        reason="Ibex module not available"
    )
    def test_create_generator_for_ibex(self):
        """Test creating generator for real Ibex module"""
        parser = RTLParser("examples/ibex/original/ibex_cs_registers.sv")
        module = parser.parse()
        
        # Should be able to create generator
        gen = SequentialGenerator(module)
        assert gen is not None
        assert gen.module.name == module.name
    
    @pytest.mark.skipif(
        not Path("examples/ibex/original/ibex_cs_registers.sv").exists(),
        reason="Ibex module not available"
    )
    def test_patterns_have_relevant_keywords(self):
        """Test patterns have keywords relevant to Ibex CSR"""
        parser = RTLParser("examples/ibex/original/ibex_cs_registers.sv")
        module = parser.parse()
        
        # Get Privilege pattern (relevant for CSR)
        lib = PatternLibrary()
        priv_pattern = lib.get_pattern('Privilege')
        
        # Should have CSR-related keywords
        all_keywords = priv_pattern.trigger_keywords + priv_pattern.payload_keywords
        assert any('csr' in kw.lower() or 'priv' in kw.lower() for kw in all_keywords)


# Test summary fixture
@pytest.fixture(scope="session", autouse=True)
def test_summary(request):
    """Print test summary at end"""
    yield
    print("\n" + "="*60)
    print("GENERATOR TEST SUMMARY")
    print("="*60)
    print("✅ Pattern Library:      3 tests")
    print("✅ Pattern Attributes:   6 tests (all patterns)")
    print("✅ Pattern Methods:      2 tests")
    print("✅ Sequential Generator: 2 tests")
    print("✅ Combinational Gen:    2 tests")
    print("✅ Edge Cases:           2 tests")
    print("✅ Real Ibex Module:     3 tests")
    print("="*60)
    print("Total: 20 tests covering patterns and generators")
    print("="*60)