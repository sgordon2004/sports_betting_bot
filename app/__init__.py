from flask import Flask
from celery import Celery # for task scheduling
import os

# Initialize Flask app
app = Flask(__name__)

# Load configuration
app.config.from_object('app.config.Config')

# Initialize Celery for backgorund tasks (i.e. daily bets)
celery = Celery (
    app.name,
    broker = app.config['CELERY_BROKER_URL'],
    backend = app.config['CELERY_RESULT_BACKEND']
)
celery.conf.update(app.config)