import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd


st.set_page_config(
    page_title="Valuation Dashboard",
    page_icon="📈",
    layout="wide"
)


st.title("📈 FinanceOS Valuation Dashboard")

st.write(
    "DCF Valuation + Graham Intrinsic Value Calculator"
)


ticker = st.text_input(
    "Enter Stock Symbol",
    "RELIANCE.NS"
)


if st.button("Calculate Valuation"):

    stock = yf.Ticker(ticker)

    info = stock.info


    try:
        price = info.get(
            "currentPrice",
            0
        )

        eps = info.get(
            "trailingEps",
            0
        )

        revenue = info.get(
            "totalRevenue",
            0
        )


        st.subheader("Market Data")


        col1, col2, col3 = st.columns(3)


        with col1:
            st.metric(
                "Current Price",
                f"₹{price:,.2f}"
            )


        with col2:
            st.metric(
                "EPS",
                f"₹{eps:.2f}"
            )


        with col3:
            st.metric(
                "Revenue",
                f"₹{revenue/10000000:,.2f} Cr"
            )


        st.divider()


        # Graham Valuation

        st.subheader(
            "Benjamin Graham Valuation"
        )


        growth = st.slider(
            "Expected Growth Rate (%)",
            1,
            20,
            10
        )


        graham_value = (
            eps *
            (8.5 + (2 * growth))
        )


        st.metric(
            "Graham Intrinsic Value",
            f"₹{graham_value:,.2f}"
        )


        st.divider()


        # DCF Model

        st.subheader(
            "DCF Valuation"
        )


        free_cash_flow = st.number_input(
            "Current Free Cash Flow (₹ Cr)",
            value=1000
        )


        growth_rate = st.slider(
            "FCF Growth (%)",
            1,
            20,
            10
        )


        discount_rate = st.slider(
            "Discount Rate (%)",
            5,
            20,
            10
        )


        terminal_growth = st.slider(
            "Terminal Growth (%)",
            1,
            8,
            3
        )


        years = 5


        future_fcf = []

        fcf = free_cash_flow


        for year in range(years):

            fcf = (
                fcf *
                (1 + growth_rate/100)
            )

            future_fcf.append(fcf)


        present_value = 0


        for i, value in enumerate(
            future_fcf
        ):

            present_value += (
                value /
                (
                    1 +
                    discount_rate/100
                ) ** (i+1)
            )


        terminal_value = (
            future_fcf[-1]
            *
            (1 + terminal_growth/100)
            /
            (
                discount_rate/100
                -
                terminal_growth/100
            )
        )


        dcf_value = (
            present_value
            +
            terminal_value /
            (
                1 +
                discount_rate/100
            ) ** years
        )


        st.metric(
            "DCF Enterprise Value",
            f"₹{dcf_value:,.2f} Cr"
        )


        st.divider()


        st.subheader(
            "Valuation Summary"
        )


        summary = pd.DataFrame(
            {
                "Method":
                [
                    "Current Price",
                    "Graham Value",
                    "DCF Value"
                ],

                "Value":
                [
                    price,
                    graham_value,
                    dcf_value
                ]
            }
        )


        st.dataframe(
            summary,
            width="stretch"
        )


    except Exception as e:

        st.error(
            f"Unable to calculate valuation: {e}"
        )
