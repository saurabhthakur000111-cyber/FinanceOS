from financeos.market.market_data import MarketData


def test_market_object_creation():
    market = MarketData()
    assert market is not None


def test_get_stock():
    market = MarketData()

    stock = market.get_stock("AAPL")

    assert stock is not None
