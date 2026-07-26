from financeos.database.database import Database


def test_database_initialization():
    db = Database()
    assert db is not None
    db.close()


def test_save_stock():
    db = Database()

    db.save_stock("AAPL", 333.02, 47489415)

    assert db is not None

    db.close()
