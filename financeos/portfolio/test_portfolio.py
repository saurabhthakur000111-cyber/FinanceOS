from financeos.portfolio.portfolio import Portfolio


def test_portfolio_creation():
    portfolio = Portfolio()
    assert portfolio is not None
