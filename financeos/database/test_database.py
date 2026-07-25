from financeos.database import Database

db = Database()

db.save_stock(
    "AAPL",
    333.02,
    47489415
)

print("Database initialized successfully.")
print("AAPL data saved successfully.")