import pytest
from app import create_app
from app.models import Imovel
from app import db
import json 

@pytest.fixture
def client():
    app = create_app(testing=True)
    with app.test_client() as client:
        yield client

def test_listar_imoveis_retorna_json(client):
    response = client.get("/imoveis")
    assert response.status_code == 200
    assert response.is_json

def test_listar_imoveis_contem_atributos(client):
    response = client.get("/imoveis")
    data = response.get_json()

    assert isinstance(data, list)  

    if data:  
        imovel = data[0]
        assert "id" in imovel
        assert "tipo" in imovel
        assert "cidade" in imovel
        assert "preco" in imovel

def test_remover_imovel(test_client, init_database, cleanup_database, imovel_id, expected_status):
    response = test_client.delete(f'/imoveis/{imovel_id}')
    assert response.status_code == expected_status
    if expected_status == 200:
        assert db.session.get(Imovel, imovel_id) is None


def test_listar_imoveis(test_client, init_database, query_param, expected_count):
    response = test_client.get(f'/imoveis{query_param}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == expected_count

def test_listar_por_cidade(test_client, init_database, route, query_param, expected_count):
    response = test_client.get(f'{route}{query_param}')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) == expected_count