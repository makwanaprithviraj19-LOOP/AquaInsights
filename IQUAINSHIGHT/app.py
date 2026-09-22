"""
AquaInsights — Water Quality Analytics Platform
Main application entry point.

Flow:  Splash → Login → Dashboard (Analytics Workspace)

Run with:  streamlit run app.py
"""

import streamlit as st

from utils.constants import PAGE_CONFIG
from utils.theme import inject_custom_css
from utils.helpers import init_session_state, get_page_info

# ── Page configuration (must be first Streamlit call) ────────────────────
st.set_page_config(**PAGE_CONFIG)

# ── Initialisation ───────────────────────────────────────────────────────
init_session_state()


# ═════════════════════════════════════════════════════════════════════════
# PHASE 1 — SPLASH SCREEN  (one-time, auto-advances)
# ═════════════════════════════════════════════════════════════════════════
if not st.session_state.get("splash_shown", False):
    from pages import splash
    splash.render()
    st.stop()


# ═════════════════════════════════════════════════════════════════════════
# PHASE 2 — LOGIN  (blocks until authenticated or guest)
# ═════════════════════════════════════════════════════════════════════════
if not st.session_state.get("logged_in", False):
    from pages import login
    login.render()
    st.stop()


# ═════════════════════════════════════════════════════════════════════════
# PHASE 3 — DASHBOARD (Analytics Workspace)
# ═════════════════════════════════════════════════════════════════════════
inject_custom_css()

from components.sidebar import render_sidebar
from components.navbar import render_navbar
from components.footer import render_footer

from pages import (
    dashboard,
    dataset,
    cleaning,
    parameters,
    analytics,
    visualizations,
    insights,
    prediction,
    reports,
    settings,
    about,
    contact,
)

# Sidebar navigation
with st.sidebar:
    selected_page = render_sidebar()

# Top navigation bar
page_info = get_page_info(selected_page)
render_navbar(page_info["title"], page_info["subtitle"])

# Page routing
_PAGE_MAP: dict = {
    "Dashboard": dashboard,
    "Dataset Overview": dataset,
    "Data Cleaning": cleaning,
    "Water Parameters": parameters,
    "Analytics": analytics,
    "Visualizations": visualizations,
    "AI Insights": insights,
    "Prediction": prediction,
    "Reports": reports,
    "Settings": settings,
    "About Us": about,
    "Contact Us": contact,
}

page_module = _PAGE_MAP.get(selected_page)
if page_module:
    page_module.render()

# Footer
render_footer()
