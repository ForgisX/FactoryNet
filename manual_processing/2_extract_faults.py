"""
Script 2: Extract fault codes, fixing instructions, and machine metadata from markdown.

Usage:
    python 2_extract_faults.py <input_markdown_path> [output_json_path]
    
Example:
    python 2_extract_faults.py data/markdown_outputs/manual.md data/extracted/manual_faults.json
"""

import sys
import json
import re
import logging
from pathlib import Path
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def extract_metadata(content: str) -> Dict:
    """
    Extract machine metadata from the manual.
    
    Args:
        content: Markdown content
        
    Returns:
        Dictionary with metadata
    """
    metadata = {
        "model": None,
        "manufacturer": None,
        "manual_id": None,
        "manual_type": None
    }
    
    # Extract model (e.g., "C1000 i A", "FANUC LASER-MODEL C1000 i A")
    model_patterns = [
        r'(?:MODEL|Model)\s+([A-Z0-9\s\-]+(?:i\s+[A-Z])?)',
        r'FANUC\s+LASER[- ]MODEL\s+([A-Z0-9\s\-]+)',
        r'(?:^|\s)([A-Z]\d{3,4}\s*i\s*[A-Z])',
    ]
    
    for pattern in model_patterns:
        match = re.search(pattern, content[:5000], re.IGNORECASE)
        if match:
            metadata["model"] = match.group(1).strip()
            break
    
    # Extract manufacturer
    if "FANUC" in content[:2000]:
        metadata["manufacturer"] = "FANUC"
    elif "Siemens" in content[:2000]:
        metadata["manufacturer"] = "Siemens"
    
    # Extract manual ID (e.g., "B-70254EN/01")
    manual_id_match = re.search(r'([A-Z]-\d{5}[A-Z]{2}(?:/\d{2})?)', content[:2000])
    if manual_id_match:
        metadata["manual_id"] = manual_id_match.group(1)
    
    # Determine manual type
    content_lower = content[:3000].lower()
    if "operator" in content_lower:
        metadata["manual_type"] = "Operator's Manual"
    elif "maintenance" in content_lower:
        metadata["manual_type"] = "Maintenance Manual"
    elif "service" in content_lower:
        metadata["manual_type"] = "Service Manual"
    
    return metadata


def extract_fault_codes(content: str) -> List[Dict]:
    """
    Extract fault codes and their fixing instructions.
    
    Args:
        content: Markdown content
        
    Returns:
        List of fault dictionaries
    """
    faults = []
    
    # Pattern 1: Error/Fault Code with description
    # Examples: "Error Code 4085", "Fault: 123", "Alarm No. 456"
    pattern1 = re.compile(
        r'(?:Error|Fault|Alarm)\s*(?:Code|No\.?|Number)?\s*[:\-\.]?\s*(\w+)\s*[:\-\.]?\s*(.+?)(?:\n|$)',
        re.IGNORECASE
    )
    
    for match in pattern1.finditer(content):
        code = match.group(1).strip()
        description = match.group(2).strip()
        
        # Try to find fixing instructions nearby (next 500 chars)
        start_pos = match.end()
        context = content[start_pos:start_pos + 500]
        
        # Look for action words
        action_match = re.search(
            r'(?:Action|Solution|Fix|Remedy|Procedure)[:\-\.]?\s*(.+?)(?:\n\n|$)',
            context,
            re.IGNORECASE | re.DOTALL
        )
        
        fixing_instruction = action_match.group(1).strip() if action_match else None
        
        faults.append({
            "code": code,
            "description": description,
            "fixing_instruction": fixing_instruction,
            "extraction_method": "pattern_match"
        })
    
    # Pattern 2: Table-based fault codes
    # Look for markdown tables with fault/error columns
    table_pattern = re.compile(
        r'\|[^\n]*(?:Code|Fault|Error|Alarm)[^\n]*\|[^\n]*\n'  # Header
        r'\|[\-\s\|]+\n'  # Separator
        r'((?:\|[^\n]+\n)+)',  # Rows
        re.IGNORECASE
    )
    
    for table_match in table_pattern.finditer(content):
        rows = table_match.group(1).strip().split('\n')
        
        for row in rows:
            cells = [cell.strip() for cell in row.split('|') if cell.strip()]
            
            if len(cells) >= 2:
                # Assume first cell is code, second is description
                # Third might be action/fix
                fault = {
                    "code": cells[0],
                    "description": cells[1] if len(cells) > 1 else "",
                    "fixing_instruction": cells[2] if len(cells) > 2 else None,
                    "extraction_method": "table_extraction"
                }
                
                # Only add if code looks like a fault code (has numbers)
                if re.search(r'\d', fault["code"]):
                    faults.append(fault)
    
    return faults


