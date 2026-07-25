import logging
import os

# Create the logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="logs/financeos.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Create logger
logger = logging.getLogger("FinanceOS")

# Test messages
logger.info("FinanceOS Started")
logger.warning("Financial statements are missing.")
logger.error("DCF calculation failed.")
logger.critical("Application shutting down.")