from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_ola_mundo():
    """
    Esse teste tem 3 etapas (AAA):
    A: arrange  - Arranjo
    A: act      - Executa a coista (o SUT)
    A: assert   - Garanta que A é A
    """

    """arrange:"""
    client = TestClient(app)

    """act:"""
    response = client.get('/')

    """assert:"""
    assert response.json() == {'message': 'Olá mundo!'}
    assert response.status_code == HTTPStatus.OK
