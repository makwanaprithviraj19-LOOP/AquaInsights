"""
AquaInsights — Analytics Page
Statistical analysis, summary statistics table, and correlation matrix matching Image 1 (#9 Analytics).
"""

import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from services.csv_loader import CSVLoader
from services.analytics_engine import AnalyticsEngine

def render() -> None:
    loader = CSVLoader()
    analytics = AnalyticsEngine()
    df = loader.get_default_dataset()

    st.markdown('<div class="card-title" style="font-size: 18px; margin-bottom: 16px;">Statistical Analysis of Dataset</div>', unsafe_allow_html=True)

    col_stat, col_corr = st.columns([1.8, 1.2])

    with col_stat:
        with st.container(border=True):
            st.markdown('### Summary Statistics')

            summary_df = analytics.compute_summary_statistics(df)
            if not summary_df.empty:
                st.dataframe(
                    summary_df.style.format("{:.2f}"),
                    use_container_width=True,
                    height=340
                )
            else:
                st.info("No numeric data available for statistics.")

    with col_corr:
        with st.container(border=True):
            st.markdown('### Correlation Matrix')

            corr_df = analytics.compute_correlations(df)
            if not corr_df.empty:
                fig_corr = px.imshow(
                    corr_df,
                    text_auto=True,
                    color_continuous_scale='RdBu_r',
                    aspect="auto"
                )
                fig_corr.update_layout(
                    height=340,
                    margin=dict(t=10, b=10, l=10, r=10),
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)'
                )
                st.plotly_chart(fig_corr, use_container_width=True, config={'displayModeBar': False})
            else:
                st.info("No correlation data available.")
