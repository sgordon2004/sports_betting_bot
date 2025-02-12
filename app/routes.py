from app import app, celery
import logging

logging.basicConfig(
    level=app.config['LOG_LEVEL'],
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Define basic routes for testing
@app.route('/') # Root URL

def home():
    logger.info("Root route accessed")
    return "Sports Betting Bot Backend is running!"