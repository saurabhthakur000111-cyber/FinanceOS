import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.express as px


st.set_page_config(
    page_title="Portfolio Optimizer",
    page_icon="📈",
    layout="wide"
)


st.title("📈 FinanceOS Portfolio Optimizer")

st.write(
    "Markowitz Mean-Variance Portfolio Optimization"
)


stocks_input = st.text_input(
    "Enter stock symbols separated by commas",
    "RELIANCE.NS,TCS.NS,INFY.NS,HDFCBANK.NS"
)


investment = st.number_input(
    "Investment Amount (₹)",
    min_value=1000,
    value=100000
)


if st.button("Optimize Portfolio"):

    stocks = [
        x.strip()
        for x in stocks_input.split(",")
    ]


    st.subheader("Selected Stocks")

    st.write(stocks)


    prices = yf.download(
        stocks,
        period="1y",
        auto_adjust=True
    )["Close"]


    prices = prices.dropna()


    returns = prices.pct_change().dropna()


    annual_returns = returns.mean() * 252

    covariance = returns.cov() * 252


    n = len(stocks)


    weights = np.ones(n) / n


    portfolio_return = np.sum(
        annual_returns * weights
    )


    portfolio_risk = np.sqrt(
        np.dot(
            weights.T,
            np.dot(
                covariance,
                weights
            )
        )
    )


    sharpe = (
        portfolio_return /
        portfolio_risk
    )


    col1, col2, col3 = st.columns(3)


    with col1:
        st.metric(
            "Expected Return",
            f"{portfolio_return:.2%}"
        )


    with col2:
        st.metric(
            "Risk",
            f"{portfolio_risk:.2%}"
        )


    with col3:
        st.metric(
            "Sharpe Ratio",
            f"{sharpe:.2f}"
        )


    st.divider()


    allocation = pd.DataFrame(
        {
            "Stock": stocks,
            "Weight": weights
        }
    )


    st.subheader(
        "Portfolio Allocation"
    )


    st.dataframe(
        allocation
    )


    fig = px.pie(
        allocation,
        names="Stock",
        values="Weight",
        title="Optimal Allocation"
    )


    st.plotly_chart(
        fig,
        width="stretch"
    )


    st.subheader(
        "Investment Allocation"
    )


    allocation["Amount"] = (
        allocation["Weight"]
        *
        investment
    )


    st.dataframe(
        allocation
    )

