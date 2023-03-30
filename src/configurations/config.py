from pydantic import BaseSettings


class Settings(BaseSettings):
    a: str = "default"
