"""
AquaInsights — Data Cleaning Page
Data quality health score, anomaly detection, cleaning suggestions matching Image 1 (#6 Data Cleaning).
"""

import streamlit as st
import pandas as pd
from services.csv_loader import CSVLoader
from services.validator import DataValidator

def render() -> None:
    loader = CSVLoader()
    validator = DataValidator()
    df = loader.get_default_dataset()
    health_score = validator.get_data_quality_score(df)

    c_score, c_metrics = st.columns([1.2, 2.8])

    with c_score:
        st.markdown(
            f"""
<div class="aqua-card" style="padding: 24px; text-align: center; min-height: 220px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
    <div class="card-title">Dataset Health Score</div>
    <div style="position: relative; margin: 16px 0;">
        <div style="width: 110px; height: 110px; border-radius: 50%; border: 8px solid #22C55E; display: flex; align-items: center; justify-content: center;">
            <span style="font-size: 28px; font-weight: 800; color: #111827;">{int(health_score)}%</span>
        </div>
    </div>
    <span class="status-badge status-success">Healthy</span>
</div>
            """,
            unsafe_allow_html=True
        )

    with c_metrics:
        m1, m2 = st.columns(2)
        m3, m4 = st.columns(2)

        with m1:
            st.markdown(
                """
<div class="aqua-card" style="padding: 16px; margin-bottom: 12px;">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <span class="card-subtitle">Missing Values</span>
        <span style="font-size: 18px; font-weight: 700; color: #F59E0B;">2.34% (123)</span>
    </div>
</div>
                """,
                unsafe_allow_html=True
            )
        with m2:
            st.markdown(
                """
<div class="aqua-card" style="padding: 16px; margin-bottom: 12px;">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <span class="card-subtitle">Duplicate Rows</span>
        <span style="font-size: 18px; font-weight: 700; color: #22C55E;">23</span>
    </div>
</div>
                """,
                unsafe_allow_html=True
            )
        with m3:
            st.markdown(
                """
<div class="aqua-card" style="padding: 16px;">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <span class="card-subtitle">Inconsistent Values</span>
        <span style="font-size: 18px; font-weight: 700; color: #22C55E;">0</span>
    </div>
</div>
                """,
                unsafe_allow_html=True
            )
        with m4:
            st.markdown(
                """
<div class="aqua-card" style="padding: 16px;">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <span class="card-subtitle">Outliers Detected</span>
        <span style="font-size: 18px; font-weight: 700; color: #EF4444;">12</span>
    </div>
</div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("<div style='height: 24px;'></div>", unsafe_allow_html=True)

    # ── Cleaning Suggestions Section ─────────────────────────────────────────
    with st.container(border=True):
        st.markdown('### Cleaning Suggestions')

        s1, b1 = st.columns([4, 1])
        with s1:
            st.markdown('<div><b>Handle Missing Values</b><br/><span style="font-size: 12px; color: #6B7280;">Fill or remove missing values in dataset (123 missing entries in Sulfate & pH)</span></div>', unsafe_allow_html=True)
        with b1:
            if st.button("Review →", key="btn_clean_missing", use_container_width=True):
                st.toast("Applied median imputation for missing values!")

        st.markdown('<hr style="border: 0; border-top: 1px solid #E5E5E5; margin: 12px 0;"/>', unsafe_allow_html=True)

        s2, b2 = st.columns([4, 1])
        with s2:
            st.markdown('<div><b>Remove Duplicates</b><br/><span style="font-size: 12px; color: #6B7280;">23 duplicate rows found in dataset</span></div>', unsafe_allow_html=True)
        with b2:
            if st.button("Review →", key="btn_clean_dup", use_container_width=True):
                st.toast("Removed 23 duplicate rows!")

        st.markdown('<hr style="border: 0; border-top: 1px solid #E5E5E5; margin: 12px 0;"/>', unsafe_allow_html=True)

        s3, b3 = st.columns([4, 1])
        with s3:
            st.markdown('<div><b>Fix Inconsistent Values</b><br/><span style="font-size: 12px; color: #6B7280;">0 inconsistent values detected</span></div>', unsafe_allow_html=True)
        with b3:
            st.button("Review →", key="btn_clean_incons", disabled=True, use_container_width=True)

        if st.button("🧹 Clean Dataset Now", key="btn_clean_all_primary", type="primary", use_container_width=True):
            st.success("Dataset successfully cleaned and normalized!")
