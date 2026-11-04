# project/app/config.py

from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    BaseSettings fetches values from our environment variables,
    and assigns it to our fields (case-insensitive).
    """

    environment: str = "dev"
    testing: bool = False
    database_url: str = ""


@lru_cache()
def get_settings() -> BaseSettings:
    """
    It is wrapped in the @lru_cache decorator so objects are read
    once and stored, so it can be reused on every call.
    """
    return Settings()
