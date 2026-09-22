"""
AquaInsights Theme Configuration
Complete custom CSS for styling the Streamlit application to match the
approved reference designs.  All colour tokens are imported from
utils.colors to guarantee a single source of truth.
"""

import streamlit as st
from utils.colors import Colors


# ═════════════════════════════════════════════════════════════════════════
# PUBLIC API
# ═════════════════════════════════════════════════════════════════════════

def inject_custom_css() -> None:
    """Inject every CSS layer into the Streamlit page (call once in app.py)."""
    st.markdown(_font_imports(), unsafe_allow_html=True)
    st.markdown(_global_styles(), unsafe_allow_html=True)
    st.markdown(_sidebar_styles(), unsafe_allow_html=True)
    st.markdown(_navbar_styles(), unsafe_allow_html=True)
    st.markdown(_card_styles(), unsafe_allow_html=True)
    st.markdown(_footer_styles(), unsafe_allow_html=True)
    st.markdown(_component_styles(), unsafe_allow_html=True)
    st.markdown(_layout_responsive_styles(), unsafe_allow_html=True)


def inject_base_css() -> None:
    """Inject fonts + global styles for splash/login (no sidebar needed)."""
    st.markdown(_font_imports(), unsafe_allow_html=True)
    st.markdown(_global_styles(), unsafe_allow_html=True)
    st.markdown(_card_styles(), unsafe_allow_html=True)


def get_sidebar_menu_styles() -> dict:
    """Return the *styles* dict consumed by streamlit-option-menu."""
    return {
        "container": {
            "padding": "4px 0 !important",
            "background-color": "transparent !important",
        },
        "icon": {
            "color": "#9CA3AF",
            "font-size": "16px",
        },
        "nav-link": {
            "font-family": "'Inter', sans-serif",
            "font-size": "14px",
            "text-align": "left",
            "margin": "2px 12px",
            "padding": "10px 16px",
            "border-radius": "8px",
            "color": "#CBD5E1",
            "--hover-color": "rgba(255, 255, 255, 0.06)",
        },
        "nav-link-selected": {
            "background-color": Colors.PRIMARY_BLUE,
            "color": "#FFFFFF",
            "font-weight": "600",
        },
    }


# ═════════════════════════════════════════════════════════════════════════
# PRIVATE – CSS LAYERS
# ═════════════════════════════════════════════════════════════════════════

