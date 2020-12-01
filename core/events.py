from typing import Callable

from fastapi import FastAPI

def create_startup_app_handler(app: FastAPI) -> Callable:
    async def startup_app() -> None:
        pass

    return startup_app

def create_shutdown_app_handler(app: FastAPI) -> Callable:
    async def shutdown_app() -> None:
        pass

    return shutdown_app