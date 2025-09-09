import pytest
from unittest.mock import patch, MagicMock
from server import app

@pytest.fixture()
def client(): 
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# -------------------------------------------------------------------------------------------------------
# Listar todos os imóveis 
@patch("server.conectando_db")
def test_listar_imoveis(mock_db, client):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchall.return_value = [{'id': 1, 'cidade': 'São Paulo'}, {'id': 2, 'cidade': 'Bofete'}]
    mock_db.return_value = mock_conn

    response = client.get(f'/imoveis')
    assert response.status_code == 200
    assert response.json == [{'id': 1, 'cidade': 'São Paulo'}, {'id': 2, 'cidade': 'Bofete'}]

# -------------------------------------------------------------------------------------------------------
# Mostra o imóvel encontrado, via id
@patch("server.conectando_db")
def test_buscar_imovel_encontrado(mock_db, client):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchone.return_value = {'id': 1, 'cidade': 'São Paulo'}
    mock_db.return_value = mock_conn

    response = client.get('/imoveis/1')
    assert response.status_code == 200
    assert response.json == {'id': 1, 'cidade': 'São Paulo'}

# -------------------------------------------------------------------------------------------------------
# Mostra se o imóvel não foi encontrado, via id
@patch("server.conectando_db")
def test_buscar_imovel_nao_encontrado(mock_db, client):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchone.return_value = None
    mock_db.return_value = mock_conn

    response = client.get('/imoveis/999')
    assert response.status_code == 404
    assert response.json == {'erro': 'Imóvel não encontrado'}

# -------------------------------------------------------------------------------------------------------
# Adicionar imóveis
@patch("server.conectando_db")
def test_adicionar_imovel(mock_db, client):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_db.return_value = mock_conn

    dados = {
        'logradouro': 'Rua X',
        'tipo_logradouro': 'Rua',
        'bairro': 'Ipiranga',
        'cidade': 'São Paulo',
        'cep': '04205-002',
        'tipo': 'casa',
        'valor': 200000,
        'data_aquisicao': '2025-05-10'
    }

    response = client.post('/imoveis', json=dados)
    assert response.status_code == 201
    assert response.json == {'mensagem': 'Imóvel criado com sucesso'}

# -------------------------------------------------------------------------------------------------------
# Atualizar imóveis (estrutura parecida, alterando as informações)
@patch("server.conectando_db")
def test_atualizar_imovel(mock_db, client):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchone.return_value = {'id': 1, 'cidade': 'São Paulo'}
    mock_db.return_value = mock_conn

    dados = {
        'logradouro': 'Rua Nova',
        'tipo_logradouro': 'Rua',
        'bairro': 'Bairro Novo',
        'cidade': 'São Paulo',
        'cep': '01000-000',
        'tipo': 'apartamento',
        'valor': 300000,
        'data_aquisicao': '2025-06-01'
    }

    response = client.put('/imoveis/1', json=dados)
    assert response.status_code == 200
    assert response.json == {'mensagem': 'Imóvel atualizado com sucesso'}

# -------------------------------------------------------------------------------------------------------
# Remover imóveis
@patch("server.conectando_db")
def test_remover_imovel(mock_db, client):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.rowcount = 1
    mock_conn.cursor.return_value = mock_cursor
    mock_db.return_value = mock_conn

    response = client.delete(f'/imoveis/1')
    assert response.status_code == 200:
    assert response.json == {'mensagem': 'Imóvel removido com sucesso'}

# -------------------------------------------------------------------------------------------------------
# Listar imóveis por tipo
@patch("server.conectando_db")
def test_listar_por_tipo(mock_db, client):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [{'id': 1, 'tipo': 'casa'}, {'id': 2, 'tipo': 'apartamento'}]
    mock_conn.cursor.return_value = mock_cursor
    mock_db.return_value = mock_conn

    response = client.get('/imoveis/tipo/casa')
    assert response.status_code == 200
    assert response.json == [{'id': 1, 'tipo': 'casa'}, {'id': 2, 'tipo': 'apartamento'}]

# -------------------------------------------------------------------------------------------------------
# Listar imóveis por cidade
@patch("server.conectando_db")
def test_listar_por_cidade(mock_db, client):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [{'id': 2, 'cidade': 'Bofete'}]
    mock_conn.cursor.return_value = mock_cursor
    mock_db.return_value = mock_conn

    response = client.get('/imoveis/cidade/Bofete')
    assert response.status_code == 200
    assert response.json == [{'id': 2, 'cidade': 'Bofete'}]