import pytest
from app import create_app

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
