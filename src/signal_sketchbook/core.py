"""Core workflow for Signal Sketchbook by Red@."""

PROJECT_NAME = "Signal Sketchbook"
DOMAIN_THEME = "visualization"


def build_snapshot() -> dict[str, str]:
    return {"project": PROJECT_NAME, "author": "Red@", "theme": DOMAIN_THEME}