def _font_imports() -> str:
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');
    </style>
    """


def _global_styles() -> str:
    return f"""
    <style>
        /* ── Global ─────────────────────────────────────────────── */
        .stApp {{
            background-color: {Colors.BACKGROUND};
            font-family: 'Inter', 'Poppins', -apple-system, BlinkMacSystemFont, sans-serif;
        }}

        /* Hide Streamlit chrome & default multipage navigation */
        #MainMenu  {{ visibility: hidden !important; }}
        footer     {{ visibility: hidden !important; }}
        [data-testid="stHeader"], header[data-testid="stHeader"] {{
            display: none !important;
            height: 0px !important;
            min-height: 0px !important;
            padding: 0 !important;
            margin: 0 !important;
        }}
        [data-testid="stSidebarNav"],
        [data-testid="stSidebarNavItems"],
        nav[data-testid="stSidebarNav"] {{
            display: none !important;
        }}

        /* Lock sidebar open — hide the collapse toggle */
        [data-testid="stSidebarCollapseButton"],
        button[data-testid="baseButton-headerNoPadding"],
        [data-testid="collapsedControl"] {{
            display: none !important;
        }}

        /* ── Typography overrides — design system headings ────────── */
        .main .block-container h1 {{
            font-family: 'Poppins', sans-serif !important;
            font-size: 26px !important;
            font-weight: 700 !important;
            color: {Colors.TEXT_PRIMARY} !important;
            margin-bottom: 0.5rem !important;
        }}
        .main .block-container h2 {{
            font-family: 'Poppins', sans-serif !important;
            font-size: 20px !important;
            font-weight: 700 !important;
            color: {Colors.TEXT_PRIMARY} !important;
            margin-bottom: 0.4rem !important;
        }}
        .main .block-container h3 {{
            font-family: 'Poppins', sans-serif !important;
            font-size: 15px !important;
            font-weight: 600 !important;
            color: {Colors.TEXT_PRIMARY} !important;
            margin-bottom: 0.5rem !important;
        }}

        /* Primary button styling */
        .stButton > button[kind="primary"] {{
            background: {Colors.PRIMARY_BLUE} !important;
            color: #ffffff !important;
            border: none !important;
            font-family: 'Inter', sans-serif !important;
            font-weight: 600 !important;
            border-radius: 8px !important;
            transition: all 0.2s ease !important;
        }}
        .stButton > button[kind="primary"]:hover {{
            background: {Colors.SECONDARY_BLUE} !important;
            box-shadow: 0 4px 12px rgba(30, 136, 229, 0.3) !important;
        }}

        /* Force readable text on light backgrounds */
        .main .block-container,
        .main .block-container p,
        .main .block-container span,
        .main .block-container label,
        .main .block-container h1,
        .main .block-container h2,
        .main .block-container h3,
        .main .block-container li {{
            color: {Colors.TEXT_PRIMARY};
        }}
        .main .block-container .stCaption,
        .main .block-container small {{
            color: {Colors.TEXT_SECONDARY} !important;
        }}

        /* Scrollbar */
        ::-webkit-scrollbar       {{ width: 6px; height: 6px; }}
        ::-webkit-scrollbar-track {{ background: transparent; }}
        ::-webkit-scrollbar-thumb {{ background: {Colors.BORDER}; border-radius: 3px; }}
        ::-webkit-scrollbar-thumb:hover {{ background: {Colors.TEXT_SECONDARY}; }}

        /* Main content area — ~28px below navbar */
        .main .block-container {{
            padding-top: 1.75rem !important;
            padding-bottom: 1rem !important;
            padding-left: 1.75rem !important;
            padding-right: 1.75rem !important;
            max-width: 100% !important;
        }}
        section.main > div {{
            padding-top: 0 !important;
        }}

        /* Tighten vertical gap */
        div[data-testid="stVerticalBlock"] {{
            gap: 0.75rem !important;
        }}
        div[data-testid="stVerticalBlock"] > div:first-child {{
            margin-top: 0px !important;
            padding-top: 0px !important;
        }}

        /* Links */
        a {{ color: {Colors.PRIMARY_BLUE}; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
    </style>
    """


def _sidebar_styles() -> str:
    return f"""
    <style>
        /* ── Sidebar ────────────────────────────────────────────── */
        section[data-testid="stSidebar"] {{
            background: linear-gradient(180deg, {Colors.SIDEBAR} 0%, {Colors.SIDEBAR_DARK} 100%);
            min-width: 270px !important;
            max-width: 270px !important;
            box-shadow: 4px 0 24px rgba(0, 0, 0, 0.18);
        }}

        section[data-testid="stSidebar"] > div:first-child {{
            padding-top: 0;
            background: transparent;
        }}

        [data-testid="stSidebarContent"] {{
            padding: 0 !important;
        }}

        /* Text colours inside sidebar */
        section[data-testid="stSidebar"] .stMarkdown p,
        section[data-testid="stSidebar"] .stMarkdown span {{
            color: {Colors.TEXT_SIDEBAR} !important;
        }}

        section[data-testid="stSidebar"] hr {{
            border-color: {Colors.OVERLAY_BORDER};
            margin: 0.5rem 1rem;
        }}

        /* streamlit-option-menu overrides */
        section[data-testid="stSidebar"] .nav-link {{
            font-family: 'Inter', sans-serif !important;
            font-size: 14px !important;
            padding: 10px 16px !important;
            margin: 2px 12px !important;
            border-radius: 8px !important;
            color: {Colors.TEXT_SIDEBAR} !important;
            transition: all 0.2s ease !important;
        }}
        section[data-testid="stSidebar"] .nav-link:hover {{
            background-color: {Colors.OVERLAY_LIGHT} !important;
            color: {Colors.TEXT_WHITE} !important;
        }}
        section[data-testid="stSidebar"] .nav-link-selected {{
            background-color: {Colors.PRIMARY_BLUE} !important;
            color: {Colors.TEXT_WHITE} !important;
            font-weight: 600 !important;
            box-shadow: {Colors.SHADOW_BLUE} !important;
        }}
    </style>
    """


def _navbar_styles() -> str:
    return f"""
    <style>
        /* ── Top Navbar ─────────────────────────────────────────── */
        .aqua-navbar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 0 12px 0;
            margin-bottom: 8px;
            border-bottom: 1px solid {Colors.BORDER};
        }}
        .navbar-left {{
            display: flex;
            flex-direction: column;
        }}
        .navbar-title {{
            font-family: 'Poppins', sans-serif;
            font-size: 22px;
            font-weight: 700;
            color: {Colors.TEXT_PRIMARY} !important;
            margin: 0;
            line-height: 1.2;
        }}
        .navbar-subtitle {{
            font-family: 'Inter', sans-serif;
            font-size: 13px;
            color: {Colors.TEXT_SECONDARY} !important;
            margin: 2px 0 0 0;
        }}

        /* Right-side controls */
        .navbar-right {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        .navbar-search {{
            display: flex;
            align-items: center;
            background: {Colors.CARD};
            border: 1px solid {Colors.BORDER};
            border-radius: 10px;
            padding: 6px 14px;
            width: 250px;
            transition: border-color 0.2s ease, box-shadow 0.2s ease;
        }}
        .navbar-search:focus-within {{
            border-color: {Colors.PRIMARY_BLUE};
            box-shadow: 0 0 0 3px rgba(30, 136, 229, 0.1);
        }}
        .navbar-search input {{
            border: none;
            background: transparent;
            outline: none;
            font-family: 'Inter', sans-serif;
            font-size: 13px;
            color: {Colors.TEXT_PRIMARY};
            width: 100%;
            margin-left: 8px;
        }}
        .navbar-search input::placeholder {{ color: {Colors.TEXT_LIGHT}; }}

        /* Icon buttons */
        .nav-icon-btn {{
            width: 38px;
            height: 38px;
            border-radius: 10px;
            border: 1px solid {Colors.BORDER};
            background: {Colors.CARD};
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.2s ease;
            color: {Colors.TEXT_SECONDARY};
            font-size: 16px;
            position: relative;
        }}
        .nav-icon-btn:hover {{
            background: {Colors.BACKGROUND};
            border-color: {Colors.PRIMARY_BLUE};
            color: {Colors.PRIMARY_BLUE};
        }}
        .notification-dot {{
            position: absolute;
            top: 7px; right: 7px;
            width: 7px; height: 7px;
            background: {Colors.DANGER};
            border-radius: 50%;
            border: 2px solid {Colors.CARD};
        }}

        /* User profile chip */
        .user-profile {{
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 4px 10px 4px 4px;
            border-radius: 10px;
            border: 1px solid {Colors.BORDER};
            background: {Colors.CARD};
            cursor: pointer;
            transition: border-color 0.2s ease;
        }}
        .user-profile:hover {{ border-color: {Colors.PRIMARY_BLUE}; }}
        .user-avatar {{
            width: 32px; height: 32px;
            border-radius: 8px;
            background: {Colors.PRIMARY_BLUE};
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 600;
            font-size: 13px;
            font-family: 'Inter', sans-serif;
        }}
        .user-info {{ display: flex; flex-direction: column; }}
        .user-name {{
            font-family: 'Inter', sans-serif;
            font-size: 12px;
            font-weight: 600;
            color: {Colors.TEXT_PRIMARY} !important;
            line-height: 1.2;
        }}
        .user-role {{
            font-family: 'Inter', sans-serif;
            font-size: 10px;
            color: {Colors.TEXT_SECONDARY} !important;
        }}
    </style>
    """


def _card_styles() -> str:
    return f"""
    <style>
        /* ── Cards ──────────────────────────────────────────────── */
        .aqua-card {{
            background: {Colors.CARD} !important;
            border-radius: 16px !important;
            border: 1px solid {Colors.BORDER} !important;
            padding: 20px !important;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04) !important;
            transition: transform 0.2s ease, box-shadow 0.2s ease !important;
        }}
        .aqua-card:hover {{
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08) !important;
        }}

        .card-title {{
            font-family: 'Poppins', sans-serif !important;
            font-size: 15px !important;
            font-weight: 600 !important;
            color: {Colors.TEXT_PRIMARY} !important;
            margin-bottom: 12px !important;
        }}
        .card-subtitle {{
            font-family: 'Inter', sans-serif !important;
            font-size: 12px !important;
            color: {Colors.TEXT_SECONDARY} !important;
        }}

        .metric-value {{
            font-family: 'Poppins', sans-serif !important;
            font-size: 28px !important;
            font-weight: 700 !important;
            color: {Colors.TEXT_PRIMARY} !important;
            line-height: 1.2 !important;
        }}
        .metric-label {{
            font-family: 'Inter', sans-serif !important;
            font-size: 12px !important;
            color: {Colors.TEXT_SECONDARY} !important;
            margin-top: 4px !important;
        }}

        /* Status badges */
        .status-badge {{
            display: inline-block;
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 500;
            font-family: 'Inter', sans-serif;
        }}
        .status-success {{ background: rgba(34,197,94,0.1);  color: {Colors.SUCCESS}; }}
        .status-warning {{ background: rgba(245,158,11,0.1); color: {Colors.WARNING}; }}
        .status-danger  {{ background: rgba(239,68,68,0.1);  color: {Colors.DANGER};  }}
        .status-info    {{ background: rgba(59,130,246,0.1);  color: {Colors.INFO};    }}
    </style>
    """


def _footer_styles() -> str:
    return f"""
    <style>
        /* ── Footer ─────────────────────────────────────────────── */
        .aqua-footer {{
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px 0 12px 0;
            margin-top: 36px;
            border-top: 1px solid {Colors.BORDER};
        }}
        .footer-text {{
            font-family: 'Inter', sans-serif;
            font-size: 12px;
            color: {Colors.TEXT_SECONDARY};
        }}
        .footer-text strong {{
            color: {Colors.TEXT_PRIMARY};
            font-weight: 600;
        }}
    </style>
    """


def _component_styles() -> str:
    return f"""
    <style>
        /* ── Empty Page Placeholder ─────────────────────────────── */
        .page-placeholder {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 420px;
            background: {Colors.CARD};
            border-radius: 16px;
            border: 2px dashed {Colors.BORDER};
            margin-top: 8px;
        }}
        .placeholder-icon {{
            font-size: 52px;
            margin-bottom: 16px;
            opacity: 0.6;
        }}
        .placeholder-title {{
            font-family: 'Poppins', sans-serif;
            font-size: 22px;
            font-weight: 600;
            color: {Colors.TEXT_PRIMARY};
            margin-bottom: 8px;
        }}
        .placeholder-text {{
            font-family: 'Inter', sans-serif;
            font-size: 14px;
            color: {Colors.TEXT_SECONDARY};
            text-align: center;
            max-width: 420px;
            line-height: 1.6;
        }}

        /* ── Sidebar Logo ───────────────────────────────────────── */
        .sidebar-logo {{
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 24px 20px 12px 20px;
        }}
        .logo-icon {{
            width: 44px; height: 44px;
            background: {Colors.GRADIENT_BLUE};
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: {Colors.SHADOW_BLUE};
            flex-shrink: 0;
        }}
        .logo-text {{
            font-family: 'Poppins', sans-serif;
            font-size: 18px;
            font-weight: 700;
            letter-spacing: 0.5px;
        }}
        .logo-text .aqua {{ color: {Colors.SECONDARY_BLUE}; }}
        .logo-text .insights {{ color: {Colors.TEXT_WHITE}; }}

        /* ── Sidebar Divider ────────────────────────────────────── */
        .sidebar-divider {{
            height: 1px;
            background: {Colors.OVERLAY_BORDER};
            margin: 8px 20px;
        }}

        /* ── Sidebar Section Label ──────────────────────────────── */
        .sidebar-section-label {{
            font-family: 'Inter', sans-serif;
            font-size: 11px;
            font-weight: 600;
            color: rgba(255, 255, 255, 0.35);
            text-transform: uppercase;
            letter-spacing: 1px;
            padding: 8px 24px 4px 24px;
            margin: 0;
        }}

        /* ── Dataset Info Panel (sidebar) ───────────────────────── */
        .dataset-info {{
            background: {Colors.OVERLAY_LIGHT};
            border-radius: 12px;
            padding: 16px;
            margin: 12px 16px;
            border: 1px solid {Colors.OVERLAY_BORDER};
        }}
        .dataset-info-title {{
            font-family: 'Inter', sans-serif;
            font-size: 12px;
            font-weight: 600;
            color: {Colors.TEXT_LIGHT};
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 10px;
        }}
        .dataset-info-row {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 4px 0;
        }}
        .dataset-info-label {{
            font-family: 'Inter', sans-serif;
            font-size: 12px;
            color: {Colors.TEXT_LIGHT};
        }}
        .dataset-info-value {{
            font-family: 'Inter', sans-serif;
            font-size: 12px;
            color: {Colors.TEXT_WHITE};
            font-weight: 500;
        }}
        .view-details-btn {{
            display: block;
            width: 100%;
            padding: 8px 0;
            margin-top: 12px;
            background: {Colors.PRIMARY_BLUE};
            color: {Colors.TEXT_WHITE};
            border: none;
            border-radius: 8px;
            font-family: 'Inter', sans-serif;
            font-size: 13px;
            font-weight: 500;
            cursor: pointer;
            text-align: center;
            transition: background 0.2s ease;
        }}
        .view-details-btn:hover {{ background: {Colors.SECONDARY_BLUE}; }}

        /* ── Streamlit Widget Overrides ──────────────────────────── */
        .stSelectbox > div > div {{ border-radius: 8px; }}
        .stButton > button {{
            border-radius: 8px;
            font-family: 'Inter', sans-serif;
            font-weight: 500;
            transition: all 0.2s ease;
        }}
        .stTabs [data-baseweb="tab-list"] {{ gap: 0; }}
        .stTabs [data-baseweb="tab"] {{
            font-family: 'Inter', sans-serif;
            font-size: 14px;
            font-weight: 500;
            padding: 10px 20px;
            border-radius: 8px 8px 0 0;
        }}

        /* ── Bordered containers as aqua-cards ──────────────────── */
        div[data-testid="stVerticalBlockBorderWrapper"] {{
            background: {Colors.CARD} !important;
            border-radius: 16px !important;
            border: 1px solid {Colors.BORDER} !important;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04) !important;
            padding: 16px 18px !important;
            overflow: hidden !important;
        }}
        div[data-testid="stVerticalBlockBorderWrapper"] .js-plotly-plot,
        div[data-testid="stVerticalBlockBorderWrapper"] .plotly-graph-div {{
            max-width: 100% !important;
            overflow: hidden !important;
        }}
        div[data-testid="stPlotlyChart"] {{
            overflow: hidden !important;
        }}

        /* Disabled nav controls */
        .nav-btn-disabled {{
            opacity: 0.55;
            cursor: not-allowed;
        }}
    </style>
    """


def _layout_responsive_styles() -> str:
    return f"""
    <style>
        @media (max-width: 1400px) {{
            .main .block-container {{
                padding-left: 1.25rem !important;
                padding-right: 1.25rem !important;
            }}
        }}
        @media (max-width: 1100px) {{
            .navbar-search {{
                width: 180px !important;
            }}
            .stats-grid {{
                grid-template-columns: repeat(2, 1fr) !important;
            }}
            .tech-grid {{
                grid-template-columns: repeat(3, 1fr) !important;
            }}
        }}
        @media (max-width: 768px) {{
            .main .block-container {{
                padding-top: 1.25rem !important;
                padding-left: 0.75rem !important;
                padding-right: 0.75rem !important;
            }}
            .aqua-navbar {{
                flex-direction: column;
                align-items: flex-start;
                gap: 8px;
            }}
            .navbar-right {{
                flex-wrap: wrap;
            }}
            .login-left {{
                min-height: 320px !important;
            }}
        }}
    </style>
    """
