import csv
import re
import sys

def clean_unit(unit_str):
    """Clean common OCR errors in units."""
    unit_str = unit_str.strip().lower()
    if unit_str in ['m’', 'm3', 'm\'', '7', 'm7']:
        return 'm3'
    if unit_str in ['m?', 'm2', 'm²', 'e']:
        return 'm2'
    return unit_str

def parse_mowud_line(line):
    """
    Parse a line like: 1.2.33 |10cm thick HCB Structure m’ 112.61
    Returns a dict for the CSV.
    """
    # Clean up the line
    line = line.strip()
    if not line: return None

    # Regex to match: code | description unit price
    # Improved regex to handle cases where unit might be a single char or symbol
    # Code: ([\d\.]+)
    # Separator: \s*\|?\s*
    # Description: (.*?)
    # Unit: \s+([a-zA-Z\’\?\'\d\²³\.]+|[e\.])
    # Price: \s+([\d,]+\.?\d*)
    match = re.search(r'^([\d\.]+)\s*\|?\s*(.*?)\s+([a-zA-Z\’\?\'\d\²³\.]+|[e\.])\s+([\d,]+\.?\d*)$', line)

    if not match:
        # Fallback for lines without clear unit column (some OCR might skip it)
        match = re.search(r'^([\d\.]+)\s*\|?\s*(.*?)\s+([\d,]+\.?\d*)$', line)
        if not match: return None
        code, desc, price = match.groups()
        unit = "unit"
    else:
        code, desc, unit, price = match.groups()

    code, desc, unit, price = match.groups()
    price = price.replace(',', '')

    return {
        "resource_code": f"ET_MOWUD_{code.replace('.', '_')}",
        "name": desc.strip(),
        "type": "Material", # Default to material for these items
        "category": "Construction",
        "unit": clean_unit(unit),
        "price_avg": price,
        "price_min": price,
        "price_max": price,
        "price_median": price,
        "price_variants": "1",
        "currency": "ETB",
        "avg_cost_per_use": "0",
        "avg_qty_per_use": "0",
        "usage_count": "0",
        "used_in_work_items": "0",
        "parent_category": "MoWUD",
        "parent_collection": "Ethiopian Standards",
        "parent_department": "Building Construction",
        "parent_section": "General"
    }

def convert_text_to_csv(input_text, output_file):
    lines = input_text.strip().split('\n')
    results = []

    for line in lines:
        parsed = parse_mowud_line(line)
        if parsed:
            results.append(parsed)

    if not results:
        print("No items parsed. Check the input format.")
        return

    keys = results[0].keys()
    with open(output_file, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        # We assume headers are already there from the previous step
        writer.writerows(results)

    print(f"Successfully added {len(results)} items to {output_file}")

if __name__ == "__main__":
    # Sample data for testing
    sample = """
1.2.33 |10cm thick HCB Structure m’ 112.61
1.2.34 |15cm thick HCB Structure m? 123.75
1.2.35 |20cm thick HCB Structure 7 173.25
1.2.36 |Terrazzo floor . 192.50
1.2.37 |Cement screed floor e 43.31
"""
    convert_text_to_csv(sample, 'data/catalog/regions/DDC_CWICR_ETB_ETHIOPIA_Catalog.csv')
