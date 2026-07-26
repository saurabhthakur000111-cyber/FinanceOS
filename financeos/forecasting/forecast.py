from financeos.database.database import Database


class ForecastEngine:

    def __init__(self):
        self.db = Database()

    def get_average_price(self, symbol):

        query = """
        SELECT AVG(price)
        FROM stocks
        WHERE symbol = ?
        """

        cursor = self.db.connection.cursor()

        cursor.execute(query, (symbol,))

        result = cursor.fetchone()

        return result[0]

    def forecast_price(self, symbol):

        avg_price = self.get_average_price(symbol)

        if avg_price:
            future_price = avg_price * 1.05
            return round(future_price, 2)

        return None


if __name__ == "__main__":

    engine = ForecastEngine()

    prediction = engine.forecast_price("AAPL")

    print("========== FORECAST ==========")
    print("Symbol : AAPL")
    print("Predicted Price :", prediction)
