from financeos.database import Database

db = Database()

print("Database initialized successfully.")

db.save_stock(
    "AAPL",
    333.02,
    47489415
)

print("AAPL data saved successfully.")

db.close()