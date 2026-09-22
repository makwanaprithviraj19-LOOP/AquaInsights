"""
AquaInsights Helper Utilities
Shared helper functions used across the application.
"""

import streamlit as st
from typing import Optional


def get_page_info(page_name: str) -> dict:
    """Retrieve the title, subtitle, and emoji for a given page name."""
    from utils.constants import NAV_ITEMS

    for item in NAV_ITEMS:
        if item["label"] == page_name:
            return {
                "title": item["title"],
                "subtitle": item["subtitle"],
                "emoji": item.get("emoji", "📄"),
            }
    return {"title": page_name, "subtitle": "", "emoji": "📄"}


def init_session_state() -> None:
    """Initialise all session-state keys with safe defaults."""
    defaults: dict = {
        "selected_page": "Dashboard",
        "dataset": None,
        "dataset_name": None,
        "dataset_uploaded_at": None,
        "dark_mode": False,
        "notifications": [],
        # ── Auth & navigation flow ───────────────────────────────
        "splash_shown": False,
        "logged_in": False,
        "app_view": "home",
        "user_email": None,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def format_number(value: float, decimals: int = 2) -> str:
    """Format a number with K / M suffixes for readability."""
    if abs(value) >= 1_000_000:
        return f"{value / 1_000_000:.{decimals}f}M"
    if abs(value) >= 1_000:
        return f"{value / 1_000:.{decimals}f}K"
    return f"{value:,.{decimals}f}"


def render_page_placeholder(page_label: str) -> None:
    """Render a styled empty-state placeholder for pages not yet implemented."""
    info = get_page_info(page_label)
    st.markdown(
        f"""
        <div class="page-placeholder">
            <div class="placeholder-icon">{info["emoji"]}</div>
            <div class="placeholder-title">{info["title"]}</div>
            <div class="placeholder-text">
                {info["subtitle"]}.<br/>
                This section will be available in a future update.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
