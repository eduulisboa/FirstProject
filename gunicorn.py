from src.settings import APP_HOST, APP_PORT, APP_WORKERS, APP_WORKER_LOGLEVEL, DEBUG

wsgi_app = 'src.main:app'
bind = f'{APP_HOST}:{APP_PORT}'
workers = APP_WORKERS
worker_class = 'uvicorn.workers.UvicornWorker'
max_requests = 1000
timeout = 60
reload = DEBUG
loglevel = APP_WORKER_LOGLEVEL
