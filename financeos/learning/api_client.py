from financeos.api.stock_api import get_stock_price


symbol = input("Enter Stock Symbol: ").upper()


try:

    quote = get_stock_price(symbol)

    print()
    print("========== LIVE STOCK DATA ==========")
    print("Symbol       :", quote.get("01. symbol"))
    print("Open Price   :", quote.get("02. open"))
    print("High Price   :", quote.get("03. high"))
    print("Low Price    :", quote.get("04. low"))
    print("Current Price:", quote.get("05. price"))
    print("Volume       :", quote.get("06. volume"))
    print("=====================================")


except Exception as error:

    print()
    print("ERROR:", error)