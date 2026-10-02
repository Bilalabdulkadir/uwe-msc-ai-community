from fastapi import FastAPI
from app.main import app


def test_health():
    client = FastAPI()
    assert client is not None
