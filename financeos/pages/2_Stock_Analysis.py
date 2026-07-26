import streamlit as st
import yfinance as yf
import plotly.graph_objects as go


st.set_page_config(
    page_title="Stock Analysis",
    page_icon="📊",
    layout="wide"
)


st.title("📊 FinanceOS Stock Analysis")


ticker = st.text_input(
    "Enter Stock Symbol",
    "RELIANCE.NS"
)


if st.button("Analyze"):

    stock = yf.Ticker(ticker)

    info = stock.info


    st.subheader(
        f"{ticker} Overview"
    )


    col1, col2, col3, col4 = st.columns(4)


    with col1:
        st.metric(
            "Current Price",
            f"₹{info.get('currentPrice','N/A')}"
        )


    with col2:
        st.metric(
            "Market Cap",
            info.get(
                "marketCap",
                "N/A"
            )
        )


    with col3:
        st.metric(
            "P/E Ratio",
            info.get(
                "trailingPE",
                "N/A"
            )
        )


    with col4:
        st.metric(
            "ROE",
            info.get(
                "returnOnEquity",
                "N/A"
            )
        )


    st.divider()


    st.subheader(
        "Price History"
    )


    history = stock.history(
        period="1y"
    )


    fig = go.Figure()


    fig.add_trace(
        go.Scatter(
            x=history.index,
            y=history["Close"],
            name="Price"
        )
    )


    fig.update_layout(
        height=400
    )


    st.plotly_chart(
        fig,
        width="stretch"
    )


    st.divider()


    st.subheader(
        "Financial Statements"
    )


    tab1, tab2, tab3 = st.tabs(
        [
            "Income Statement",
            "Balance Sheet",
            "Cash Flow"
        ]
    )


    with tab1:
        st.dataframe(
            stock.financials
        )


    with tab2:
        st.dataframe(
            stock.balance_sheet
        )


    with tab3:
        st.dataframe(
            stock.cashflow
        )
