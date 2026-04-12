# config.py
# Central configuration for P04 — UK House Price Dynamics
# All file paths and project parameters defined here.
# Import this module at the top of every notebook.

import os

# ── Project root ──────────────────────────────────────────────────────────────
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# ── Directory paths ───────────────────────────────────────────────────────────
DATA_RAW        = os.path.join(PROJECT_ROOT, "data", "raw")
DATA_PROCESSED  = os.path.join(PROJECT_ROOT, "data", "processed")
FIGURES_DIR     = os.path.join(PROJECT_ROOT, "figures")
REPORTS_DIR     = os.path.join(PROJECT_ROOT, "reports")
SRC_DIR         = os.path.join(PROJECT_ROOT, "src")

# ── Raw input files ───────────────────────────────────────────────────────────
PPD_2024        = os.path.join(DATA_RAW, "pp-2024.csv")
HPSSA_LA        = os.path.join(DATA_RAW, "hpssa_la.csv")
ONSPD_SUBSET    = os.path.join(DATA_RAW, "onspd_subset.csv")
ASHE_EARNINGS   = os.path.join(DATA_RAW, "ashe_la_earnings.csv")
IMD_FILE        = os.path.join(DATA_RAW, "File_7_-_All_IoD2019_Scores__Ranks__Deciles_and_Population_Denominators_3.csv")

# ── Processed output files ────────────────────────────────────────────────────
HOUSE_PRICES_FINAL = os.path.join(DATA_PROCESSED, "house_prices_final.csv")

# ── Figure output paths ───────────────────────────────────────────────────────
FIG_AFFORDABILITY_BAR   = os.path.join(FIGURES_DIR, "01_affordability_ratio_bar.png")
FIG_REGIONAL_BOX        = os.path.join(FIGURES_DIR, "02_regional_affordability.png")
FIG_PROPERTY_TYPE       = os.path.join(FIGURES_DIR, "03_property_type_prices.png")
FIG_PRICE_SURGE         = os.path.join(FIGURES_DIR, "04_price_surge_regions.png")
FIG_DEPRIVATION_SCATTER = os.path.join(FIGURES_DIR, "05_deprivation_vs_affordability.png")

# ── ONS ArcGIS — LAD to region lookup (reused from P02/P03) ──────────────────
LAD_REGION_URL = (
    "https://services1.arcgis.com/ESMARspQHYMw9BZ9/arcgis/rest/services/"
    "LAD24_RGN24_EN_LU/FeatureServer/0/query"
    "?where=1%3D1&outFields=LAD24CD,LAD24NM,RGN24CD,RGN24NM"
    "&f=json&resultRecordCount=400"
)

# ── Price Paid Data parameters ────────────────────────────────────────────────
PPD_COLUMNS = [
    "transaction_id", "price", "date_of_transfer", "postcode",
    "property_type", "new_build", "tenure", "paon", "saon",
    "street", "locality", "town_city", "district", "county",
    "ppd_category", "record_status"
]
PPD_KEEP_COLUMNS = [
    "transaction_id", "price", "date_of_transfer", "postcode",
    "property_type", "new_build", "tenure", "town_city", "district",
    "ppd_category"
]
PPD_CHUNK_SIZE  = 100_000
PPD_CATEGORY_A  = "A"

PROPERTY_TYPE_LABELS = {
    "D": "Detached",
    "S": "Semi-Detached",
    "T": "Terraced",
    "F": "Flat / Maisonette",
    "O": "Other"
}

# ── Analysis parameters ───────────────────────────────────────────────────────
FIGURE_DPI      = 300
RANDOM_STATE    = 42
ENGLAND_REGIONS = [
    "East Midlands", "East of England", "London",
    "North East", "North West", "South East",
    "South West", "West Midlands", "Yorkshire and The Humber"
]