import yfinance as yf
import pandas as pd
import numpy as np


def calculate_returns(symbols):

    data = yf.download(
        symbols,
        period="1y",
        auto_adjust=True
    )["Close"]

    returns = data.pct_change().dropna()

    return returns



def calculate_volatility(returns):

    volatility = (
        returns.std()
        *
        np.sqrt(252)
    )

    return volatility



def calculate_sharpe(returns):

    portfolio_return = returns.mean() * 252

    volatility = (
        returns.std()
        *
        np.sqrt(252)
    )

    if volatility == 0:
        return 0

    sharpe = (
        portfolio_return
        /
        volatility
    )

    return sharpe



def calculate_beta(stock, benchmark="^NSEI"):

    stock_data = yf.download(
        stock,
        period="1y",
        auto_adjust=True
    )["Close"]

    benchmark_data = yf.download(
        benchmark,
        period="1y",
        auto_adjust=True
    )["Close"]


    combined = pd.concat(
        [
            stock_data,
            benchmark_data
        ],
        axis=1
    ).dropna()


    combined.columns = [
        "Stock",
        "Market"
    ]


    covariance = np.cov(
        combined["Stock"],
        combined["Market"]
    )[0][1]


    market_variance = np.var(
        combined["Market"]
    )


    beta = covariance / market_variance

    return round(float(beta), 2)



def risk_score(volatility, sharpe):

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
        min(score, 100)
    )
