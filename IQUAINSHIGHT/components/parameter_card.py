import streamlit as st

def render_parameter_card(
    name: str,
    value: str,
    unit: str,
    status: str = "Normal",
    status_type: str = "success",
) -> None:
    html = f"""
<div class="aqua-card" style="display: flex; align-items: center; justify-content: space-between; padding: 16px 20px;">
    <div>
        <div class="card-subtitle" style="margin-bottom: 4px;">{name}</div>
        <div style="display: flex; align-items: baseline; gap: 4px;">
            <span class="metric-value" style="font-size: 24px;">{value}</span>
            <span class="metric-label">{unit}</span>
        </div>
    </div>
    <span class="status-badge status-{status_type}">{status}</span>
</div>
    """
    st.markdown(html, unsafe_allow_html=True)
