"""
Placeholder Handler Module
Replaces placeholders in templates with actual signal names
"""

from typing import Dict, List
import re

class PlaceholderHandler:
    """Handles placeholder replacement in templates"""
    
    # Standard placeholders
    PLACEHOLDERS = {
        'MODULE_NAME': 'Original module name',
        'CLOCK_SIGNAL': 'Clock signal name',
        'RESET_SIGNAL': 'Reset signal name',
        'TRIGGER_SIGNAL': 'Trojan trigger signal',
        'PAYLOAD_SIGNAL': 'Trojan payload target signal',
        'TRIGGER_CONDITION': 'Trigger condition logic',
        'PAYLOAD_ACTION': 'Payload action logic',
        'COUNTER_WIDTH': 'Counter bit width',
        'COUNTER_THRESHOLD': 'Counter threshold value',
        'DATA_WIDTH': 'Data bus width',
        'TROJAN_ID': 'Unique Trojan identifier',
    }
    
    def __init__(self):
        """Initialize placeholder handler"""
        pass
    
    def replace_placeholders(self, template: str, replacements: Dict[str, str]) -> str:
        """
        Replace all placeholders in template
        
        Args:
            template: Template content with {{PLACEHOLDERS}}
            replacements: Dictionary mapping placeholder names to values
            
        Returns:
            Template with placeholders replaced
        """
        result = template
        
        for placeholder, value in replacements.items():
            # Replace {{PLACEHOLDER}} with value
            pattern = f"{{{{{placeholder}}}}}"
            result = result.replace(pattern, str(value))
        
        return result
    
    def find_missing_placeholders(self, template: str, replacements: Dict[str, str]) -> List[str]:
        """
        Find placeholders in template that weren't replaced
        
        Args:
            template: Template content
            replacements: Dictionary of replacements that were provided
            
        Returns:
            List of missing placeholder names
        """
        # Find all {{PLACEHOLDER}} patterns
        placeholders_in_template = re.findall(r'\{\{([A-Z_]+)\}\}', template)
        
        # Find which ones weren't replaced
        missing = [p for p in placeholders_in_template if p not in replacements]
        
        return list(set(missing))  # Remove duplicates
    
    def validate_replacements(self, template: str, replacements: Dict[str, str]) -> tuple:
        """
        Validate that all required placeholders have replacements
        
        Args:
            template: Template content
            replacements: Dictionary of replacements
            
        Returns:
            Tuple of (is_valid, missing_placeholders)
        """
        missing = self.find_missing_placeholders(template, replacements)
        return (len(missing) == 0, missing)
    
    def get_placeholder_list(self, template: str) -> List[str]:
        """
        Get list of all placeholders in a template
        
        Args:
            template: Template content
            
        Returns:
            List of placeholder names found in template
        """
        placeholders = re.findall(r'\{\{([A-Z_]+)\}\}', template)
        return sorted(list(set(placeholders)))