"""
AquaInsights — Public Top Navigation Bar
Horizontal navigation for public-facing pages (Home, About, Contact, Dashboard).
"""

import streamlit as st
from streamlit_option_menu import option_menu
from utils.colors import Colors


def render_public_navbar() -> str:
    """Render the public-facing horizontal navigation bar. Returns selected label."""

    st.markdown(_navbar_css(), unsafe_allow_html=True)

    # ── Logo + Nav Row ────────────────────────────────────────────────────
    logo_col, nav_col, action_col = st.columns([1.5, 3.2, 1.3])

    with logo_col:
        st.markdown(
            """<div class="pub-logo" style="display:flex; align-items:center; gap:10px; padding:4px 0;">
<div style="width:36px; height:36px; border-radius:10px; background:linear-gradient(135deg,#1E88E5,#42A5F5); display:flex; align-items:center; justify-content:center; box-shadow:0 4px 12px rgba(30,136,229,0.35);">
<svg width="20" height="20" viewBox="0 0 24 24" fill="white">
<path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0L12 2.69z"/>
</svg>
</div>
<span style="font-family:'Poppins',sans-serif; font-size:18px; font-weight:700; color:#14213D; letter-spacing:.3px;">
<span style="color:#1E88E5;">Aqua</span>Insights
</span>
</div>""",
            unsafe_allow_html=True,
        )

    # Active tab mapping
    current_view = st.session_state.get("app_view", "home")
    view_map = {"home": 0, "about": 1, "contact": 2, "dashboard": 3}
    default_idx = view_map.get(current_view, 0)

    with nav_col:
        selected = option_menu(
            menu_title=None,
            options=["Home", "About Us", "Contact Us", "Dashboard"],
            icons=["house-door", "info-circle", "envelope", "speedometer2"],
            default_index=default_idx,
            orientation="horizontal",
            key="public_nav_menu_main",
            styles={
                "container": {
                    "padding": "0 !important",
                    "background": "transparent !important",
                },
                "icon": {"font-size": "14px", "color": "#6B7280"},
                "nav-link": {
                    "font-family": "'Inter', sans-serif",
                    "font-size": "14px",
                    "padding": "8px 18px",
                    "border-radius": "8px",
                    "color": "#374151",
                    "--hover-color": "rgba(30,136,229,0.06)",
                    "margin": "0 2px",
                },
                "nav-link-selected": {
                    "background-color": Colors.PRIMARY_BLUE,
                    "color": "#FFFFFF",
                    "font-weight": "600",
                },
            },
        )

    with action_col:
        bc1, bc2 = st.columns(2)
        with bc1:
            if st.session_state.get("logged_in"):
                if st.button("Logout", key="pub_nav_logout", use_container_width=True):
                    for k in ("logged_in", "user_email", "app_view"):
                        st.session_state[k] = {"logged_in": False, "user_email": None, "app_view": "home"}[k]
                    st.rerun()
        with bc2:
            if not st.session_state.get("logged_in"):
                if st.button("Login", key="pub_nav_login_btn", type="primary", use_container_width=True):
                    st.session_state["app_view"] = "login"
                    st.rerun()

    # ── Handle selection ──────────────────────────────────────────────────
    if selected == "Dashboard" and current_view != "dashboard":
        st.session_state["app_view"] = "dashboard"
        st.rerun()
    elif selected == "Home" and current_view != "home":
        st.session_state["app_view"] = "home"
        st.rerun()
    elif selected == "About Us" and current_view != "about":
        st.session_state["app_view"] = "about"
        st.rerun()
    elif selected == "Contact Us" and current_view != "contact":
        st.session_state["app_view"] = "contact"
        st.rerun()

    st.markdown('<div style="border-bottom:1px solid #E5E5E5; margin-bottom:16px;"></div>', unsafe_allow_html=True)

    return selected


def _navbar_css() -> str:
    return """<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');
</style>"""
