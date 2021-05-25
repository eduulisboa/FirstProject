import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.settings import APP_HOST, APP_PORT, APP_WORKER_LOGLEVEL, ALLOWED_HOSTS, DEBUG
from src.controllers import user_router
from src.repositories.postgres.sqlalchemy import create_database

create_database()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(user_router, tags=['User'])


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=APP_HOST,
        port=APP_PORT,
        reload=DEBUG,
        log_level=APP_WORKER_LOGLEVEL
    )
