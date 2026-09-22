"""
AquaInsights — Login Page
Full-screen split-layout SaaS login page matching Reference Image 3.
"""

import streamlit as st
from utils.colors import Colors


def render() -> None:
    """Render the Login page cleanly without raw HTML rendering bugs."""

    st.markdown(_login_css(), unsafe_allow_html=True)

    left_col, right_col = st.columns([1.1, 1], gap="large")

    # ═══════════════════ LEFT PANEL ═══════════════════════════════════════
    with left_col:
        st.markdown(_left_panel_html(), unsafe_allow_html=True)

    # ═══════════════════ RIGHT PANEL (Form) ═══════════════════════════════
    with right_col:
        st.markdown(_right_panel_header_html(), unsafe_allow_html=True)

        with st.form("login_form_main", clear_on_submit=False):
            email = st.text_input("Email Address", placeholder="you@example.com", key="login_email_input")
            password = st.text_input("Password", type="password", placeholder="Enter your password", key="login_password_input")

            rem_col, forgot_col = st.columns(2)
            with rem_col:
                remember = st.checkbox("Remember me", value=True, key="login_remember")
            with forgot_col:
                st.markdown(
                    '<p style="text-align:right; margin:6px 0 0 0;"><a href="#" style="font-size:12px; color:#1E88E5; font-family:Inter,sans-serif; text-decoration:none;">Forgot Password?</a></p>',
                    unsafe_allow_html=True,
                )

            submit = st.form_submit_button("Sign In", type="primary", use_container_width=True)

            if submit:
                if email and password:
                    st.session_state["logged_in"] = True
                    st.session_state["user_email"] = email
                    st.session_state["app_view"] = "home"
                    st.rerun()
                else:
                    st.error("Please enter both email and password.")

        st.markdown('<div style="text-align:center; font-size:12px; color:#9CA3AF; margin:12px 0;">OR</div>', unsafe_allow_html=True)

        gc1, gc2 = st.columns(2)
        with gc1:
            if st.button("👤 Continue as Guest", key="login_guest_btn", use_container_width=True):
                st.session_state["logged_in"] = True
                st.session_state["user_email"] = "guest@aquainsights.io"
                st.session_state["app_view"] = "home"
                st.rerun()
        with gc2:
            st.button("Create Account", key="login_create_btn", use_container_width=True, disabled=True)

        st.markdown(
            '<p style="text-align:center; font-size:11px; color:#9CA3AF; margin-top:16px; font-family:Inter,sans-serif;">Don\'t have an account? <a href="#" style="color:#1E88E5; font-weight:600; text-decoration:none;">Create Account</a></p>',
            unsafe_allow_html=True,
        )


def _left_panel_html() -> str:
    return """<div class="login-left">
<div class="particle p1"></div>
<div class="particle p2"></div>
<div class="particle p3"></div>
<div class="water-ring ring1"></div>
<div class="water-ring ring2"></div>
<div class="login-left-content">
<div class="login-left-logo">
<svg width="44" height="44" viewBox="0 0 24 24" fill="white">
<path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0L12 2.69z"/>
</svg>
</div>
<h1 class="login-left-title"><span style="color:#64B5F6;">AQUA</span>INSIGHTS</h1>
<p class="login-left-subtitle">Enterprise Water Quality Analytics Platform</p>
<p class="login-left-desc">Analyze. Visualize. Understand.<br/>Make better decisions for a healthier tomorrow.</p>
<div class="login-features">
<div class="login-feat-item"><span class="feat-icon">📊</span><div><strong>Smart Analytics</strong><br/><span style="font-size:11px; color:#94A3B8;">Get actionable insights from water quality data</span></div></div>
<div class="login-feat-item"><span class="feat-icon">✨</span><div><strong>AI Powered</strong><br/><span style="font-size:11px; color:#94A3B8;">Advanced ML models for accurate predictions</span></div></div>
<div class="login-feat-item"><span class="feat-icon">🛡️</span><div><strong>Secure & Reliable</strong><br/><span style="font-size:11px; color:#94A3B8;">Enterprise grade security for your data</span></div></div>
</div>
</div>
</div>"""


