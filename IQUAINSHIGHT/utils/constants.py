"""
AquaInsights Application Constants
Centralized configuration and constant definitions.
"""

APP_NAME = "AquaInsights"
APP_TAGLINE = "Every Drop. Every Insight. Every Decision."
APP_VERSION = "1.0"
APP_YEAR = "2026"

# ── Streamlit Page Configuration ─────────────────────────────────────────
PAGE_CONFIG: dict = {
    "page_title": "AquaInsights | Water Quality Analytics",
    "page_icon": "💧",
    "layout": "wide",
    "initial_sidebar_state": "expanded",
}

# ── Navigation Items ─────────────────────────────────────────────────────
# Defines sidebar menu items with icon, page title, subtitle, and placeholder emoji.
NAV_ITEMS: list[dict] = [
    {
        "label": "Dashboard",
        "icon": "speedometer2",
        "title": "Analytics Workspace",
        "subtitle": "Overview of your water quality analysis",
        "emoji": "📊",
    },
    {
        "label": "Dataset Overview",
        "icon": "table",
        "title": "Dataset Overview",
        "subtitle": "Explore and analyze your uploaded datasets",
        "emoji": "📋",
    },
    {
        "label": "Data Cleaning",
        "icon": "funnel",
        "title": "Data Cleaning",
        "subtitle": "Clean and prepare your dataset",
        "emoji": "🧹",
    },
    {
        "label": "Water Parameters",
        "icon": "droplet-half",
        "title": "Water Parameters",
        "subtitle": "Explore individual water quality parameters",
        "emoji": "💧",
    },
    {
        "label": "Analytics",
        "icon": "bar-chart-line",
        "title": "Analytics",
        "subtitle": "Statistical analysis of your dataset",
        "emoji": "📈",
    },
    {
        "label": "Visualizations",
        "icon": "pie-chart",
        "title": "Visualizations",
        "subtitle": "Interactive data visualizations",
        "emoji": "📉",
    },
    {
        "label": "AI Insights",
        "icon": "stars",
        "title": "AI Insights",
        "subtitle": "AI-powered insights about your dataset",
        "emoji": "✨",
    },
    {
        "label": "Prediction",
        "icon": "cpu",
        "title": "Prediction",
        "subtitle": "Water potability prediction model",
        "emoji": "🎯",
    },
    {
        "label": "Reports",
        "icon": "file-earmark-text",
        "title": "Report Generator",
        "subtitle": "Create and download executive reports",
        "emoji": "📄",
    },
    {
        "label": "Settings",
        "icon": "gear",
        "title": "Settings",
        "subtitle": "Configure platform preferences",
        "emoji": "⚙️",
    },
    {
        "label": "About Us",
        "icon": "info-circle",
        "title": "About AquaInsights",
        "subtitle": "Mission, vision, technology stack, and roadmap",
        "emoji": "ℹ️",
    },
    {
        "label": "Contact Us",
        "icon": "envelope",
        "title": "Contact Us",
        "subtitle": "Get in touch with the AquaInsights team",
        "emoji": "✉️",
    },
]

# ── File Upload ──────────────────────────────────────────────────────────
SUPPORTED_FILE_TYPES: list[str] = ["csv", "xlsx", "xls"]
MAX_FILE_SIZE_MB: int = 50

# ── Water Quality Parameters ─────────────────────────────────────────────
WATER_PARAMETERS: list[str] = [
    "pH",
    "Hardness",
    "Solids (TDS)",
    "Chloramines",
    "Sulfate",
    "Conductivity",
    "Organic Carbon",
    "Trihalomethanes",
    "Turbidity",
    "Potability",
]
