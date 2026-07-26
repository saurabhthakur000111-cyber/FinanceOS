import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")


def get_stock_price(symbol):

    if not API_KEY:
        raise Exception("API key missing")

    url = (
        f"https://www.alphavantage.co/query?"
        f"function=GLOBAL_QUOTE"
        f"&symbol={symbol}"
        f"&apikey={API_KEY}"
    )

    try:
        response = requests.get(url, timeout=10)

        response.raise_for_status()

    except requests.exceptions.Timeout:
        raise Exception("Request timed out")

    except requests.exceptions.RequestException as e:
        raise Exception(f"API request failed: {e}")

    data = response.json()

    if "Global Quote" not in data:
        raise Exception("Invalid stock symbol or API limit reached")

    return data["Global Quote"]