def _right_panel_header_html() -> str:
    return """<div style="text-align:center; margin-bottom:16px; padding-top:12px;">
<div style="width:48px; height:48px; border-radius:12px; background:linear-gradient(135deg,#1E88E5,#42A5F5); display:inline-flex; align-items:center; justify-content:center; box-shadow:0 6px 18px rgba(30,136,229,.35); margin-bottom:12px;">
<svg width="24" height="24" viewBox="0 0 24 24" fill="white">
<path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0L12 2.69z"/>
</svg>
</div>
<h2 style="font-family:'Poppins',sans-serif; font-size:22px; font-weight:700; color:#111827; margin:0;">Welcome Back 👋</h2>
<p style="font-family:'Inter',sans-serif; font-size:13px; color:#6B7280; margin:4px 0 0 0;">Sign in to your AquaInsights account</p>
</div>"""


def _login_css() -> str:
    return """<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');

section[data-testid="stSidebar"] { display: none !important; }
[data-testid="stHeader"]         { display: none !important; }
#MainMenu, footer                { visibility: hidden !important; }
.stApp { background: #F8FAFC !important; }
.main .block-container { padding: 1rem 2rem !important; max-width: 100% !important; }

.login-left {
    position: relative;
    min-height: 86vh;
    background: linear-gradient(160deg, #14213D 0%, #0D1B2A 50%, #091520 100%);
    border-radius: 20px;
    display: flex; align-items: center; justify-content: center;
    overflow: hidden;
    padding: 30px;
}
.login-left-content {
    position: relative; z-index: 2;
    text-align: left; max-width: 380px;
}
.login-left-logo {
    width: 68px; height: 68px; border-radius: 16px;
    background: linear-gradient(135deg, #1E88E5, #42A5F5);
    display: inline-flex; align-items: center; justify-content: center;
    box-shadow: 0 8px 24px rgba(30,136,229,.4);
    margin-bottom: 20px;
}
.login-left-title {
    font-family: 'Poppins', sans-serif;
    font-size: 28px; font-weight: 800; color: #fff;
    letter-spacing: 0.5px; margin: 0 0 6px 0;
}
.login-left-subtitle {
    font-family: 'Inter', sans-serif;
    font-size: 13px; color: #94A3B8;
    margin: 0 0 16px 0;
}
.login-left-desc {
    font-family: 'Inter', sans-serif;
    font-size: 13px; color: #64748B; line-height: 1.6;
    margin: 0 0 24px 0;
}
.login-features {
    display: flex; flex-direction: column; gap: 14px;
}
.login-feat-item {
    display: flex; align-items: center; gap: 12px;
    background: rgba(255,255,255,.05); border: 1px solid rgba(255,255,255,.08);
    border-radius: 12px; padding: 10px 14px;
    font-family: 'Inter', sans-serif; font-size: 12px; color: #E2E8F0;
}
.feat-icon { font-size: 18px; }

@keyframes float { 0%,100% { transform:translateY(0); } 50% { transform:translateY(-14px); } }
.particle {
    position: absolute; border-radius: 50%;
    background: rgba(30,136,229,.15);
    animation: float 4s ease-in-out infinite;
}
.p1 { width:8px; height:8px; top:15%; left:12%; animation-delay:0s; }
.p2 { width:12px; height:12px; top:70%; left:20%; animation-delay:.8s; }
.p3 { width:6px; height:6px; top:30%; right:15%; animation-delay:1.4s; }

@keyframes waterRing {
    0%   { transform:scale(.7); opacity:.4; }
    100% { transform:scale(2.2); opacity:0; }
}
.water-ring {
    position: absolute; border-radius: 50%;
    border: 1px solid rgba(66,165,245,.2);
    pointer-events: none;
}
.ring1 { width:160px; height:160px; top:40%; left:40%; animation:waterRing 3.5s ease-out infinite; }
.ring2 { width:160px; height:160px; top:40%; left:40%; animation:waterRing 3.5s ease-out 1.2s infinite; }

[data-testid="stForm"] {
    background: #FFFFFF !important;
    border: 1px solid #E5E7EB !important;
    border-radius: 18px !important;
    padding: 24px !important;
    box-shadow: 0 4px 16px rgba(0,0,0,.04) !important;
}
</style>"""
