# Ethiopia Customization Guide for OpenConstructionERP

This guide explains how to customize OpenConstructionERP for the Ethiopian context, integrating it with your automated quantity surveying tools and local standards.

---

## 1. Project Architecture Overview

OpenConstructionERP is built with a highly modular architecture, allowing you to add features (like an Ethiopia-specific regional pack) without modifying the core system.

### Backend (Python/FastAPI)
- **Modular Core**: Located in `backend/app/modules/`. Each subdirectory is a self-contained module.
- **Auto-Discovery**: The system automatically detects and loads modules that have a `manifest.py` file.
- **Data Layer**: Uses SQLAlchemy for ORM (PostgreSQL in production, SQLite for dev).
- **AI Integration**: Pluggable AI engine supporting multiple LLM providers (OpenAI, Anthropic, etc.) for estimation and chat.

### Frontend (React/TypeScript)
- **Vite-powered SPA**: Fast builds and HMR.
- **AG Grid**: Used for high-performance BOQ and data management.
- **Module Registry**: Modules are registered in `frontend/src/modules/_registry.ts`.
- **i18n**: Multi-language support using `i18next`.

### CAD/BIM Pipeline
- **DDC cad2data**: Converts proprietary formats (RVT, IFC, DWG, DGN) into a canonical JSON format.
- **Quantity Extraction**: Extracts volumes, areas, lengths, and counts automatically.

---

## 2. Creating the "Ethiopia Pack" (oe_ethiopia_pack)

To localize the platform, you will create a new regional module.

### Step 1: Scaffold the Backend Module
1. Create a directory: `backend/app/modules/ethiopia_pack/`
2. Create `manifest.py`:
```python
from app.core.module_loader import ModuleManifest

manifest = ModuleManifest(
    name="oe_ethiopia_pack",
    version="1.0.0",
    display_name="Regional Pack — Ethiopia",
    description="Ethiopian construction standards (MoWUD), ETB currency, and local cost data.",
    author="Your Name/DigitalMehandis",
    category="regional",
    depends=[],
    auto_install=False,
    enabled=True,
)
```
3. Create `config.py` to define local standards:
```python
PACK_CONFIG = {
    "region_code": "ET",
    "countries": ["ET"],
    "default_currency": "ETB",
    "default_locale": "en-ET",
    "measurement_system": "metric",
    "standards": [
        {
            "code": "MoWUD",
            "name": "MoWUD Standard Technical Specifications",
            "description": "Ministry of Works and Urban Development standards for Ethiopia",
            "divisions": [
                {"number": "01", "title": "General Requirements"},
                {"number": "02", "title": "Earthwork"},
                # Add your specific divisions here
            ],
        }
    ],
    "default_units": {
        "length": "m",
        "area": "m2",
        "volume": "m3",
        "weight": "kg",
    },
}
```

### Step 2: Import Ethiopian Cost Data
1. Prepare your data in CSV format following the CWICR structure.
2. Place your files in `data/catalog/regions/`:
   - `DDC_CWICR_ETB_ETHIOPIA_Catalog.csv`
3. Use the `openestimate` CLI or the UI to import the catalog into the system.

### Step 3: Integrating Your CAD Logic
Since you want to use the OpenConstructionERP approach:
1. **Upload**: Use the existing file upload system.
2. **Convert**: The system uses `DDC cad2data`. It supports:
   - **Revit (.rvt)** and **IFC** for BIM.
   - **AutoCAD (.dwg)** and **MicroStation (.dgn)** for 2D/3D CAD.
3. **Map**: Link extracted quantities to your MoWUD-based BOQ items. In the UI, you can use the **BIM Quantity Picker** to drag quantities directly into your estimate.

### Step 4: AI-Powered Estimation for Ethiopia
You can leverage the AI engine to speed up the process:
1. **Configure LLM**: Add your API key (e.g., Anthropic or OpenAI) in the settings.
2. **AI Cost Advisor**: Once your Ethiopian cost database is imported, you can ask the AI: *"What is the current rate for C-25 concrete in Addis Ababa?"*
3. **Photo to Estimate**: Upload a site photo, and the AI will attempt to generate a preliminary BOQ based on recognized elements, which you can then match to your MoWUD items.

---

## 3. Customizing the UI
1. Add Ethiopian Birr (ETB) if not already fully configured in `frontend/src/features/settings/RegionalSettings.tsx`.
2. Create a frontend module in `frontend/src/modules/ethiopia-pack/` if you need custom Ethiopian dashboard widgets or reporting templates.

---

## 4. Deployment for SaaS (Ethiopian Context)
- **Docker**: Use the provided `docker-compose.yml`.
- **Database**: Ensure PostgreSQL is used for multi-user stability.
- **Environment Variables**:
  - `CURRENCY_DEFAULT=ETB`
  - `LOCALE_DEFAULT=en-ET`
- **Security**: Update `JWT_SECRET` and set up HTTPS.

---

## 5. Next Steps
- Clone the repository.
- Follow the **Local Development** guide in `README.md`.
- Start by creating the `ethiopia_pack` backend module.
- Reach out on the [Telegram community](https://t.me/datadrivenconstruction) for architecture-level questions.
