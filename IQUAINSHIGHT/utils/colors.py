"""
AquaInsights Color Palette
Centralized color definitions for consistent theming across the application.
"""


class Colors:
    """Application-wide color constants matching the approved design system."""

    # ── Backgrounds ──────────────────────────────────────────────────────
    BACKGROUND = "#F8FAFC"
    SIDEBAR = "#14213D"
    SIDEBAR_DARK = "#0D1B2A"
    SIDEBAR_HOVER = "#1E2A4A"
    CARD = "#FFFFFF"

    # ── Primary ──────────────────────────────────────────────────────────
    PRIMARY_BLUE = "#1E88E5"
    SECONDARY_BLUE = "#42A5F5"
    HIGHLIGHT = "#FCA311"

    # ── Borders ──────────────────────────────────────────────────────────
    BORDER = "#E5E5E5"
    BORDER_LIGHT = "#F0F0F0"

    # ── Text ─────────────────────────────────────────────────────────────
    TEXT_PRIMARY = "#111827"
    TEXT_SECONDARY = "#6B7280"
    TEXT_LIGHT = "#9CA3AF"
    TEXT_WHITE = "#FFFFFF"
    TEXT_SIDEBAR = "#CBD5E1"
    TEXT_MUTED = "#D1D5DB"

    # ── Status ───────────────────────────────────────────────────────────
    SUCCESS = "#22C55E"
    WARNING = "#F59E0B"
    DANGER = "#EF4444"
    INFO = "#3B82F6"

    # ── Gradients ────────────────────────────────────────────────────────
    GRADIENT_BLUE = "linear-gradient(135deg, #1E88E5 0%, #42A5F5 100%)"
    GRADIENT_DARK = "linear-gradient(180deg, #14213D 0%, #0D1B2A 100%)"
    GRADIENT_SUCCESS = "linear-gradient(135deg, #22C55E 0%, #16A34A 100%)"
    GRADIENT_WARNING = "linear-gradient(135deg, #F59E0B 0%, #D97706 100%)"
    GRADIENT_DANGER = "linear-gradient(135deg, #EF4444 0%, #DC2626 100%)"

    # ── Shadows ──────────────────────────────────────────────────────────
    SHADOW_SM = "0 1px 2px rgba(0, 0, 0, 0.05)"
    SHADOW_MD = "0 4px 6px -1px rgba(0, 0, 0, 0.1)"
    SHADOW_LG = "0 10px 15px -3px rgba(0, 0, 0, 0.1)"
    SHADOW_CARD = "0 1px 3px rgba(0, 0, 0, 0.08)"
    SHADOW_BLUE = "0 4px 14px rgba(30, 136, 229, 0.35)"

    # ── Opacity Layers ───────────────────────────────────────────────────
    OVERLAY_LIGHT = "rgba(255, 255, 255, 0.06)"
    OVERLAY_MEDIUM = "rgba(255, 255, 255, 0.1)"
    OVERLAY_BORDER = "rgba(255, 255, 255, 0.08)"
