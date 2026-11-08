import uvicorn


def run() -> None:
    uvicorn.run("cnc_asset_api.main:app", host="0.0.0.0", port=8000)
