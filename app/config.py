# Define configuration settings (environment variables, API keys, etc.)
import os
from dotenv import load_dotenv

load_dotenv() # Loads environment variables from .env file

class Config:
    # Flask settings
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here')

    # Celery settings (use Redis as broker/backend)
    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')
    CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')