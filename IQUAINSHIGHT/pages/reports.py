"""
AquaInsights — Reports Page
PDF report generator & live document preview matching Image 1 (#13 Report Generator).
"""

import streamlit as st
import plotly.express as px
from services.report_engine import ReportEngine
from services.csv_loader import CSVLoader

def render() -> None:
    rep_engine = ReportEngine()
    loader = CSVLoader()
    df = loader.get_default_dataset()

    st.markdown('<div class="card-title" style="font-size: 18px; margin-bottom: 16px;">Report Generator</div>', unsafe_allow_html=True)

    col_config, col_preview = st.columns([1.2, 1.8])

    with col_config:
        with st.container(border=True):
            st.markdown('### Select Report Type')

            report_type = st.radio(
                "",
                options=["Summary Report (Overview of key insights & metrics)", "Detailed Report (In-depth analysis with charts)", "Custom Report (Select parameters to include)"],
                index=0,
                key="rep_type_select"
            )

            st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)
            st.markdown('<div class="card-title" style="font-size: 13px;">Export Formats</div>', unsafe_allow_html=True)

            pdf_bytes = rep_engine.generate_pdf_report(df)
            csv_bytes = rep_engine.generate_csv_export(df)

            c_pdf, c_csv = st.columns(2)
            with c_pdf:
                st.download_button(
                    label="📄 Generate PDF",
                    data=pdf_bytes,
                    file_name="AquaInsights_Water_Report.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                    type="primary"
                )
            with c_csv:
                st.download_button(
                    label="📊 Export CSV",
                    data=csv_bytes,
                    file_name="AquaInsights_Water_Data.csv",
                    mime="text/csv",
                    use_container_width=True
                )

    with col_preview:
        st.markdown(
            """
<div class="aqua-card" style="padding: 24px; min-height: 460px;">
    <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #E5E5E5; padding-bottom: 12px; margin-bottom: 16px;">
        <div>
            <div style="font-size: 16px; font-weight: 700; color: #1E88E5;">AquaInsights</div>
            <div style="font-size: 11px; color: #6B7280;">Water Quality Analysis Report Preview</div>
        </div>
        <span class="status-badge status-success">Ready to Export</span>
    </div>

    <div style="text-align: center; margin: 20px 0;">
        <div style="font-size: 12px; color: #6B7280;">OVERALL WATER HEALTH SCORE</div>
        <div style="font-size: 32px; font-weight: 800; color: #22C55E; margin: 4px 0;">92%</div>
        <div style="font-size: 11px; color: #6B7280;">88.7% Safe Water Compliance</div>
    </div>

    <div style="border: 1px solid #E5E5E5; border-radius: 8px; padding: 12px; margin-top: 16px;">
        <div style="font-size: 12px; font-weight: 600; color: #111827; margin-bottom: 8px;">Parameters Summary</div>
        <div style="display: flex; justify-content: space-between; font-size: 11px; color: #6B7280; border-bottom: 1px solid #F0F0F0; padding: 4px 0;">
            <span>pH (Avg: 7.18)</span>
            <span style="color:#22C55E; font-weight:600;">Compliant</span>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 11px; color: #6B7280; border-bottom: 1px solid #F0F0F0; padding: 4px 0;">
            <span>Turbidity (Avg: 2.1 NTU)</span>
            <span style="color:#22C55E; font-weight:600;">Compliant</span>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 11px; color: #6B7280; padding: 4px 0;">
            <span>Hardness (Avg: 195 mg/L)</span>
            <span style="color:#22C55E; font-weight:600;">Compliant</span>
        </div>
    </div>
</div>
            """,
            unsafe_allow_html=True
        )
