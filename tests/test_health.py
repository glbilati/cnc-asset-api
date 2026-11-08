import pytest
from httpx import ASGITransport, AsyncClient

from cnc_asset_api.main import create_app


@pytest.mark.anyio
async def test_live_returns_ok() -> None:
    transport = ASGITransport(app=create_app())
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/health/live")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}