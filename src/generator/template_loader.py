"""
Template Loader Module
Loads SystemVerilog templates from disk for Trojan generation
"""

import os
from pathlib import Path
from typing import Dict, Optional

class TemplateLoader:
    """Loads and manages Trojan templates"""
    
    def __init__(self, templates_dir: Optional[str] = None):
        """
        Initialize template loader
        
        Args:
            templates_dir: Path to templates directory (default: auto-detect)
        """
        if templates_dir is None:
            # Auto-detect templates directory
            current_dir = Path(__file__).parent
            self.templates_dir = current_dir.parent.parent / "templates" / "trojan_templates"
        else:
            self.templates_dir = Path(templates_dir)
            
        if not self.templates_dir.exists():
            raise FileNotFoundError(f"Templates directory not found: {self.templates_dir}")
    
    def load_template(self, pattern_name: str, template_type: str) -> str:
        """
        Load a template file
        
        Args:
            pattern_name: Pattern name (dos, leak, privilege, etc.)
            template_type: Template type (sequential or combinational)
            
        Returns:
            Template content as string
            
        Raises:
            FileNotFoundError: If template file doesn't exist
        """
        # Normalize pattern name to lowercase
        pattern_name_lower = pattern_name.lower()
        template_path = self.templates_dir / template_type / f"{pattern_name_lower}_template.sv"
        
        if not template_path.exists():
            raise FileNotFoundError(f"Template not found: {template_path}")
        
        with open(template_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def load_all_templates(self, template_type: str) -> Dict[str, str]:
        """
        Load all templates of a given type
        
        Args:
            template_type: Template type (sequential or combinational)
            
        Returns:
            Dictionary mapping pattern names to template content
        """
        templates = {}
        template_dir = self.templates_dir / template_type
        
        if not template_dir.exists():
            return templates
        
        for template_file in template_dir.glob("*_template.sv"):
            pattern_name = template_file.stem.replace("_template", "")
            templates[pattern_name] = self.load_template(pattern_name, template_type)
        
        return templates
    
    def list_available_templates(self) -> Dict[str, list]:
        """
        List all available templates
        
        Returns:
            Dictionary with template types and their available patterns
        """
        available = {}
        
        for template_type in ["sequential", "combinational"]:
            type_dir = self.templates_dir / template_type
            if type_dir.exists():
                patterns = [f.stem.replace("_template", "") 
                           for f in type_dir.glob("*_template.sv")]
                available[template_type] = sorted(patterns)
        
        return available