from financeos.options import BlackScholes


def test_black_scholes():
    option = BlackScholes(
        stock_price=100,
        strike_price=100,
        time=1,
        rate=0.05,
        volatility=0.20,
    )

    assert option.call_price() > 0
    assert option.put_price() > 0
