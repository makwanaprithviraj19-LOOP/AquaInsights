"""
AquaInsights — Splash Screen
Animated full-viewport splash with water ripple, logo zoom,
fade-in text, and a progress bar that auto-advances.
"""

import streamlit as st
import time


def render() -> None:
    """Render the splash screen once, then auto-advance to login."""

    # ── Hide all Streamlit chrome ─────────────────────────────────────────
    st.markdown(
        """<style>
section[data-testid="stSidebar"] { display: none !important; }
[data-testid="stHeader"]         { display: none !important; }
#MainMenu, footer                { visibility: hidden !important; }
.main .block-container { padding: 0 !important; max-width: 100vw !important; }
.stApp { background: #14213D !important; }
</style>""",
        unsafe_allow_html=True,
    )

    # ── Splash HTML + CSS animations ──────────────────────────────────────
    st.markdown(_splash_content(), unsafe_allow_html=True)

    # Wait for animations then auto-advance
    time.sleep(2.5)
    st.session_state["splash_shown"] = True
    st.rerun()


def _splash_content() -> str:
    return """<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');

@keyframes fadeIn  { from { opacity:0; } to { opacity:1; } }
@keyframes zoomIn  { from { opacity:0; transform:scale(.5); } to { opacity:1; transform:scale(1); } }
@keyframes slideUp { from { opacity:0; transform:translateY(24px); } to { opacity:1; transform:translateY(0); } }
@keyframes pulse   { 0%,100% { transform:scale(1); } 50% { transform:scale(1.06); } }
@keyframes loadBar { from { width:0; } to { width:100%; } }

@keyframes ripple1 { 0% { transform:scale(.6); opacity:.5; } 100% { transform:scale(2.4); opacity:0; } }
@keyframes ripple2 { 0% { transform:scale(.6); opacity:.4; } 100% { transform:scale(2.8); opacity:0; } }

.splash {
    position: fixed; inset: 0; z-index: 99999;
    background: linear-gradient(160deg, #14213D 0%, #0D1B2A 60%, #0A1628 100%);
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    overflow: hidden;
}
.splash-ripple {
    position: absolute; border-radius: 50%;
    border: 1.5px solid rgba(30,136,229,.25); pointer-events: none;
}
.splash-ripple.r1 { width:160px; height:160px; animation: ripple1 2.4s ease-out infinite; }
.splash-ripple.r2 { width:160px; height:160px; animation: ripple2 2.4s ease-out .6s infinite; }

.splash-logo-wrap {
    position: relative; z-index: 2;
    animation: zoomIn .8s cubic-bezier(.22,1,.36,1) forwards;
}
.splash-logo {
    width: 86px; height: 86px;
    background: linear-gradient(135deg, #1E88E5 0%, #42A5F5 100%);
    border-radius: 20px;
    display: flex; align-items: center; justify-content: center;
    box-shadow: 0 8px 32px rgba(30,136,229,.45);
    animation: pulse 2s ease-in-out infinite;
}
.splash-brand {
    margin-top: 22px; font-family: 'Poppins', sans-serif;
    font-size: 32px; font-weight: 800; letter-spacing: 1px;
    animation: fadeIn .7s ease .4s both; z-index: 2;
}
.splash-brand .aqua     { color: #42A5F5; }
.splash-brand .insights { color: #FFFFFF; }

.splash-tagline {
    margin-top: 8px; font-family: 'Inter', sans-serif;
    font-size: 14px; color: #94A3B8; letter-spacing: .5px;
    animation: slideUp .6s ease .8s both; z-index: 2;
}
.splash-progress-wrap {
    margin-top: 40px; width: 220px; height: 4px;
    background: rgba(255,255,255,.08); border-radius: 4px;
    overflow: hidden; animation: fadeIn .5s ease 1s both; z-index: 2;
}
.splash-progress-bar {
    height: 100%;
    background: linear-gradient(90deg, #1E88E5, #42A5F5, #64B5F6);
    border-radius: 4px; animation: loadBar 2.2s ease-in-out forwards;
}
.splash-loading-text {
    margin-top: 12px; font-family: 'Inter', sans-serif;
    font-size: 12px; color: rgba(255,255,255,.4);
    animation: fadeIn .5s ease 1.2s both; z-index: 2;
}
</style>
<div class="splash">
<div class="splash-ripple r1"></div>
<div class="splash-ripple r2"></div>
<div class="splash-logo-wrap">
<div class="splash-logo">
<svg width="44" height="44" viewBox="0 0 24 24" fill="white">
<path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0L12 2.69z"/>
</svg>
</div>
</div>
<div class="splash-brand"><span class="aqua">Aqua</span><span class="insights">Insights</span></div>
<div class="splash-tagline">Every Drop. Every Insight. Every Decision.</div>
<div class="splash-progress-wrap"><div class="splash-progress-bar"></div></div>
<div class="splash-loading-text">Loading AquaInsights&hellip;</div>
</div>"""
