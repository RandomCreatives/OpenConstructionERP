"""Module manifest for oe_ethiopia_pack."""

from app.core.module_loader import ModuleManifest

manifest = ModuleManifest(
    name="oe_ethiopia_pack",
    version="1.0.0",
    display_name="Regional Pack — Ethiopia",
    description=(
        "Ethiopian construction standards: MoWUD Standard Technical Specifications, "
        "ETB currency, metric units, and Ethiopian VAT rules."
    ),
    author="RandomCreatives / DigitalMehandis",
    category="regional",
    depends=[],
    auto_install=False,
    enabled=True,
)
