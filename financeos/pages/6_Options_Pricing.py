import streamlit as st
import numpy as np
from scipy.stats import norm


st.set_page_config(
    page_title="Options Pricing",
    page_icon="🧮",
    layout="wide"
)


st.title("🧮 FinanceOS Options Pricing Engine")

st.write(
    "Black-Scholes Options Pricing Model"
)


col1, col2 = st.columns(2)


with col1:

    stock_price = st.number_input(
        "Current Stock Price",
        value=100.0
    )

    strike_price = st.number_input(
        "Strike Price",
        value=100.0
    )

    risk_free_rate = st.number_input(
        "Risk Free Rate (%)",
        value=7.0
    )


with col2:

    volatility = st.number_input(
        "Volatility (%)",
        value=20.0
    )

    time_to_expiry = st.number_input(
        "Time to Expiry (Years)",
        value=1.0
    )

    dividend = st.number_input(
        "Dividend Yield (%)",
        value=0.0
    )


def black_scholes(
    S,
    K,
    T,
    r,
    sigma,
    q
):

    d1 = (
        np.log(S/K)
        +
        (
            r - q + sigma**2/2
        )
        *
        T
    ) / (
        sigma*np.sqrt(T)
    )


    d2 = (
        d1 -
        sigma*np.sqrt(T)
    )


    call = (
        S*np.exp(-q*T)*norm.cdf(d1)
        -
        K*np.exp(-r*T)*norm.cdf(d2)
    )


    put = (
        K*np.exp(-r*T)*norm.cdf(-d2)
        -
        S*np.exp(-q*T)*norm.cdf(-d1)
    )


    return call, put



if st.button("Calculate Option Value"):

    call, put = black_scholes(
        stock_price,
        strike_price,
        time_to_expiry,
        risk_free_rate/100,
        volatility/100,
        dividend/100
    )


    st.divider()


    c1, c2 = st.columns(2)


    with c1:

        st.metric(
            "Call Option Value",
            f"₹{call:.2f}"
        )


    with c2:

        st.metric(
            "Put Option Value",
            f"₹{put:.2f}"
        )


    st.divider()


    st.subheader(
        "Option Greeks"
    )


    delta = norm.cdf(
        (
            np.log(stock_price/strike_price)
            +
            (
                risk_free_rate/100
                +
                volatility**2/200
            )
            *
            time_to_expiry
        )
        /
        (
            volatility/100
            *
            np.sqrt(time_to_expiry)
        )
    )


    st.write(
        f"Delta: {delta:.4f}"
    )
