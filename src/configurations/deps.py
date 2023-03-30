from typing import Annotated

from fastapi import Depends
from configurations.config import Settings
from functools import lru_cache


@lru_cache
def get_settings():
    return Settings()


def get_expensive(settings: Annotated[Settings, Depends(get_settings)]):
    print("EXPENSIVE OPERATION")
    return settings.a.upper()
