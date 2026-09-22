import streamlit as st
from utils.colors import Colors

def render_navbar(title: str, subtitle: str) -> None:
    html = f"""
<div class="aqua-navbar">
    <div class="navbar-left">
        <h1 class="navbar-title">{title}</h1>
        <p class="navbar-subtitle">{subtitle}</p>
    </div>
    <div class="navbar-right">
        <div class="navbar-search">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="{Colors.TEXT_LIGHT}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="11" cy="11" r="8"></circle>
                <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
            </svg>
            <input type="text" placeholder="Search datasets, reports..." disabled />
        </div>
        <div class="nav-icon-btn" title="Toggle Theme">
            🌙
        </div>
        <div class="nav-icon-btn" title="Notifications">
            🔔
            <div class="notification-dot"></div>
        </div>
        <div class="user-profile" title="User Profile">
            <div class="user-avatar">U</div>
            <div class="user-info">
                <span class="user-name">User</span>
                <span class="user-role">Admin</span>
            </div>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="{Colors.TEXT_SECONDARY}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-left: 4px;">
                <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
        </div>
    </div>
</div>
    """
    st.markdown(html, unsafe_allow_html=True)
