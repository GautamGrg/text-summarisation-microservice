# project/app/main.py

import logging

from fastapi import FastAPI

from app.api import ping
from app.db import init_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("uvicorn")

def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)

    return application

app = create_application()
init_db(app=app)