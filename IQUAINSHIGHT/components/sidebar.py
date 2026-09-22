import streamlit as st
from streamlit_option_menu import option_menu
from utils.constants import NAV_ITEMS
from utils.theme import get_sidebar_menu_styles


def render_sidebar() -> str:
    # Render logo at top
    st.markdown(
        """<div class="sidebar-logo">
<div class="logo-icon">
<svg width="24" height="24" viewBox="0 0 24 24" fill="white">
<path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0L12 2.69z"/>
</svg>
</div>
<div class="logo-text">
<span class="aqua">AQUA</span><span class="insights">INSIGHTS</span>
</div>
</div>
<div class="sidebar-divider"></div>""",
        unsafe_allow_html=True,
    )

    labels = [item["label"] for item in NAV_ITEMS]
    icons = [item["icon"] for item in NAV_ITEMS]

    # Handle active selected index from session state
    default_idx = 0
    current_page = st.session_state.get("selected_page", "Dashboard")
    if current_page in labels:
        default_idx = labels.index(current_page)

    selected = option_menu(
        menu_title=None,
        options=labels,
        icons=icons,
        default_index=default_idx,
        styles=get_sidebar_menu_styles(),
        key="main_menu_nav",
    )

    st.session_state["selected_page"] = selected

    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)

    # Dataset Info Panel at bottom of sidebar matching Image 2
    dataset = st.session_state.get("dataset")
    file_name = st.session_state.get("dataset_name", "water_quality_2024.csv")
    uploaded_at = st.session_state.get("dataset_uploaded_at", "2 hours ago")

    if dataset is not None:
        rows = f"{len(dataset):,}"
        cols = str(len(dataset.columns))
    else:
        rows = "5,274"
        cols = "10"

    st.markdown(
        f"""<div class="dataset-info">
<div class="dataset-info-title">Dataset Info</div>
<div class="dataset-info-row">
<span class="dataset-info-label">File Name</span>
<span class="dataset-info-value" style="font-size:11px;">{file_name}</span>
</div>
<div class="dataset-info-row">
<span class="dataset-info-label">Total Rows</span>
<span class="dataset-info-value">{rows}</span>
</div>
<div class="dataset-info-row">
<span class="dataset-info-label">Total Columns</span>
<span class="dataset-info-value">{cols}</span>
</div>
<div class="dataset-info-row">
<span class="dataset-info-label">Last Uploaded</span>
<span class="dataset-info-value" style="font-size:11px;">{uploaded_at}</span>
</div>
</div>""",
        unsafe_allow_html=True,
    )

    if st.button("View Details", key="sidebar_view_details_btn", use_container_width=True):
        st.session_state["selected_page"] = "Dataset Overview"
        st.rerun()

    st.markdown('<div style="height:8px;"></div>', unsafe_allow_html=True)

    if st.button("🚪 Logout", key="sidebar_logout_btn", use_container_width=True):
        for k in ("logged_in", "user_email", "app_view"):
            st.session_state[k] = {"logged_in": False, "user_email": None, "app_view": "home"}[k]
        st.rerun()

    return selected
