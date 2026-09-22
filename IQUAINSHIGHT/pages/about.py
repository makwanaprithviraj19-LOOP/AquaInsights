"""
AquaInsights — About Us Page
Modern About page with mission, vision, problem statement, features,
tech stack, architecture overview, and future roadmap.
"""

import streamlit as st


def render() -> None:
    """Render the About Us page."""

    st.markdown(_about_css(), unsafe_allow_html=True)

    # ═══════════════════ HEADER ═══════════════════════════════════════════
    st.markdown(_header_html(), unsafe_allow_html=True)

    # ═══════════════════ MISSION & VISION ═════════════════════════════════
    mv1, mv2 = st.columns(2)
    with mv1:
        st.markdown(_mission_html(), unsafe_allow_html=True)
    with mv2:
        st.markdown(_vision_html(), unsafe_allow_html=True)

    st.markdown('<div style="height:32px;"></div>', unsafe_allow_html=True)

    # ═══════════════════ WHY WATER QUALITY MATTERS ════════════════════════
    st.markdown(_why_section_html(), unsafe_allow_html=True)
    st.markdown('<div style="height:32px;"></div>', unsafe_allow_html=True)

    # ═══════════════════ PLATFORM FEATURES ════════════════════════════════
    st.markdown('<h2 class="section-title-center">Platform Features</h2>', unsafe_allow_html=True)
    st.markdown('<div style="height:14px;"></div>', unsafe_allow_html=True)

    features = [
        ("📊", "Analytics Dashboard", "Real-time KPIs, WHO compliance tables, trend charts, and correlation heatmaps."),
        ("📋", "Dataset Management", "Upload CSV/XLSX, auto-validate schemas, detect missing values and duplicates."),
        ("🧹", "Data Cleaning", "Health scoring, imputation, outlier detection, and one-click dataset normalization."),
        ("💧", "Parameter Explorer", "Deep-dive into each water quality indicator with histograms and safe-range analysis."),
        ("✨", "AI Insights", "Automated findings, natural language Q&A, and smart treatment recommendations."),
        ("🎯", "ML Prediction", "Random Forest potability classifier with confidence scoring and safety labels."),
        ("📈", "Visualizations", "Six chart types across five categories — distribution, scatter, trend, comparison, all."),
        ("📄", "Report Generator", "Executive PDF reports via ReportLab and raw CSV exports for further analysis."),
    ]

    for i in range(0, len(features), 4):
        cols = st.columns(4)
        for j, col in enumerate(cols):
            if i + j < len(features):
                icon, title, desc = features[i + j]
                with col:
                    st.markdown(
                        f"""<div class="feat-mini-card">
<span style="font-size:24px;">{icon}</span>
<h4 style="font-family:'Poppins',sans-serif; font-size:13px; font-weight:600; color:#111827; margin:6px 0 4px 0;">{title}</h4>
<p style="font-family:'Inter',sans-serif; font-size:11px; color:#6B7280; line-height:1.4; margin:0;">{desc}</p>
</div>""",
                        unsafe_allow_html=True,
                    )

    st.markdown('<div style="height:32px;"></div>', unsafe_allow_html=True)

    # ═══════════════════ TECHNOLOGY STACK ══════════════════════════════════
    st.markdown(_tech_stack_html(), unsafe_allow_html=True)
    st.markdown('<div style="height:32px;"></div>', unsafe_allow_html=True)

    # ═══════════════════ ROADMAP ══════════════════════════════════════════
    st.markdown('<h2 class="section-title-center">Future Roadmap</h2>', unsafe_allow_html=True)
    st.markdown('<div style="height:14px;"></div>', unsafe_allow_html=True)

    roadmap_items = [
        ("Q3 2026", "Real-Time IoT Integration", "Connect live sensor feeds for continuous water quality monitoring.", "#1E88E5"),
        ("Q4 2026", "Deep Learning Anomaly Detection", "LSTM and Transformer models for advanced contamination prediction.", "#7C3AED"),
        ("Q1 2027", "Cloud Deployment", "One-click deployment to AWS, GCP, and Azure with auto-scaling.", "#F59E0B"),
        ("Q2 2027", "Mobile Application", "React Native companion app for field engineers and on-site monitoring.", "#22C55E"),
    ]

    for quarter, title, desc, color in roadmap_items:
        st.markdown(
            f"""<div class="roadmap-item">
<div class="roadmap-dot" style="background:{color};"></div>
<div class="roadmap-content">
<span class="roadmap-quarter" style="color:{color};">{quarter}</span>
<h4 class="roadmap-title">{title}</h4>
<p class="roadmap-desc">{desc}</p>
</div>
</div>""",
            unsafe_allow_html=True,
        )


def _header_html() -> str:
    return """<div style="text-align:center; padding:8px 0 28px 0;">
<div class="about-badge">About AquaInsights</div>
<h1 class="about-heading">Transforming Water Quality<br/>Through Data Science</h1>
<p class="about-sub">A comprehensive analytics platform built with modern technology to empower better water management decisions worldwide.</p>
</div>"""


def _mission_html() -> str:
    return """<div class="mv-card" style="border-left:4px solid #1E88E5;">
<div class="mv-icon">🎯</div>
<h3 class="mv-title">Our Mission</h3>
<p class="mv-text">To democratize water quality analytics by providing an accessible, AI-driven platform that transforms complex data into actionable intelligence — making clean water analysis available to every researcher, authority, and organization.</p>
</div>"""


