web: gunicorn ProjectWhisper.wsgi
worker: celery worker -A tasks.app -l INFO
