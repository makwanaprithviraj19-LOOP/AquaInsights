"""
AquaInsights — Home Page
Public landing page with hero, features, statistics, technology, and CTA sections.
"""

import streamlit as st
from utils.colors import Colors


def render() -> None:
    """Render the public Home / Landing page."""

    st.markdown(_home_css(), unsafe_allow_html=True)

    # ═══════════════════ HERO SECTION ═════════════════════════════════════
    hero_left, hero_right = st.columns([1.3, 1])

    with hero_left:
        st.markdown(_hero_content_html(), unsafe_allow_html=True)
        bc1, bc2, _ = st.columns([1, 1, 2])
        with bc1:
            if st.button("Explore Platform", key="hero_explore", type="primary", use_container_width=True):
                st.session_state["app_view"] = "about"
                st.rerun()
        with bc2:
            if st.button("Open Dashboard", key="hero_dashboard", use_container_width=True):
                st.session_state["app_view"] = "dashboard"
                st.rerun()

    with hero_right:
        st.markdown(_water_illustration_html(), unsafe_allow_html=True)

    st.markdown('<div style="height:40px;"></div>', unsafe_allow_html=True)

    # ═══════════════════ FEATURES SECTION ═════════════════════════════════
    st.markdown(_features_header_html(), unsafe_allow_html=True)

    f1, f2, f3, f4 = st.columns(4)
    _feature_cards = [
        (f1, "📊", "Smart Analytics", "Advanced dashboards with real-time metrics, interactive charts, and statistical deep-dives.", "#1E88E5"),
        (f2, "✨", "AI Insights", "Machine learning powered recommendations and natural language query interface for smart data exploration.", "#7C3AED"),
        (f3, "🎯", "Prediction", "Water potability classification using trained ML models with confidence scoring and safety assessments.", "#F59E0B"),
        (f4, "📄", "Actionable Reports", "Generate executive PDF reports and CSV exports with WHO compliance analysis and trend summaries.", "#22C55E"),
    ]

    for col, icon, title, desc, color in _feature_cards:
        with col:
            st.markdown(
                f"""<div class="feature-card">
<div class="feature-icon" style="background:linear-gradient(135deg, {color}22, {color}11);">
<span style="font-size:26px;">{icon}</span>
</div>
<h3 class="feature-title">{title}</h3>
<p class="feature-desc">{desc}</p>
</div>""",
                unsafe_allow_html=True,
            )

    st.markdown('<div style="height:40px;"></div>', unsafe_allow_html=True)

    # ═══════════════════ STATISTICS SECTION ════════════════════════════════
    st.markdown(_stats_section_html(), unsafe_allow_html=True)
    st.markdown('<div style="height:40px;"></div>', unsafe_allow_html=True)

    # ═══════════════════ TECHNOLOGY SECTION ════════════════════════════════
    st.markdown(_tech_section_html(), unsafe_allow_html=True)
    st.markdown('<div style="height:40px;"></div>', unsafe_allow_html=True)

    # ═══════════════════ CTA SECTION ══════════════════════════════════════
    st.markdown(_cta_section_html(), unsafe_allow_html=True)
    _, cta_col, _ = st.columns([2, 1.5, 2])
    with cta_col:
        if st.button("🚀 Enter Dashboard", key="cta_enter_dashboard", type="primary", use_container_width=True):
            st.session_state["app_view"] = "dashboard"
            st.rerun()


def _hero_content_html() -> str:
    return """<div class="hero-content">
<div class="hero-badge">💧 Enterprise Water Analytics</div>
<h1 class="hero-title">Intelligent Insights<br/>for <span class="hero-accent">Cleaner Water</span></h1>
<p class="hero-desc">Analyze, Visualize, Understand. AquaInsights transforms raw water quality data into actionable intelligence using advanced analytics, machine learning, and AI-powered recommendations — helping you make better decisions for a healthier tomorrow.</p>
</div>"""


