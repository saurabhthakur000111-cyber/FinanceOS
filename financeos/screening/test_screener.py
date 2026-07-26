from financeos.screening import StockScreener


def test_screener():
    screener = StockScreener()

    results = screener.screen(["AAPL"])

    assert isinstance(results, list)
