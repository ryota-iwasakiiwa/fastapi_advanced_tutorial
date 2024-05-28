from functools import lru_cache
from typing import Annotated

from fastapi import FastAPI, Depends
from fastapi.testclient import TestClient

from .config import Settings

app = FastAPI()

@lru_cache
def get_settings():
    return Settings()

@app.get("/info")
async def info(settings: Annotated[Settings, Depends(get_settings)]):
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user,
    }

client = TestClient(app)

def get_settings_override():
    return Settings(admin_email="testing_admin@example.com")

app.dependency_overrides[get_settings] = get_settings_override

def test_app():
    response = client.get("/info")
    data = response.json()

    assert data == {
        "app_name": "Awesome API",
        "admin_email": "testing_admin@example.com",
        "items_per_user": 50
    }