def _vision_html() -> str:
    return """<div class="mv-card" style="border-left:4px solid #22C55E;">
<div class="mv-icon">🌍</div>
<h3 class="mv-title">Our Vision</h3>
<p class="mv-text">A world where every drop of water is monitored, analyzed, and optimized for safety — powered by intelligent software that predicts contamination, guides treatment, and protects public health across communities.</p>
</div>"""


def _why_section_html() -> str:
    return """<div class="why-section">
<h2 class="section-title-center">Why Water Quality Matters</h2>
<div class="why-grid">
<div class="why-card"><span class="why-icon">🏥</span><h4 class="why-heading">Public Health</h4><p class="why-desc">Contaminated water causes 485,000+ diarrheal deaths yearly. Early detection saves lives.</p></div>
<div class="why-card"><span class="why-icon">🌱</span><h4 class="why-heading">Environment</h4><p class="why-desc">Monitoring prevents ecosystem degradation and protects aquatic biodiversity.</p></div>
<div class="why-card"><span class="why-icon">⚖️</span><h4 class="why-heading">Compliance</h4><p class="why-desc">WHO guidelines require regular testing. Automated tracking ensures zero violations.</p></div>
<div class="why-card"><span class="why-icon">💡</span><h4 class="why-heading">Smart Decisions</h4><p class="why-desc">Data-driven treatment optimization reduces costs and improves water safety outcomes.</p></div>
</div>
</div>"""


def _tech_stack_html() -> str:
    return """<div class="tech-stack-section">
<h2 class="section-title-center" style="color:#fff;">Technology Stack</h2>
<div style="height:16px;"></div>
<div style="display:flex; justify-content:center; gap:12px; flex-wrap:wrap;">
<div class="tech-pill">🐍 Python 3.12+</div>
<div class="tech-pill">⚡ Streamlit</div>
<div class="tech-pill">🐼 Pandas</div>
<div class="tech-pill">📐 NumPy</div>
<div class="tech-pill">📈 Plotly</div>
<div class="tech-pill">📊 Matplotlib</div>
<div class="tech-pill">🧠 Scikit-Learn</div>
<div class="tech-pill">📄 ReportLab</div>
</div>
</div>"""


def _about_css() -> str:
    return """<style>
.about-badge {
    display: inline-block; font-family:'Inter',sans-serif; font-size:12px;
    font-weight:600; color:#1E88E5; background:rgba(30,136,229,.08);
    padding:5px 14px; border-radius:20px; margin-bottom:12px;
}
.about-heading {
    font-family:'Poppins',sans-serif; font-size:32px; font-weight:800;
    color:#111827; line-height:1.2; margin:0 0 8px 0;
}
.about-sub {
    font-family:'Inter',sans-serif; font-size:14px; color:#6B7280;
    max-width:540px; margin:0 auto; line-height:1.5;
}
.section-title-center {
    font-family:'Poppins',sans-serif; font-size:22px; font-weight:700;
    color:#111827; text-align:center; margin:0;
}

.mv-card {
    background:#fff; border:1px solid #E5E7EB; border-radius:18px;
    padding:24px; min-height:200px; box-shadow:0 2px 8px rgba(0,0,0,.04);
}
.mv-icon { font-size:26px; margin-bottom:8px; }
.mv-title { font-family:'Poppins',sans-serif; font-size:16px; font-weight:600; color:#111827; margin:0 0 8px 0; }
.mv-text  { font-family:'Inter',sans-serif; font-size:12px; color:#4B5563; line-height:1.6; margin:0; }

.why-section { text-align:center; }
.why-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:14px; margin-top:16px; }
.why-card {
    background:#fff; border:1px solid #E5E7EB; border-radius:14px;
    padding:18px; transition:transform .2s ease;
}
.why-card:hover { transform:translateY(-3px); }
.why-icon { font-size:26px; }
.why-heading { font-family:'Poppins',sans-serif; font-size:13px; font-weight:600; color:#111827; margin:8px 0 4px 0; }
.why-desc { font-family:'Inter',sans-serif; font-size:11px; color:#6B7280; line-height:1.4; margin:0; }

.feat-mini-card {
    background:#fff; border:1px solid #E5E7EB; border-radius:14px;
    padding:16px; min-height:130px; box-shadow:0 1px 3px rgba(0,0,0,.04);
}

.tech-stack-section {
    background:linear-gradient(135deg,#14213D,#1B2D50);
    border-radius:18px; padding:30px 20px; text-align:center;
}
.tech-pill {
    background:rgba(255,255,255,.08); color:#fff;
    padding:6px 14px; border-radius:20px;
    font-family:'Inter',sans-serif; font-size:12px; font-weight:500;
    border:1px solid rgba(255,255,255,.1);
}

.roadmap-item {
    display:flex; align-items:flex-start; gap:14px;
    padding:10px 0; border-left:2px solid #E5E7EB;
    margin-left:10px; padding-left:20px; position:relative;
}
.roadmap-dot {
    width:10px; height:10px; border-radius:50%;
    position:absolute; left:-6px; top:14px;
}
.roadmap-content { flex:1; }
.roadmap-quarter { font-family:'Inter',sans-serif; font-size:11px; font-weight:700; }
.roadmap-title { font-family:'Poppins',sans-serif; font-size:14px; font-weight:600; color:#111827; margin:2px 0; }
.roadmap-desc { font-family:'Inter',sans-serif; font-size:12px; color:#6B7280; line-height:1.4; margin:0; }
</style>"""
