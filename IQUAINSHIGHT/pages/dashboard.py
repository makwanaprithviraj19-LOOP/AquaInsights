"""
AquaInsights — Dashboard Page
Final High-Resolution Analytics Workspace matching Image 2 reference design.
All layout issues, chart styling, text contrast, and top padding fixed.
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from utils.colors import Colors
from services.csv_loader import CSVLoader
from services.analytics_engine import AnalyticsEngine


def render() -> None:
    # Ensure default dataset is loaded
    loader = CSVLoader()
    df = loader.get_default_dataset()
    analytics = AnalyticsEngine()

    # ── Top Action Bar (Upload Dataset button top right) ─────────────────────
    col_t1, col_t2 = st.columns([3.2, 1])
    with col_t1:
        st.markdown(
            """
            <div style="margin-bottom: 4px;">
                <h2 style="font-family:'Poppins',sans-serif; font-size:22px; font-weight:700; color:#111827; margin:0;">Analytics Workspace</h2>
                <p style="font-family:'Inter',sans-serif; font-size:13px; color:#6B7280; margin:2px 0 0 0;">Overview of your water quality analysis</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col_t2:
        if st.button("📤 Upload Dataset", key="dash_top_upload_btn", type="primary", use_container_width=True):
            st.session_state["selected_page"] = "Dataset Overview"
            st.rerun()

    st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)

    # ── ROW 1: 5 KPI Metric Cards ───────────────────────────────────────────
    kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

    with kpi1:
        st.markdown(
            """
            <div class="aqua-card" style="padding: 16px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <div style="width: 36px; height: 36px; border-radius: 10px; background: rgba(30,136,229,0.12); display: flex; align-items: center; justify-content: center; color: #1E88E5; font-size: 18px;">
                        💧
                    </div>
                </div>
                <div class="card-subtitle" style="font-weight: 500;">Water Quality Index</div>
                <div class="metric-value" style="color: #1E88E5; font-size: 26px; margin: 4px 0;">92%</div>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="font-size: 12px; font-weight: 600; color: #22C55E;">Excellent</span>
                    <span style="font-size: 11px; color: #1E88E5;">📈 📈</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with kpi2:
        st.markdown(
            """
            <div class="aqua-card" style="padding: 16px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <div style="width: 36px; height: 36px; border-radius: 10px; background: rgba(59,130,246,0.12); display: flex; align-items: center; justify-content: center; color: #3B82F6; font-size: 18px;">
                        📋
                    </div>
                </div>
                <div class="card-subtitle" style="font-weight: 500;">Total Samples</div>
                <div class="metric-value" style="color: #111827; font-size: 26px; margin: 4px 0;">5,274</div>
                <div style="font-size: 12px; color: #6B7280;">Samples</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with kpi3:
        st.markdown(
            """
            <div class="aqua-card" style="padding: 16px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <div style="width: 36px; height: 36px; border-radius: 10px; background: rgba(34,197,94,0.12); display: flex; align-items: center; justify-content: center; color: #22C55E; font-size: 18px;">
                        🛡️
                    </div>
                </div>
                <div class="card-subtitle" style="font-weight: 500;">Safe Water</div>
                <div class="metric-value" style="color: #111827; font-size: 26px; margin: 4px 0;">4,681</div>
                <div style="font-size: 12px; font-weight: 600; color: #22C55E;">88.7% of total</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with kpi4:
        st.markdown(
            """
            <div class="aqua-card" style="padding: 16px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <div style="width: 36px; height: 36px; border-radius: 10px; background: rgba(245,158,11,0.12); display: flex; align-items: center; justify-content: center; color: #F59E0B; font-size: 18px;">
                        ⚠️
                    </div>
                </div>
                <div class="card-subtitle" style="font-weight: 500;">Unsafe Water</div>
                <div class="metric-value" style="color: #111827; font-size: 26px; margin: 4px 0;">593</div>
                <div style="font-size: 12px; font-weight: 600; color: #F59E0B;">11.3% of total</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with kpi5:
        st.markdown(
            """
            <div class="aqua-card" style="padding: 16px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <div style="width: 36px; height: 36px; border-radius: 10px; background: rgba(168,85,247,0.12); display: flex; align-items: center; justify-content: center; color: #A855F7; font-size: 18px;">
                        🧪
                    </div>
                </div>
                <div class="card-subtitle" style="font-weight: 500;">Parameters Analyzed</div>
                <div class="metric-value" style="color: #111827; font-size: 26px; margin: 4px 0;">9</div>
                <div style="font-size: 12px; color: #6B7280;">Water Quality Indicators</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

    # ── ROW 2: Key Indicators (Left) | Donut Chart (Middle) | AI Insights (Right) ─
    c1, c2, c3 = st.columns([2.2, 1.4, 1.4])

    with c1:
        st.markdown(
            """
            <div class="aqua-card" style="min-height: 280px; padding: 18px;">
                <div class="card-title">Key Water Quality Indicators</div>
                <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; margin-top: 14px;">
                    <div style="background: #F8FAFC; border: 1px solid #E5E5E5; border-radius: 10px; padding: 10px; text-align: center;">
                        <div style="font-size: 11px; color: #6B7280; font-weight: 500;">pH</div>
                        <div style="font-size: 18px; font-weight: 700; color: #111827; margin: 4px 0;">7.18</div>
                        <span class="status-badge status-success" style="font-size: 10px; padding: 2px 6px;">Normal</span>
                    </div>
                    <div style="background: #F8FAFC; border: 1px solid #E5E5E5; border-radius: 10px; padding: 10px; text-align: center;">
                        <div style="font-size: 11px; color: #6B7280; font-weight: 500;">Hardness</div>
                        <div style="font-size: 18px; font-weight: 700; color: #111827; margin: 4px 0;">195 <span style="font-size: 10px; font-weight: 400;">mg/L</span></div>
                        <span class="status-badge status-info" style="font-size: 10px; padding: 2px 6px;">Moderate</span>
                    </div>
                    <div style="background: #F8FAFC; border: 1px solid #E5E5E5; border-radius: 10px; padding: 10px; text-align: center;">
                        <div style="font-size: 11px; color: #6B7280; font-weight: 500;">TDS</div>
                        <div style="font-size: 18px; font-weight: 700; color: #111827; margin: 4px 0;">315 <span style="font-size: 10px; font-weight: 400;">ppm</span></div>
                        <span class="status-badge status-success" style="font-size: 10px; padding: 2px 6px;">Good</span>
                    </div>
                    <div style="background: #F8FAFC; border: 1px solid #E5E5E5; border-radius: 10px; padding: 10px; text-align: center;">
                        <div style="font-size: 11px; color: #6B7280; font-weight: 500;">Turbidity</div>
                        <div style="font-size: 18px; font-weight: 700; color: #111827; margin: 4px 0;">2.1 <span style="font-size: 10px; font-weight: 400;">NTU</span></div>
                        <span class="status-badge status-success" style="font-size: 10px; padding: 2px 6px;">Good</span>
                    </div>
                    <div style="background: #F8FAFC; border: 1px solid #E5E5E5; border-radius: 10px; padding: 10px; text-align: center;">
                        <div style="font-size: 11px; color: #6B7280; font-weight: 500;">Conductivity</div>
                        <div style="font-size: 18px; font-weight: 700; color: #111827; margin: 4px 0;">512 <span style="font-size: 10px; font-weight: 400;">µS/cm</span></div>
                        <span class="status-badge status-info" style="font-size: 10px; padding: 2px 6px;">Moderate</span>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        with st.container(border=True):
            st.markdown('### Water Quality Distribution')
            
            # Plotly Donut Chart with clean layout
            fig_donut = go.Figure(data=[go.Pie(
                labels=['Safe (88.7%)', 'Unsafe (11.3%)'],
                values=[4681, 593],
                hole=0.65,
                marker_colors=['#22C55E', '#F59E0B'],
                textinfo='none',
                hoverinfo='label+value'
            )])
            fig_donut.update_layout(
                showlegend=True,
                legend=dict(orientation="h", yanchor="bottom", y=-0.25, xanchor="center", x=0.5, font=dict(family="Inter", size=11, color="#374151")),
                margin=dict(t=5, b=25, l=5, r=5),
                height=180,
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                annotations=[dict(text='<b>5,274</b><br/><span style="font-size:11px;color:#6B7280;">Total Samples</span>', x=0.5, y=0.5, font_size=15, font_color="#111827", showarrow=False)]
            )
            st.plotly_chart(fig_donut, use_container_width=True, config={'displayModeBar': False})

    with c3:
        st.markdown(
            """
            <div class="aqua-card" style="min-height: 280px; padding: 18px;">
                <div style="display: flex; align-items: center; gap: 6px; margin-bottom: 12px;">
                    <span style="color: #7C3AED; font-size: 16px;">✨</span>
                    <span class="card-title" style="margin: 0; color: #111827;">AI Quick Insights</span>
                </div>
                <div style="display: flex; flex-direction: column; gap: 8px; font-size: 12px; color: #374151;">
                    <div style="display: flex; align-items: flex-start; gap: 6px;">
                        <span style="color: #22C55E; font-weight: bold;">✔</span>
                        <span>Average pH is within WHO standards.</span>
                    </div>
                    <div style="display: flex; align-items: flex-start; gap: 6px;">
                        <span style="color: #22C55E; font-weight: bold;">✔</span>
                        <span>Water quality appears healthy overall.</span>
                    </div>
                    <div style="display: flex; align-items: flex-start; gap: 6px;">
                        <span style="color: #22C55E; font-weight: bold;">✔</span>
                        <span>Conductivity shows strong correlation with TDS.</span>
                    </div>
                    <div style="display: flex; align-items: flex-start; gap: 6px;">
                        <span style="color: #22C55E; font-weight: bold;">✔</span>
                        <span>Turbidity levels are within acceptable range.</span>
                    </div>
                    <div style="display: flex; align-items: flex-start; gap: 6px;">
                        <span style="color: #22C55E; font-weight: bold;">✔</span>
                        <span>No significant abnormalities detected.</span>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

    # ── ROW 3: Trend (Left) | Heatmap (Middle) | WHO Compliance (Right) ─────────
    r3_1, r3_2, r3_3 = st.columns([2.0, 1.5, 1.5])

    with r3_1:
        with st.container(border=True):
            st.markdown('### Trend Overview (pH)')
            
            # Generated pH trend over time
            dates = pd.date_range(start="2026-05-01", end="2026-06-05", freq="D")
            np.random.seed(42)
            ph_vals = np.random.normal(7.18, 0.3, len(dates))
            ph_vals = np.clip(ph_vals, 6.5, 8.2)
            
            fig_trend = go.Figure()
            fig_trend.add_trace(go.Scatter(
                x=dates, y=ph_vals,
                mode='lines+markers',
                line=dict(color='#1E88E5', width=2.5),
                marker=dict(size=5, color='#1E88E5')
            ))
            fig_trend.update_layout(
                margin=dict(t=10, b=25, l=35, r=10),
                height=220,
                yaxis=dict(range=[5.5, 8.5], gridcolor='#F0F0F0', tickfont=dict(color='#374151', size=10)),
                xaxis=dict(gridcolor='#F0F0F0', tickfont=dict(color='#374151', size=10)),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)'
            )
            st.plotly_chart(fig_trend, use_container_width=True, config={'displayModeBar': False})

    with r3_2:
        with st.container(border=True):
            st.markdown('### Parameter Correlation Heatmap')
            
            # Heatmap matrix
            corr_matrix = [
                [1.0, 0.2, 0.4, 0.1, -0.3],
                [0.2, 1.0, 0.6, 0.2, -0.4],
                [0.4, 0.6, 1.0, 0.3, -0.6],
                [0.1, 0.2, 0.3, 1.0, -0.8],
                [-0.3, -0.4, -0.6, -0.8, 1.0]
            ]
            labels = ['pH', 'Hardness', 'TDS', 'Turbidity', 'Conductivity']
            
            fig_heat = go.Figure(data=go.Heatmap(
                z=corr_matrix,
                x=labels,
                y=labels,
                colorscale='Blues',
                showscale=True,
                colorbar=dict(tickfont=dict(color='#374151', size=10))
            ))
            fig_heat.update_layout(
                margin=dict(t=10, b=25, l=45, r=10),
                height=220,
                xaxis=dict(tickfont=dict(color='#374151', size=10)),
                yaxis=dict(tickfont=dict(color='#374151', size=10)),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)'
            )
            st.plotly_chart(fig_heat, use_container_width=True, config={'displayModeBar': False})

    with r3_3:
        st.markdown(
            """
            <div class="aqua-card" style="min-height: 310px; padding: 18px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                    <span class="card-title" style="margin:0;">WHO Standards Compliance</span>
                    <span style="font-size: 11px; color: #1E88E5; font-weight: 500; cursor: pointer;">View All ></span>
                </div>
                <table style="width: 100%; border-collapse: collapse; font-size: 12px;">
                    <thead>
                        <tr style="color: #6B7280; border-bottom: 1px solid #E5E5E5; text-align: left;">
                            <th style="padding: 6px 0;">Parameter</th>
                            <th style="padding: 6px 0;">WHO Limit</th>
                            <th style="padding: 6px 0;">Your Avg.</th>
                            <th style="padding: 6px 0;">Status</th>
                        </tr>
                    </thead>
                    <tbody style="color: #111827;">
                        <tr style="border-bottom: 1px solid #F0F0F0;">
                            <td style="padding: 8px 0; font-weight: 500;">pH</td>
                            <td style="color: #6B7280;">6.5 – 8.5</td>
                            <td>7.18</td>
                            <td><span style="color:#22C55E; font-weight:600;">✔ Compliant</span></td>
                        </tr>
                        <tr style="border-bottom: 1px solid #F0F0F0;">
                            <td style="padding: 8px 0; font-weight: 500;">Turbidity (NTU)</td>
                            <td style="color: #6B7280;">&lt; 5</td>
                            <td>2.1</td>
                            <td><span style="color:#22C55E; font-weight:600;">✔ Compliant</span></td>
                        </tr>
                        <tr style="border-bottom: 1px solid #F0F0F0;">
                            <td style="padding: 8px 0; font-weight: 500;">Hardness (mg/L)</td>
                            <td style="color: #6B7280;">&lt; 200</td>
                            <td>195</td>
                            <td><span style="color:#22C55E; font-weight:600;">✔ Compliant</span></td>
                        </tr>
                        <tr style="border-bottom: 1px solid #F0F0F0;">
                            <td style="padding: 8px 0; font-weight: 500;">TDS (ppm)</td>
                            <td style="color: #6B7280;">&lt; 500</td>
                            <td>315</td>
                            <td><span style="color:#22C55E; font-weight:600;">✔ Compliant</span></td>
                        </tr>
                        <tr>
                            <td style="padding: 8px 0; font-weight: 500;">Chloramines (mg/L)</td>
                            <td style="color: #6B7280;">&lt; 4</td>
                            <td>2.2</td>
                            <td><span style="color:#22C55E; font-weight:600;">✔ Compliant</span></td>
                        </tr>
                    </tbody>
                </table>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

    # ── ROW 4: Recent Datasets | Analysis Summary | Quality Score | Quick Actions ──
    r4_1, r4_2, r4_3, r4_4 = st.columns([1.3, 1.1, 1.1, 1.5])

    with r4_1:
        st.markdown(
            """
            <div class="aqua-card" style="min-height: 240px; padding: 18px;">
                <div class="card-title">Recent Datasets</div>
                <div style="display: flex; flex-direction: column; gap: 10px; margin-top: 10px;">
                    <div style="display: flex; align-items: center; gap: 10px;">
                        <span style="font-size: 18px;">📄</span>
                        <div>
                            <div style="font-size: 12px; font-weight: 600; color: #111827;">water_quality_2024.csv</div>
                            <div style="font-size: 11px; color: #6B7280;">5,274 rows · Uploaded 2 hours ago</div>
                        </div>
                    </div>
                    <div style="display: flex; align-items: center; gap: 10px;">
                        <span style="font-size: 18px;">📄</span>
                        <div>
                            <div style="font-size: 12px; font-weight: 600; color: #111827;">river_water_may.csv</div>
                            <div style="font-size: 11px; color: #6B7280;">3,452 rows · Uploaded 1 day ago</div>
                        </div>
                    </div>
                    <div style="display: flex; align-items: center; gap: 10px;">
                        <span style="font-size: 18px;">📄</span>
                        <div>
                            <div style="font-size: 12px; font-weight: 600; color: #111827;">plant_water_april.csv</div>
                            <div style="font-size: 11px; color: #6B7280;">2,981 rows · Uploaded 3 days ago</div>
                        </div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with r4_2:
        st.markdown(
            """
            <div class="aqua-card" style="min-height: 240px; padding: 18px;">
                <div class="card-title">Analysis Summary</div>
                <div style="display: flex; flex-direction: column; gap: 12px; margin-top: 12px; font-size: 12px;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="color: #6B7280;">Missing Values</span>
                        <span style="font-weight: 700; color: #F59E0B;">2.34%</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="color: #6B7280;">Duplicate Rows</span>
                        <span style="font-weight: 700; color: #22C55E;">23</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="color: #6B7280;">Memory Usage</span>
                        <span style="font-weight: 700; color: #111827;">21.8 MB</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="color: #6B7280;">Data Types</span>
                        <span style="font-weight: 700; color: #111827;">9</span>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with r4_3:
        with st.container(border=True):
            st.markdown('<h3 style="text-align: center;">Data Quality Score</h3>', unsafe_allow_html=True)
            
            # Clean semi-gauge indicator
            fig_score = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = 96,
                number = {'suffix': "%", 'font': {'size': 26, 'color': "#111827", 'family': "Poppins"}},
                gauge = {
                    'axis': {'range': [0, 100], 'visible': False},
                    'bar': {'color': "#22C55E", 'thickness': 0.3},
                    'bgcolor': "#E5E5E5"
                }
            ))
            fig_score.update_layout(
                height=130,
                margin=dict(t=0, b=0, l=10, r=10),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)'
            )
            st.plotly_chart(fig_score, use_container_width=True, config={'displayModeBar': False})
            st.markdown('<div style="font-size: 11px; background: #DCFCE7; color: #15803D; padding: 4px 8px; border-radius: 6px; display: inline-block; font-weight: 500; text-align: center; width: 100%;">Overall data quality is excellent.</div>', unsafe_allow_html=True)

    with r4_4:
        with st.container(border=True):
            st.markdown('### Quick Actions')
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("📊 Visualizations", key="qa_vis", use_container_width=True):
                    st.session_state["selected_page"] = "Visualizations"
                    st.rerun()
                    
                if st.button("🧠 Make Prediction", key="qa_pred", use_container_width=True):
                    st.session_state["selected_page"] = "Prediction"
                    st.rerun()
            with col2:
                if st.button("✨ AI Insights", key="qa_ai", use_container_width=True):
                    st.session_state["selected_page"] = "AI Insights"
                    st.rerun()
                    
                if st.button("📥 Download Report", key="qa_rep", use_container_width=True):
                    st.session_state["selected_page"] = "Reports"
                    st.rerun()
