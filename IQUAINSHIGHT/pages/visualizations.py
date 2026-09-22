"""
AquaInsights — Visualizations Page
Interactive charts gallery matching Image 1 (#10 Visualizations).
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from services.csv_loader import CSVLoader

def render() -> None:
    loader = CSVLoader()
    df = loader.get_default_dataset()

    st.markdown('<div class="card-title" style="font-size: 18px; margin-bottom: 16px;">Interactive Data Visualizations</div>', unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["All Charts", "Distribution", "Relationship", "Trend", "Comparison"])

    with tab1:
        # 6-chart grid matching Image 1 #10
        r1c1, r1c2, r1c3 = st.columns(3)
        r2c1, r2c2, r2c3 = st.columns(3)

        with r1c1:
            with st.container(border=True):
                st.markdown('### pH Distribution')
                fig1 = px.histogram(df, x='pH', nbins=20, color_discrete_sequence=['#1E88E5'])
                fig1.update_layout(height=180, margin=dict(t=10, b=20, l=20, r=10), showlegend=False)
                st.plotly_chart(fig1, use_container_width=True, config={'displayModeBar': False})

        with r1c2:
            with st.container(border=True):
                st.markdown('### TDS vs Hardness')
                fig2 = px.scatter(df.head(200), x='Hardness', y='Solids', color_discrete_sequence=['#42A5F5'])
                fig2.update_layout(height=180, margin=dict(t=10, b=20, l=20, r=10), showlegend=False)
                st.plotly_chart(fig2, use_container_width=True, config={'displayModeBar': False})

        with r1c3:
            with st.container(border=True):
                st.markdown('### Water Quality Trend')
                fig3 = px.line(y=np.sin(np.linspace(0, 10, 30)) * 0.5 + 7.18, color_discrete_sequence=['#1E88E5'])
                fig3.update_layout(height=180, margin=dict(t=10, b=20, l=20, r=10), showlegend=False)
                st.plotly_chart(fig3, use_container_width=True, config={'displayModeBar': False})

        st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

        with r2c1:
            with st.container(border=True):
                st.markdown('### Water Quality Distribution')
                fig4 = px.pie(values=[4681, 593], names=['Safe', 'Unsafe'], hole=0.6, color_discrete_sequence=['#22C55E', '#F59E0B'])
                fig4.update_layout(height=180, margin=dict(t=10, b=20, l=20, r=10), showlegend=True)
                st.plotly_chart(fig4, use_container_width=True, config={'displayModeBar': False})

        with r2c2:
            with st.container(border=True):
                st.markdown('### Correlation Heatmap')
                fig5 = px.imshow(df.select_dtypes(include=[np.number]).corr(), color_continuous_scale='Blues')
                fig5.update_layout(height=180, margin=dict(t=10, b=20, l=20, r=10))
                st.plotly_chart(fig5, use_container_width=True, config={'displayModeBar': False})

        with r2c3:
            with st.container(border=True):
                st.markdown('### Turbidity Distribution')
                fig6 = px.box(df, y='Turbidity', color_discrete_sequence=['#A855F7'])
                fig6.update_layout(height=180, margin=dict(t=10, b=20, l=20, r=10))
                st.plotly_chart(fig6, use_container_width=True, config={'displayModeBar': False})

    with tab2:
        with st.container(border=True):
            st.markdown('### Detailed Distribution Charts')
            fig_dist_all = px.histogram(df, x='Turbidity', color='Potability', barmode='overlay', color_discrete_sequence=['#EF4444', '#22C55E'])
            fig_dist_all.update_layout(height=350)
            st.plotly_chart(fig_dist_all, use_container_width=True)

    with tab3:
        with st.container(border=True):
            st.markdown('### Relationship Scatter Matrix')
            fig_rel = px.scatter_matrix(df, dimensions=['pH', 'Hardness', 'Solids', 'Turbidity'], color='Potability', color_discrete_sequence=['#EF4444', '#22C55E'])
            fig_rel.update_layout(height=450)
            st.plotly_chart(fig_rel, use_container_width=True)

    with tab4:
        with st.container(border=True):
            st.markdown('### Parameter Time Series Trend')
            fig_trend_detail = px.line(df.head(100), y=['pH', 'Turbidity'], color_discrete_sequence=['#1E88E5', '#F59E0B'])
            fig_trend_detail.update_layout(height=350)
            st.plotly_chart(fig_trend_detail, use_container_width=True)

    with tab5:
        with st.container(border=True):
            st.markdown('### WHO Limits Comparison')
            avg_vals = df[['pH', 'Turbidity', 'Chloramines']].mean()
            fig_comp = px.bar(x=avg_vals.index, y=avg_vals.values, color=avg_vals.index, color_discrete_sequence=['#1E88E5', '#22C55E', '#A855F7'])
            fig_comp.update_layout(height=350)
            st.plotly_chart(fig_comp, use_container_width=True)
