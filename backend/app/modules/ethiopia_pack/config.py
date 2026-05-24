"""Regional configuration for Ethiopia."""

from typing import Any

PACK_CONFIG: dict[str, Any] = {
    # ── Identity ─────────────────────────────────────────────────────────────
    "region_code": "ET",
    "countries": ["ET"],
    "default_currency": "ETB",
    "default_locale": "en-ET",
    "measurement_system": "metric",
    "paper_size": "A4",
    "date_format": "DD/MM/YYYY",
    "number_format": "1,234.56",
    # ── Standards ────────────────────────────────────────────────────────────
    "standards": [
        {
            "code": "MoWUD",
            "name": "MoWUD Standard Technical Specifications",
            "description": "Ministry of Works and Urban Development standards for Ethiopia",
            "divisions": [
                {"number": "01", "title": "General Requirements"},
                {"number": "02", "title": "Earthwork"},
                {"number": "03", "title": "Concrete Work"},
                {"number": "04", "title": "Masonry Work"},
                {"number": "05", "title": "Carpentry and Joinery"},
                {"number": "06", "title": "Roofing and Waterproofing"},
                {"number": "07", "title": "Glazing and Metal Work"},
                {"number": "08", "title": "Finishing Work"},
                {"number": "09", "title": "Sanitary and Plumbing"},
                {"number": "10", "title": "Electrical Installation"},
            ],
        },
    ],
    # ── Contract types ───────────────────────────────────────────────────────
    "contract_types": [
        {
            "code": "MoWUD_GCC",
            "name": "MoWUD General Conditions of Contract",
            "description": "Standard conditions of contract for construction of civil work projects",
        },
        {
            "code": "FIDIC_ET",
            "name": "FIDIC (Ethiopian Adaptation)",
            "description": "FIDIC contracts adapted for Ethiopian infrastructure projects",
        },
    ],
    # ── Tax rules (Ethiopia VAT 15%) ─────────────────────────────────────────
    "tax_rules": [
        {
            "code": "ET_VAT",
            "name": "Value Added Tax (VAT)",
            "type": "vat",
            "rate_pct": "15",
            "description": "Standard Ethiopian VAT applied to goods and services",
        },
        {
            "code": "ET_WITHHOLDING",
            "name": "Withholding Tax",
            "type": "withholding",
            "rate_pct": "2",
            "description": "Withholding tax on payments for goods and services",
        },
    ],
    # ── Cost database references ─────────────────────────────────────────────
    "cost_database_references": [
        {
            "code": "MoWUD_DSR",
            "name": "MoWUD — Detailed Schedule of Rates",
            "description": "Standard rates for Ethiopian construction projects (Building/Road)",
            "file_reference": "DDC_CWICR_ETB_ETHIOPIA_Catalog.csv",
        },
    ],
    # ── Units (metric defaults) ──────────────────────────────────────────────
    "default_units": {
        "length": "m",
        "area": "m²",
        "volume": "m³",
        "weight": "kg",
        "temperature": "°C",
    },
}
