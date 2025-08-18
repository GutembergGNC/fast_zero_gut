import pytest
from fastapi.testclient import TestClient

from fastapi_zero.app import app

"""Bloco de Código de teste reutilizável (fixture):"""


@pytest.fixture
def client():
    return TestClient(app)
