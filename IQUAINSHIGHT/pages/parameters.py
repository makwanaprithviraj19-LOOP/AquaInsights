"""
AquaInsights — Water Parameters Page
Water quality parameters overview grid & parameter explorer deep dive matching Image 1 (#7 & #8).
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from services.csv_loader import CSVLoader
from services.analytics_engine import AnalyticsEngine

def render() -> None:
    loader = CSVLoader()
    analytics = AnalyticsEngine()
    df = loader.get_default_dataset()

    tab_overview, tab_explorer = st.tabs(["💧 All Water Parameters", "🔬 Parameter Explorer (pH)"])

    # ── TAB 1: ALL WATER PARAMETERS ──────────────────────────────────────────
    with tab_overview:
        st.markdown('<div class="card-title" style="font-size: 18px; margin-bottom: 16px;">Explore & understand water quality parameters</div>', unsafe_allow_html=True)

        params_data = [
            ("pH", "7.18", "", "Normal", "success"),
            ("Hardness", "195", "mg/L", "Moderate", "info"),
            ("TDS", "315", "ppm", "Good", "success"),
            ("Turbidity", "2.1", "NTU", "Good", "success"),
            ("Conductivity", "512", "µS/cm", "Moderate", "info"),
            ("Chloramines", "2.2", "mg/L", "Good", "success"),
            ("Sulfate", "333", "mg/L", "Good", "success"),
            ("Organic Carbon", "10.2", "mg/L", "Good", "success"),
        ]

        row1_cols = st.columns(4)
        for i, (name, val, unit, status, s_type) in enumerate(params_data[:4]):
            with row1_cols[i]:
                st.markdown(
                    f"""
<div class="aqua-card" style="padding: 16px; min-height: 140px;">
    <div class="card-subtitle">{name}</div>
    <div class="metric-value" style="font-size: 24px; margin: 6px 0;">{val} <span style="font-size: 12px; font-weight:400; color:#6B7280;">{unit}</span></div>
    <span class="status-badge status-{s_type}">{status}</span>
</div>
                    """,
                    unsafe_allow_html=True
                )

        st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

        row2_cols = st.columns(4)
        for i, (name, val, unit, status, s_type) in enumerate(params_data[4:]):
            with row2_cols[i]:
                st.markdown(
                    f"""
<div class="aqua-card" style="padding: 16px; min-height: 140px;">
    <div class="card-subtitle">{name}</div>
    <div class="metric-value" style="font-size: 24px; margin: 6px 0;">{val} <span style="font-size: 12px; font-weight:400; color:#6B7280;">{unit}</span></div>
    <span class="status-badge status-{s_type}">{status}</span>
</div>
                    """,
                    unsafe_allow_html=True
                )

    # ── TAB 2: PARAMETER EXPLORER (pH) ───────────────────────────────────────
    with tab_explorer:
        col_ex1, col_ex2 = st.columns([1.5, 2.5])

        with col_ex1:
            st.markdown(
                """
<div class="aqua-card" style="padding: 20px; margin-bottom: 16px;">
    <div class="card-subtitle">Current Average</div>
    <div class="metric-value" style="font-size: 36px; color: #111827; margin: 8px 0;">7.18</div>
    <span class="status-badge status-success">Normal</span>
    <div style="margin-top: 16px; font-size: 12px; color: #6B7280;">
        Ideal Range (WHO): <b style="color:#111827;">6.5 – 8.5</b>
    </div>
</div>

<div class="aqua-card" style="padding: 20px;">
    <div class="card-title">About pH</div>
    <p style="font-size: 12px; color: #6B7280; line-height: 1.5;">
        Measures acidity or alkalinity of water. It indicates how acidic or basic the water is on a scale of 0 to 14.
    </p>
    <div class="card-title" style="margin-top: 12px;">Health Impact</div>
    <p style="font-size: 12px; color: #6B7280; line-height: 1.5;">
        pH outside the desired range can cause irritation, corrosion, and taste or piping issues.
    </p>
    <div class="card-title" style="margin-top: 12px;">Recommendation</div>
    <p style="font-size: 12px; color: #22C55E; line-height: 1.5; font-weight: 500;">
        ✔ pH level is within the recommended range. No action required.
    </p>
</div>
                """,
                unsafe_allow_html=True
            )

        with col_ex2:
            with st.container(border=True):
                st.markdown('### pH Distribution')

                np.random.seed(42)
                ph_samples = np.random.normal(7.18, 0.4, 1000)

                fig_dist = px.histogram(
                    ph_samples, nbins=30,
                    color_discrete_sequence=['#1E88E5'],
                    labels={'value': 'pH Level'}
                )
                fig_dist.update_layout(
                    showlegend=False,
                    height=300,
                    margin=dict(t=10, b=30, l=30, r=10),
                    xaxis=dict(gridcolor='#E5E5E5'),
                    yaxis=dict(gridcolor='#E5E5E5'),
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)'
                )
                st.plotly_chart(fig_dist, use_container_width=True, config={'displayModeBar': False})

                st.markdown(
                    """
    <div style="background: #DCFCE7; border: 1px solid #86EFAC; padding: 12px; border-radius: 8px; font-size: 12px; color: #15803D; font-weight: 500;">
        🛡️ This parameter is within safe limits.
    </div>
                    """,
                    unsafe_allow_html=True
                )
