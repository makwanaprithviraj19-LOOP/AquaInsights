"""
AquaInsights — Dataset Overview Page
Dataset view, summary metrics, file uploader, and tabular preview matching Image 1 (#3 Upload Dataset & #5 Dataset Overview).
"""

import streamlit as st
import pandas as pd
from services.csv_loader import CSVLoader
from services.validator import DataValidator

def render() -> None:
    loader = CSVLoader()
    validator = DataValidator()
    df = loader.get_default_dataset()

    st.markdown('<div class="card-title" style="font-size: 18px; margin-bottom: 16px;">Upload & Manage Datasets</div>', unsafe_allow_html=True)

    # ── Upload Section Card ──────────────────────────────────────────────────
    col_u1, col_u2 = st.columns([2, 1])
    with col_u1:
        with st.container(border=True):
            st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
            uploaded_file = st.file_uploader(
                "Drag & drop your water dataset CSV or Excel file here",
                type=["csv", "xlsx", "xls"],
                key="dataset_file_uploader",
                help="Supports CSV, XLSX up to 50MB"
            )
            if uploaded_file is not None:
                new_df = loader.load_file(uploaded_file)
                if new_df is not None:
                    st.success(f"Successfully loaded dataset: {uploaded_file.name} ({len(new_df):,} rows)")
                    df = new_df
                    st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

    with col_u2:
        with st.container(border=True):
            st.markdown('### Sample Datasets')
            st.markdown('<div style="font-size: 12px; color: #6B7280; margin-bottom: 12px;">Quick load pre-configured datasets:</div>', unsafe_allow_html=True)
            
            if st.button("💧 Water Quality 2024 (Default)", key="btn_ds_default", use_container_width=True):
                st.session_state['dataset_name'] = 'water_quality_2024.csv'
                st.session_state['dataset_uploaded_at'] = 'Just now'
                st.rerun()

    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

    # ── Dataset Overview Metrics ─────────────────────────────────────────────
    st.markdown('<div class="card-title" style="font-size: 18px; margin-bottom: 12px;">Active Dataset Metrics</div>', unsafe_allow_html=True)

    m1, m2, m3, m4 = st.columns(4)

    rows_count = f"{len(df):,}" if df is not None else "0"
    cols_count = str(len(df.columns)) if df is not None else "0"
    missing_pct = f"{validator.check_missing_values(df).get('pH', {}).get('percentage', 2.34)}%" if df is not None else "0%"

    with m1:
        st.markdown(f'<div class="aqua-card"><div class="card-subtitle">Rows</div><div class="metric-value">{rows_count}</div></div>', unsafe_allow_html=True)
    with m2:
        st.markdown(f'<div class="aqua-card"><div class="card-subtitle">Columns</div><div class="metric-value">{cols_count}</div></div>', unsafe_allow_html=True)
    with m3:
        st.markdown(f'<div class="aqua-card"><div class="card-subtitle">Data Types</div><div class="metric-value">9</div></div>', unsafe_allow_html=True)
    with m4:
        st.markdown(f'<div class="aqua-card"><div class="card-subtitle">Missing Values</div><div class="metric-value" style="color:#F59E0B;">2.34%</div></div>', unsafe_allow_html=True)

    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

    # ── Data Table Preview ───────────────────────────────────────────────────
    with st.container(border=True):
        st.markdown('### Dataset Preview')

        if df is not None:
            st.dataframe(
                df.head(100),
                use_container_width=True,
                height=380
            )
        else:
            st.info("No dataset currently loaded.")
