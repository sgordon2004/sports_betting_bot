# Define configuration settings (environment variables, API keys, etc.)
import os
from dotenv import load_dotenv

load_dotenv() # Loads environment variables from .env file

class Config:
    # Flask settings
    SECRET_KEY = os.getenv('SECRET_KEY')

    # Celery settings (use Redis as broker/backend)
    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')
    CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')

    # NBA API/Twitter credentials (will add later)
    NBA_API_KEY = os.getenv('NBA_API_KEY', '')
    NBA_API_TIMEOUT = 30 # seconds
    NBA_CACHE_EXPIRY = 3600 # 1 hour cache for team data
    TWITTER_BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN', '')

    # Logging settings (for better monitoring)
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'backend.log')