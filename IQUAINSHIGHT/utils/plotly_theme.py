"""
AquaInsights Plotly Theme
Standardized chart layout for consistent dashboard presentation.
"""

from __future__ import annotations

import plotly.graph_objects as go

PLOTLY_CONFIG: dict = {
    "displayModeBar": False,
    "responsive": True,
}

DEFAULT_HEIGHT: int = 220
COMPACT_HEIGHT: int = 180
GAUGE_HEIGHT: int = 130


def apply_aqua_layout(
    fig: go.Figure,
    *,
    height: int = DEFAULT_HEIGHT,
    show_legend: bool = False,
    legend_bottom: bool = False,
) -> go.Figure:
    """Apply consistent margins, fonts, and transparent backgrounds."""
    legend = dict(
        orientation="h",
        yanchor="bottom",
        y=-0.22 if legend_bottom else 1.02,
        xanchor="center",
        x=0.5,
        font=dict(family="Inter", size=10, color="#374151"),
    )

    fig.update_layout(
        height=height,
        margin=dict(t=8, b=28 if legend_bottom else 20, l=40, r=12),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter", size=10, color="#374151"),
        showlegend=show_legend,
        legend=legend if show_legend else None,
        autosize=True,
    )

    fig.update_xaxes(
        gridcolor="#F0F0F0",
        tickfont=dict(color="#374151", size=10),
        zeroline=False,
    )
    fig.update_yaxes(
        gridcolor="#F0F0F0",
        tickfont=dict(color="#374151", size=10),
        zeroline=False,
    )
    return fig