def extract_maintenance_procedures(content: str) -> List[Dict]:
    """
    Extract maintenance procedures and schedules.
    
    Args:
        content: Markdown content
        
    Returns:
        List of maintenance procedure dictionaries
    """
    procedures = []
    
    # Look for maintenance sections
    maintenance_sections = re.finditer(
        r'##\s+(?:MAINTENANCE|PERIODIC\s+MAINTENANCE|DAILY\s+INSPECTION).*?\n(.*?)(?=\n##|\Z)',
        content,
        re.IGNORECASE | re.DOTALL
    )
    
    for section in maintenance_sections:
        section_content = section.group(1)
        
        # Extract table-based maintenance items
        table_pattern = re.compile(
            r'\|[^\n]*(?:Item|Procedure|Task)[^\n]*\|[^\n]*\n'
            r'\|[\-\s\|]+\n'
            r'((?:\|[^\n]+\n)+)',
            re.IGNORECASE
        )
        
        for table_match in table_pattern.finditer(section_content):
            rows = table_match.group(1).strip().split('\n')
            
            for row in rows:
                cells = [cell.strip() for cell in row.split('|') if cell.strip()]
                
                if len(cells) >= 2:
                    procedures.append({
                        "item": cells[0],
                        "period": cells[1] if len(cells) > 1 else None,
                        "description": cells[2] if len(cells) > 2 else None,
                    })
    
    return procedures


def extract_all(markdown_path: Path) -> Dict:
    """
    Extract all information from a markdown manual.
    
    Args:
        markdown_path: Path to markdown file
        
    Returns:
        Dictionary with all extracted information
    """
    logger.info(f"Extracting from: {markdown_path.name}")
    
    # Read markdown
    with open(markdown_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract metadata
    logger.info("Extracting metadata...")
    metadata = extract_metadata(content)
    logger.info(f"  Model: {metadata.get('model', 'Unknown')}")
    logger.info(f"  Manufacturer: {metadata.get('manufacturer', 'Unknown')}")
    
    # Extract fault codes
    logger.info("Extracting fault codes...")
    faults = extract_fault_codes(content)
    logger.info(f"  Found {len(faults)} fault codes")
    
    # Extract maintenance procedures
    logger.info("Extracting maintenance procedures...")
    maintenance = extract_maintenance_procedures(content)
    logger.info(f"  Found {len(maintenance)} maintenance items")
    
    # Combine all
    result = {
        "source_file": markdown_path.name,
        "metadata": metadata,
        "fault_codes": faults,
        "maintenance_procedures": maintenance,
        "extraction_stats": {
            "total_faults": len(faults),
            "total_maintenance_items": len(maintenance),
            "content_length": len(content)
        }
    }
    
    return result


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    # Parse arguments
    markdown_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("data/extracted") / f"{markdown_path.stem}_extracted.json"
    
    # Validate input
    if not markdown_path.exists():
        logger.error(f"Markdown file not found: {markdown_path}")
        sys.exit(1)
    
    # Process
    try:
        result = extract_all(markdown_path)
        
        # Save to JSON
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        
        logger.info(f"\n✓ SUCCESS: Extracted data saved to {output_path}")
        logger.info(f"  Fault codes: {result['extraction_stats']['total_faults']}")
        logger.info(f"  Maintenance items: {result['extraction_stats']['total_maintenance_items']}")
        
    except Exception as e:
        logger.error(f"\n✗ FAILED: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
