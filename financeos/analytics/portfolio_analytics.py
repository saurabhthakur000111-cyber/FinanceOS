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

    stock_data = yf.download(
        stock,
        period="1y",
        auto_adjust=True
    )["Close"]


    market_data = yf.download(
        benchmark,
        period="1y",
        auto_adjust=True
    )["Close"]


    if hasattr(stock_data, "columns"):
        stock_data = stock_data.iloc[:,0]

    if hasattr(market_data, "columns"):
        market_data = market_data.iloc[:,0]


    returns = pd.concat(
        [
            stock_data.pct_change(),
            market_data.pct_change()
        ],
        axis=1
    ).dropna()


    returns.columns = [
        "Stock_Return",
        "Market_Return"
    ]


    covariance = np.cov(
        returns["Stock_Return"],
        returns["Market_Return"]
    )[0][1]


    market_variance = np.var(
        returns["Market_Return"]
    )


    beta = covariance / market_variance


    return round(
        float(beta),
        2
    )
