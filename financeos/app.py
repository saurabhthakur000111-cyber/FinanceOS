import streamlit as st


st.set_page_config(
    page_title="FinanceOS",
    page_icon="📈",
    layout="wide"
)


st.title("📈 FinanceOS")

st.subheader(
    "AI Powered Financial Analytics Platform"
)


st.divider()


col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "Models",
        "11"
    )

with col2:
    st.metric(
        "Modules",
        "10"
    )

with col3:
    st.metric(
        "Status",
        "Production Ready"
    )

with col4:
    st.metric(
        "Version",
        "1.0"
    )


st.divider()


st.header("Available Finance Engines")


modules = {
    "📄 Financial Statements": "accounting",
    "📊 Ratio Analysis": "fundamentals",
    "💼 Portfolio Management": "portfolio",
    "⚠️ Risk Engine": "risk",
    "🎲 Monte Carlo Simulation": "forecasting",
    "📈 Markowitz Optimization": "optimization",
    "💰 DCF Valuation": "valuation",
    "🧮 Graham Valuation": "valuation",
    "📉 Black-Scholes": "options",
    "🔎 Stock Screener": "screening",
    "🤖 AI Finance Assistant": "ai"
}


for name, module in modules.items():
    st.success(
        f"{name}  |  {module}"
    )


st.divider()

st.info(
    "Use the sidebar to access FinanceOS analytics modules."
)