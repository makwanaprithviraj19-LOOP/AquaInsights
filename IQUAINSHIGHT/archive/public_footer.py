"""
AquaInsights — Public Page Footer
Shared footer for Home, About, and Contact pages.
"""

import streamlit as st
from utils.constants import APP_NAME, APP_VERSION, APP_YEAR


def render_public_footer() -> None:
    """Render the public-facing footer with tech stack badges."""

    st.markdown(
        f"""<div style="margin-top:40px; padding:28px 0 20px 0; border-top:1px solid #E5E7EB; text-align:center;">
<div style="font-family:'Poppins',sans-serif; font-size:17px; font-weight:700; color:#14213D; margin-bottom:4px;">
💧&nbsp;<span style="color:#1E88E5;">Aqua</span>Insights
</div>
<div style="font-family:'Inter',sans-serif; font-size:12px; color:#6B7280; margin-bottom:14px;">
Every Drop. Every Insight. Every Decision.
</div>
<div style="display:flex; gap:8px; justify-content:center; flex-wrap:wrap; margin-bottom:16px;">
<span style="background:#14213D; color:#fff; padding:4px 12px; border-radius:20px; font-size:11px; font-family:'Inter',sans-serif; font-weight:500;">Python</span>
<span style="background:#FF4B4B; color:#fff; padding:4px 12px; border-radius:20px; font-size:11px; font-family:'Inter',sans-serif; font-weight:500;">Streamlit</span>
<span style="background:#636EFA; color:#fff; padding:4px 12px; border-radius:20px; font-size:11px; font-family:'Inter',sans-serif; font-weight:500;">Plotly</span>
<span style="background:#F7931E; color:#fff; padding:4px 12px; border-radius:20px; font-size:11px; font-family:'Inter',sans-serif; font-weight:500;">Scikit-Learn</span>
</div>
<div style="font-family:'Inter',sans-serif; font-size:11px; color:#9CA3AF;">
<strong style="color:#111827;">{APP_NAME}</strong> &middot; Version {APP_VERSION} &middot; &copy; {APP_YEAR} All Rights Reserved
</div>
</div>""",
        unsafe_allow_html=True,
    )
