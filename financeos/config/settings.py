"""
FinanceOS Configuration

Central configuration for the application.
"""

from pathlib import Path


class Config:
    """Application configuration."""

    PROJECT_NAME = "FinanceOS"
    VERSION = "0.1.0"
    AUTHOR = "Saurabh Singh"

    BASE_DIR = Path(__file__).resolve().parent.parent

    ASSETS_DIR = BASE_DIR / "assets"
    DOCS_DIR = BASE_DIR / "docs"
    NOTEBOOKS_DIR = BASE_DIR / "notebooks"

    DEFAULT_CURRENCY = "INR"
    DEFAULT_FORECAST_YEARS = 5

    DEBUG = True
    