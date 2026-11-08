from fastapi import FastAPI

from cnc_asset_api.api import health


def create_app() -> FastAPI:
    app = FastAPI(title="CNC Asset API", version="0.1.0")
    app.include_router(health.router)
    return app


app = create_app()
