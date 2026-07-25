from financeos.database import Database


db = Database()

db.initialize()

db.save_stock(
    "AAPL",
    333.02,
    47489415
)