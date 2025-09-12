from http import HTTPStatus

from fastapi_zero.schemas import UserPublic


def test_create_user(client):
    """arrange:"""
    """client oriundo do pytest"""

    """act:"""
    response = client.post(
        '/users/',
        json={
            'username': 'alice5',
            'email': 'alice5@example.com',
            'password': 'secrets',
        },
    )

    """assert:"""
    assert response.status_code == HTTPStatus.CREATED

    """Validar UserPublic:"""
    assert response.json() == {
        'username': 'alice5',
        'email': 'alice5@example.com',
        'id': 1,
    }


def test_read_users(client):
    """arrange:"""
    """client oriundo do pytest"""

    """act:"""
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_read_users_with_user(client, user):
    """arrange:"""
    """client oriundo do pytest"""

    """act:"""
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user):
    """arrange:"""
    """client oriundo do pytest"""

    """act:"""
    response = client.put(
        '/users/1',
        json={
            'password': '123',
            'username': 'testusername2',
            'email': 'test@test.com',
            'id': 1,
        },
    )
    assert response.json() == {
        'username': 'testusername2',
        'email': 'test@test.com',
        'id': 1,
    }


def test_delete_user(client, user):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


"""def test_root_deve_retornar_ola_mundo(client):

    Esse teste tem 3 etapas (AAA):
    A: arrange  - Arranjo
    A: act      - Executa a coisa (o SUT)
    A: assert   - Garanta que A é A

    arrange:
    client oriundo do pytest, em conftest.py

    act:
    response = client.get('/')

    assert:
    assert response.json() == {'message': 'Olá mundo!'}
    assert response.status_code == HTTPStatus.OK


    def test_exercicio_ola_mundo_em_html(client):
    arrange:
    client oriundo do pytest

    act:
    response = client.get('/exercicio-html')

    assert:
    assert response.status_code == HTTPStatus.OK
    assert '<h1> Olá Mundo </h1>' in response.text



    def test_aula3_update_user_com_404(client):
    arrange:
    client oriundo do pytest

    act:
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found!'}


    def test_aula3_delete_user_com_404(client):
    arrange:
    client oriundo do pytest

    act:
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found!'}


    def test_read_user_exercicio_aula03_200(client):
    arrange:
    client oriundo do pytest

    act
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


    def test_read_user_exercicio_aula03_404(client):
    arrange:
    client oriundo do pytest

    act:
    response = client.get('/users/999')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found!'}"""
