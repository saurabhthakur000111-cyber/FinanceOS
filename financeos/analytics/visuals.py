import plotly.express as px


def sector_allocation_chart(df):

    fig = px.pie(
        df,
        values="Current Value",
        names="Symbol",
        title="Portfolio Allocation"
    )

    return fig



def performance_chart(df):

    fig = px.bar(
        df,
        x="Symbol",
        y="P&L",
        title="Portfolio Profit & Loss"
    )

    return fig



def risk_gauge(score):

    fig = px.indicator(
        mode="gauge+number",
        value=score,
        title={
            "text": "Portfolio Risk Score"
        },
        gauge={
            "axis": {
                "range": [0,100]
            }
        }
    )

    return fig
