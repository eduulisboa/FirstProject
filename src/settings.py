from decouple import config, Csv

DEBUG = config('DEBUG', default=False, cast=bool)
APP_HOST = config('APP_HOST', default='0.0.0.0')
APP_PORT = config('APP_PORT', default=8000, cast=int)
APP_WORKERS = config('APP_WORKERS', default=1, cast=int)
APP_WORKER_LOGLEVEL = 'info' if not DEBUG else 'debug'

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1', cast=Csv())

DATABASE_NAME = config('DATABASE_NAME', default='pasd')
DATABASE_HOST = config('DATABASE_HOST', default='localhost')
DATABASE_PORT = config('DATABASE_PORT', default=5432, cast=int)
DATABASE_USER = config('DATABASE_USER', default='root')
DATABASE_PASSWORD = config('DATABASE_PASSWORD', default='toor')

DATABASE_URI = 'postgresql://{user}:{password}@{host}:{port}/{name}'.format(
    user=DATABASE_USER,
    password=DATABASE_PASSWORD,
    host=DATABASE_HOST,
    port=DATABASE_PORT,
    name=DATABASE_NAME,
)
