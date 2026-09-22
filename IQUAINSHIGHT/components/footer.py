import streamlit as st
from utils.constants import APP_NAME, APP_VERSION, APP_YEAR

def render_footer() -> None:
    html = f"""
<div class="aqua-footer">
    <p class="footer-text">
        <strong>{APP_NAME}</strong> · Version {APP_VERSION} · © {APP_YEAR} All Rights Reserved
    </p>
</div>
    """
    st.markdown(html, unsafe_allow_html=True)
