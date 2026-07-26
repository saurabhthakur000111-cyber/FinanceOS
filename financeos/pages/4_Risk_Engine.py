import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.express as px


st.set_page_config(
    page_title="Risk Engine",
    page_icon="⚠️",
    layout="wide"
)


st.title("⚠️ FinanceOS Risk Engine")

st.write(
    "Portfolio risk measurement and Monte Carlo simulation"
)


stocks_input = st.text_input(
    "Enter portfolio stocks",
    "RELIANCE.NS,TCS.NS,INFY.NS,HDFCBANK.NS"
)


if st.button("Calculate Risk"):

    stocks = [
        x.strip()
        for x in stocks_input.split(",")
    ]


    prices = yf.download(
        stocks,
        period="1y",
        auto_adjust=True
    )["Close"]


    prices = prices.dropna()


    returns = prices.pct_change().dropna()


    portfolio_returns = (
        returns.mean(axis=1)
    )


    volatility = (
        portfolio_returns.std()
        *
        np.sqrt(252)
    )


    var_95 = np.percentile(
        portfolio_returns,
        5
    )


    expected_shortfall = (
        portfolio_returns[
            portfolio_returns <= var_95
        ].mean()
    )


    max_drawdown = (
        (
            prices / prices.cummax()
        ) - 1
    ).min().min()


    col1, col2, col3, col4 = st.columns(4)


    with col1:
        st.metric(
            "Annual Volatility",
            f"{volatility:.2%}"
        )


    with col2:
        st.metric(
            "VaR 95%",
            f"{var_95:.2%}"
        )


    with col3:
        st.metric(
            "Expected Shortfall",
            f"{expected_shortfall:.2%}"
        )


    with col4:
        st.metric(
            "Max Drawdown",
            f"{max_drawdown:.2%}"
        )


    st.divider()


    st.subheader(
        "Portfolio Return Distribution"
    )


    fig = px.histogram(
        portfolio_returns,
        nbins=50,
        title="Daily Returns"
    )


    st.plotly_chart(
        fig,
        width="stretch"
    )


    st.divider()


    st.subheader(
        "Monte Carlo Simulation"
    )


    simulations = []

    last_value = 100000


    for i in range(100):

        prices_sim = [
            last_value
        ]

        for day in range(252):

            change = np.random.normal(
                portfolio_returns.mean(),
                portfolio_returns.std()
            )

            prices_sim.append(
                prices_sim[-1]
                *
                (1 + change)
            )

        simulations.append(
            prices_sim
        )


    simulation_df = pd.DataFrame(
        np.array(simulations).T
    )


    st.line_chart(
        simulation_df
    )
