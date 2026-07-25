from financeos.market.market_data import MarketData

market = MarketData()

stock = market.get_stock("AAPL")

print(stock)