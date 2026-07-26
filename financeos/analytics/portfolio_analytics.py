import yfinance as yf
import pandas as pd
import numpy as np


def calculate_returns(symbols):

    prices = yf.download(
        symbols,
        period="1y",
        auto_adjust=True
    )["Close"]

    returns = prices.pct_change().dropna()

    return returns



def calculate_volatility(returns):

    return (
        returns.std()
        *
        np.sqrt(252)
    )



def calculate_sharpe(returns):

    annual_return = returns.mean() * 252

    annual_volatility = (
        returns.std()
        *
        np.sqrt(252)
    )

    if annual_volatility == 0:
        return 0

    return (
        annual_return /
        annual_volatility
    )



def calculate_beta(
    stock,
    benchmark="^NSEI"
):

    stock_price = yf.download(
        stock,
        period="1y",
        auto_adjust=True
    )["Close"]


    market_price = yf.download(
        benchmark,
        period="1y",
        auto_adjust=True
    )["Close"]


    data = pd.concat(
        [
            stock_price,
            market_price
        ],
        axis=1
    ).dropna()


    data.columns = [
        "Stock",
        "Market"
    ]


    covariance = np.cov(
        data["Stock"],
        data["Market"]
    )[0][1]


    variance = np.var(
        data["Market"]
    )


    return round(
        float(covariance / variance),
        2
    )



def calculate_risk_score(
    volatility,
    sharpe
):

    score = 50


    if volatility < 0.15:
        score += 20

    elif volatility > 0.30:
        score -= 20


    if sharpe > 1:
        score += 20

    elif sharpe < 0:
        score -= 20


    return max(
        0,
        min(score,100)
    )
