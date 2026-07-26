import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go


st.set_page_config(
    page_title="FinanceOS",
    page_icon="📈",
    layout="wide"
)


st.title("📈 FinanceOS")
st.subheader(
    "AI Powered Financial Intelligence Platform"
)


st.divider()


# Market Overview

st.header("🌎 Market Overview")


symbols = {
    "NIFTY 50": "^NSEI",
    "SENSEX": "^BSESN",
    "RELIANCE": "RELIANCE.NS",
    "TCS": "TCS.NS"
}


cols = st.columns(4)


for col, (name, ticker) in zip(cols, symbols.items()):

    try:

        data = yf.download(
            ticker,
            period="5d",
            progress=False
        )


        price = data["Close"].iloc[-1]


        col.metric(
            name,
            f"₹{float(price):,.2f}"
        )


    except:

        col.metric(
            name,
            "N/A"
        )


st.divider()


# Portfolio Section

st.header("💼 Portfolio Intelligence")


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Portfolio Value",
        "₹10,00,000"
    )


with col2:

    st.metric(
        "Today's Return",
        "+1.25%"
    )


with col3:

    st.metric(
        "Risk Score",
        "Medium"
    )


st.divider()


# Performance Chart

st.header("📊 Market Performance")


try:

    data = yf.download(
        "RELIANCE.NS",
        period="1y",
        progress=False
    )


    fig = go.Figure()


    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data["Close"].values.flatten(),
            name="Reliance"
        )
    )


    fig.update_layout(
        height=400,
        xaxis_title="Date",
        yaxis_title="Price"
    )


    st.plotly_chart(
        fig,
        width="stretch"
    )


except:

    st.warning(
        "Market data unavailable"
    )


st.divider()


# System Modules

st.header("🚀 FinanceOS Modules")


modules = pd.DataFrame(
    {
        "Module": [
            "Financial Statements",
            "Ratio Analysis",
            "Portfolio Management",
            "Risk Engine",
            "Monte Carlo Simulation",
            "Markowitz Optimization",
            "DCF Valuation",
            "Graham Valuation",
            "Black-Scholes",
            "Stock Screener",
            "AI Assistant"
        ],
        "Status": [
            "Completed"
        ] * 11
    }
)


st.dataframe(
    modules,
    width="stretch"
)


st.success(
    "FinanceOS Platform Operational"
)
