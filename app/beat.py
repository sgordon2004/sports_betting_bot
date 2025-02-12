from app import celery

def main():
    """Start Celery Beat"""
    celery.beat()

if __name__ == "__main__":
    main()