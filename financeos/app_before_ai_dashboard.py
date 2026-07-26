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


@st.cache_data(ttl=300)
def get_price(symbol):

    try:
        data = yf.Ticker(symbol)

        price = data.history(
            period="1d"
        )["Close"].iloc[-1]

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


st.subheader("➕ Add Stock Holding")


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
    buy_price = st.number_input(
        "Buy Price",
        min_value=1.0,
        value=2500.0
    )


if st.button("Add Stock"):

    add_stock(
        symbol,
        quantity,
        buy_price
    )

    st.success(
        "Stock added successfully"
    )


# -----------------------------
# Portfolio P&L Engine
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


    current_prices = []
    investments = []
    current_values = []
    profits = []


    for _, row in df.iterrows():

        current_price = get_price(
            row["Symbol"]
        )


        if current_price != "N/A":

            investment = (
                row["Quantity"]
                *
                row["Buy Price"]
            )


            current_value = (
                row["Quantity"]
                *
                current_price
            )


            profit = (
                current_value
                -
                investment
            )


        else:

            investment = 0
            current_value = 0
            profit = 0


        current_prices.append(current_price)
        investments.append(round(investment, 2))
        current_values.append(round(current_value, 2))
        profits.append(round(profit, 2))


    df["Current Price"] = current_prices
    df["Investment"] = investments
    df["Current Value"] = current_values
    df["P&L"] = profits


    st.dataframe(
        df,
        width="stretch"
    )


    total_investment = sum(investments)
    total_value = sum(current_values)
    total_profit = sum(profits)


    col1, col2, col3 = st.columns(3)


    with col1:
        st.metric(
            "Total Investment",
            f"₹{total_investment:,.2f}"
        )


    with col2:
        st.metric(
            "Current Value",
            f"₹{total_value:,.2f}"
        )


    with col3:
        st.metric(
            "Total P&L",
            f"₹{total_profit:,.2f}"
        )


else:

    st.info(
        "No stocks added yet"
    )
# -----------------------------
# Portfolio Analytics
# -----------------------------

st.header("📈 Portfolio Analytics")


if portfolio:

    symbols = df["Symbol"].tolist()


    returns = calculate_returns(symbols)


    avg_returns = returns.mean(axis=1)


    volatility = calculate_volatility(
        avg_returns
    )


    sharpe = calculate_sharpe(
        avg_returns
    )


    beta = calculate_beta(
        symbols[0]
    )


    score = risk_score(
        volatility,
        sharpe
    )


    col1, col2, col3, col4 = st.columns(4)


    with col1:
        st.metric(
            "Volatility",
            f"{volatility:.2%}"
        )


    with col2:
        st.metric(
            "Sharpe Ratio",
            round(sharpe,2)
        )


    with col3:
        st.metric(
            "Beta vs NIFTY",
            beta
        )


    with col4:
        st.metric(
            "Risk Score",
            f"{score}/100"
        )

# -----------------------------
# Footer
# -----------------------------

st.divider()

st.caption(
    "FinanceOS | AI Powered Financial Intelligence Platform"
)
