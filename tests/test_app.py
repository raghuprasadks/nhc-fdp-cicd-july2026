import pytest

from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json() == {'status': 'ok'}


def test_data_endpoint(client):
    response = client.get('/api/data')
    assert response.status_code == 200
    assert response.get_json()['status'] == 'success'
