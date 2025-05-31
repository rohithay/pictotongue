web: gunicorn --bind 0.0.0.0:$PORT app:app --workers 3 --timeout 120
worker: celery -A app.celery worker --loglevel=info