def _water_illustration_html() -> str:
    return """<div style="display:flex; align-items:center; justify-content:center; min-height:340px; position:relative;">
<style>
@keyframes dropFloat { 0%,100% { transform:translateY(0); } 50% { transform:translateY(-14px); } }
@keyframes ringPulse { 0%,100% { transform:scale(1); opacity:.3; } 50% { transform:scale(1.15); opacity:.15; } }
</style>
<div style="position:absolute; width:240px; height:240px; border-radius:50%; border:2px solid rgba(30,136,229,.12); animation:ringPulse 3s ease-in-out infinite;"></div>
<div style="width:160px; height:160px; border-radius:50%; background:linear-gradient(160deg, rgba(30,136,229,.12) 0%, rgba(66,165,245,.06) 100%); display:flex; align-items:center; justify-content:center; animation:dropFloat 4s ease-in-out infinite; box-shadow:0 12px 40px rgba(30,136,229,.12);">
<svg width="70" height="70" viewBox="0 0 24 24" fill="none">
<path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0L12 2.69z" fill="url(#dropGradHome)" opacity=".85"/>
<defs>
<linearGradient id="dropGradHome" x1="6" y1="3" x2="18" y2="21">
<stop offset="0%" stop-color="#1E88E5"/>
<stop offset="100%" stop-color="#64B5F6"/>
</linearGradient>
</defs>
</svg>
</div>
<div style="position:absolute; top:30px; right:15px; background:#fff; border:1px solid #E5E5E5; border-radius:10px; padding:6px 12px; box-shadow:0 4px 12px rgba(0,0,0,.06); font-family:Inter,sans-serif; font-size:11px; color:#6B7280;">
<span style="font-weight:700; color:#22C55E;">92%</span> Quality
</div>
<div style="position:absolute; bottom:30px; left:10px; background:#fff; border:1px solid #E5E5E5; border-radius:10px; padding:6px 12px; box-shadow:0 4px 12px rgba(0,0,0,.06); font-family:Inter,sans-serif; font-size:11px; color:#6B7280;">
<span style="font-weight:700; color:#1E88E5;">5,274</span> Samples
</div>
</div>"""


def _features_header_html() -> str:
    return """<div style="text-align:center; margin-bottom:24px;">
<h2 class="section-title">Powerful Capabilities</h2>
<p class="section-subtitle">Everything you need for comprehensive water quality analysis</p>
</div>"""


def _stats_section_html() -> str:
    return """<div class="stats-section">
<div class="stats-grid">
<div class="stat-item"><div class="stat-value">5,274+</div><div class="stat-label">Water Samples</div></div>
<div class="stat-item"><div class="stat-value" style="color:#22C55E;">96%</div><div class="stat-label">Data Quality</div></div>
<div class="stat-item"><div class="stat-value" style="color:#7C3AED;">9</div><div class="stat-label">Parameters Analyzed</div></div>
<div class="stat-item"><div class="stat-value" style="color:#F59E0B;">88.7%</div><div class="stat-label">Safe Water Rate</div></div>
</div>
</div>"""


def _tech_section_html() -> str:
    return """<div style="text-align:center; margin-bottom:24px;">
<h2 class="section-title">Built With Modern Technology</h2>
<p class="section-subtitle">Enterprise-grade stack for reliability and performance</p>
</div>
<div class="tech-grid">
<div class="tech-card"><div class="tech-icon">🐍</div><div class="tech-name">Python</div><div class="tech-role">Core Engine</div></div>
<div class="tech-card"><div class="tech-icon" style="color:#FF4B4B;">⚡</div><div class="tech-name">Streamlit</div><div class="tech-role">Application Framework</div></div>
<div class="tech-card"><div class="tech-icon" style="color:#636EFA;">📈</div><div class="tech-name">Plotly</div><div class="tech-role">Interactive Charts</div></div>
<div class="tech-card"><div class="tech-icon" style="color:#150458;">🐼</div><div class="tech-name">Pandas</div><div class="tech-role">Data Processing</div></div>
<div class="tech-card"><div class="tech-icon" style="color:#F7931E;">🧠</div><div class="tech-name">Scikit-Learn</div><div class="tech-role">Machine Learning</div></div>
<div class="tech-card"><div class="tech-icon" style="color:#22C55E;">🤖</div><div class="tech-name">ML Pipeline</div><div class="tech-role">Prediction Engine</div></div>
</div>"""


