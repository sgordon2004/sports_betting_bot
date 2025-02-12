from app import celery

# Celery worker startup


def main():
    """Start Celery worker"""
    celery.start()

if __name__ == "__main__":
    main()