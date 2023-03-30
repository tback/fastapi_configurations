from fastapi import FastAPI
from configurations.routes import router as root_router


def create_app():
    app = FastAPI()
    app.include_router(root_router)

    return app


app = create_app()
