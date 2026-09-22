"""
AquaInsights — Settings Page
User preferences & platform settings matching Image 1 (#14 Settings).
"""

import streamlit as st

def render() -> None:
    st.markdown('<div class="card-title" style="font-size: 18px; margin-bottom: 16px;">Customize your experience</div>', unsafe_allow_html=True)

    with st.container(border=True):
        # ── Appearance ──────────────────────────────────────────────────────────
        st.markdown('### Appearance')
        theme_choice = st.selectbox("Theme", ["Light", "Dark", "System Default"], index=0, key="sett_theme")

        st.markdown('<hr style="border: 0; border-top: 1px solid #E5E5E5; margin: 16px 0;"/>', unsafe_allow_html=True)

        # ── Language ────────────────────────────────────────────────────────────
        st.markdown('### Language')
        lang_choice = st.selectbox("Language", ["English (US)", "Spanish", "French", "German"], index=0, key="sett_lang")

        st.markdown('<hr style="border: 0; border-top: 1px solid #E5E5E5; margin: 16px 0;"/>', unsafe_allow_html=True)

        # ── Data Preferences ────────────────────────────────────────────────────
        st.markdown('### Data Preferences')
        col_d1, col_d2 = st.columns(2)
        with col_d1:
            st.number_input("Missing Value Threshold (%)", min_value=1, max_value=50, value=5, key="sett_miss_thresh")
        with col_d2:
            st.number_input("Outlier Threshold (IQR)", min_value=1.0, max_value=3.0, value=1.5, step=0.1, key="sett_iqr_thresh")

        st.markdown('<hr style="border: 0; border-top: 1px solid #E5E5E5; margin: 16px 0;"/>', unsafe_allow_html=True)

        # ── Export Preferences ──────────────────────────────────────────────────
        st.markdown('### Export Preferences')
        st.selectbox("Default Export Format", ["PDF Document", "CSV Dataset", "Excel Spreadsheet"], index=0, key="sett_export_fmt")

        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

        if st.button("Save Preferences", key="btn_save_settings", type="primary"):
            st.success("Preferences saved successfully!")
