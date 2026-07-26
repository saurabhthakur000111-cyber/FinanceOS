import streamlit as st
import yfinance as yf
import pandas as pd

from database.database import add_stock, get_portfolio

from analytics.portfolio_analytics import (
    calculate_returns,
    calculate_volatility,
    calculate_sharpe,
    calculate_beta,
    risk_score
)

from analytics.visuals import (
    sector_allocation_chart,
    performance_chart,
    risk_gauge
)
