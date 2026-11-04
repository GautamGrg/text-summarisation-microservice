# project/app/main.py

from fastapi import FastAPI

from app.api import ping, summaries
from app.db import init_db


def create_application() -> FastAPI:
    """
    Intialises the FastAPI instance and plugs in
    routes + database
    """
    application = FastAPI()
    # Health check endpoint with GET /ping - to prove app is up.
    application.include_router(ping.router)
    application.include_router(
        router=summaries.router,
        prefix="/summaries",
        tags=["summaries"],
    )
    return application


app = create_application()
init_db(app=app)