def _cta_section_html() -> str:
    return """<div class="cta-section">
<h2 class="cta-title">Ready to Transform Water Quality Analysis?</h2>
<p class="cta-desc">Start exploring your data with enterprise-grade tools designed for impact.</p>
</div>"""


def _home_css() -> str:
    return """<style>
section[data-testid="stSidebar"] { display: none !important; }

.hero-content { padding: 12px 0 0 0; }
.hero-badge {
    display: inline-block; font-family: 'Inter', sans-serif; font-size: 12px; font-weight: 600;
    color: #1E88E5; background: rgba(30,136,229,.08); padding: 6px 14px; border-radius: 20px;
    margin-bottom: 14px;
}
.hero-title {
    font-family: 'Poppins', sans-serif; font-size: 38px; font-weight: 800; line-height: 1.15;
    color: #111827; margin: 0 0 14px 0;
}
.hero-accent { color: #1E88E5; }
.hero-desc {
    font-family: 'Inter', sans-serif; font-size: 14px; color: #4B5563; line-height: 1.6;
    max-width: 500px; margin: 0 0 20px 0;
}

.section-title {
    font-family: 'Poppins', sans-serif; font-size: 26px; font-weight: 700; color: #111827; margin: 0 0 4px 0;
}
.section-subtitle {
    font-family: 'Inter', sans-serif; font-size: 13px; color: #6B7280; margin: 0;
}

.feature-card {
    background: #FFFFFF; border: 1px solid #E5E7EB; border-radius: 18px;
    padding: 22px; min-height: 220px; box-shadow: 0 2px 8px rgba(0,0,0,.04);
    transition: transform .2s ease, box-shadow .2s ease;
}
.feature-card:hover { transform: translateY(-4px); box-shadow: 0 8px 20px rgba(0,0,0,.08); }
.feature-icon {
    width: 48px; height: 48px; border-radius: 12px;
    display: flex; align-items: center; justify-content: center; margin-bottom: 14px;
}
.feature-title {
    font-family: 'Poppins', sans-serif; font-size: 15px; font-weight: 600; color: #111827; margin: 0 0 6px 0;
}
.feature-desc {
    font-family: 'Inter', sans-serif; font-size: 12px; color: #6B7280; line-height: 1.5; margin: 0;
}

.stats-section {
    background: linear-gradient(135deg, #14213D 0%, #1B2D50 100%);
    border-radius: 18px; padding: 36px 28px;
}
.stats-grid {
    display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; text-align: center;
}
.stat-value {
    font-family: 'Poppins', sans-serif; font-size: 32px; font-weight: 800; color: #FFFFFF;
}
.stat-label {
    font-family: 'Inter', sans-serif; font-size: 12px; color: #94A3B8; margin-top: 4px;
}

.tech-grid { display: grid; grid-template-columns: repeat(6, 1fr); gap: 14px; }
.tech-card {
    background: #FFFFFF; border: 1px solid #E5E7EB; border-radius: 14px;
    padding: 18px; text-align: center; transition: transform .2s ease;
}
.tech-card:hover { transform: translateY(-3px); }
.tech-icon { font-size: 26px; margin-bottom: 6px; }
.tech-name { font-family: 'Poppins', sans-serif; font-size: 13px; font-weight: 600; color: #111827; }
.tech-role { font-family: 'Inter', sans-serif; font-size: 10px; color: #9CA3AF; margin-top: 2px; }

.cta-section { text-align: center; padding: 12px 0; }
.cta-title { font-family: 'Poppins', sans-serif; font-size: 24px; font-weight: 700; color: #111827; margin: 0 0 6px 0; }
.cta-desc { font-family: 'Inter', sans-serif; font-size: 13px; color: #6B7280; margin: 0 0 16px 0; }
</style>"""
