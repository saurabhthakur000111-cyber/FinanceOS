import streamlit as st
import yfinance as yf
import pandas as pd

from database.database import add_stock, get_portfolio


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="FinanceOS",
    page_icon="📈",
    layout="wide"
)


# -----------------------------
# Header
# -----------------------------

st.title("📈 FinanceOS")
st.subheader("AI Powered Financial Intelligence Platform")


# -----------------------------
# Market Overview
# -----------------------------

st.header("🌎 Market Overview")


def get_price(symbol):
    try:
        data = yf.Ticker(symbol)
        price = data.history(period="1d")["Close"].iloc[-1]
        return round(float(price), 2)

    except Exception:
        return "N/A"


col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "NIFTY 50",
        get_price("^NSEI")
    )

with col2:
    st.metric(
        "SENSEX",
        get_price("^BSESN")
    )

with col3:
    st.metric(
        "RELIANCE",
        get_price("RELIANCE.NS")
    )

with col4:
    st.metric(
        "TCS",
        get_price("TCS.NS")
    )


# -----------------------------
# Portfolio Intelligence
# -----------------------------

st.header("💼 Portfolio Intelligence")


st.subheader("📁 Add Stock Holding")


col1, col2, col3 = st.columns(3)


with col1:
    symbol = st.text_input(
        "Stock Symbol",
        "RELIANCE.NS"
    )


with col2:
    quantity = st.number_input(
        "Quantity",
        min_value=1,
        value=10
    )


with col3:
    price = st.number_input(
        "Buy Price",
        min_value=1.0,
        value=2500.0
    )


if st.button("➕ Add Stock"):

    add_stock(
        symbol,
        quantity,
        price
    )

    st.success(
        "Stock added successfully"
    )


# -----------------------------
# Display Portfolio
# -----------------------------

st.subheader("📊 Current Holdings")


portfolio = get_portfolio()


if portfolio:

    df = pd.DataFrame(
        portfolio,
        columns=[
            "ID",
            "Symbol",
            "Quantity",
            "Buy Price"
        ]
    )

    st.dataframe(
        df,
        width="stretch"
    )


else:

    st.info(
        "No stocks added yet"
    )


# -----------------------------
# Footer
# -----------------------------

st.divider()

st.caption(
    "FinanceOS | AI Powered Financial Intelligence Platform"
)