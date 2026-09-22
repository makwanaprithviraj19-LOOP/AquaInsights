"""
AquaInsights UI Helpers
Shared presentation-layer utilities for cards, HTML, and layout.
"""

from __future__ import annotations

from contextlib import contextmanager
from typing import Generator

import streamlit as st
import streamlit.components.v1 as components


@contextmanager
def aqua_card(title: str | None = None) -> Generator[None, None, None]:
    """
    Render a bordered card that correctly wraps Streamlit widgets.

    Uses st.container(border=True) instead of open/close HTML divs,
    which do not wrap Streamlit elements and leak raw </div> text.
    """
    with st.container(border=True):
        if title:
            st.markdown(
                f'<div class="card-title" style="margin-bottom:8px;">{title}</div>',
                unsafe_allow_html=True,
            )
        yield


def render_html(html: str) -> None:
    """Render an HTML block safely."""
    st.markdown(html, unsafe_allow_html=True)


def render_html_component(html: str, height: int = 600) -> None:
    """Render complex HTML/CSS in an isolated iframe (login panels, etc.)."""
    components.html(
        f"<!DOCTYPE html><html><head><meta charset='utf-8'/></head><body style='margin:0;padding:0;'>{html}</body></html>",
        height=height,
        scrolling=False,
    )
