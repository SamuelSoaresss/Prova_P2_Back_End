import pytest

def test_isolamento_banco(client):
    response = client.get("/produtos/")
    assert response.status_code == 200
    assert response.json() == []

def test_listar_vazio(client):
    response = client.get("/produtos/")
    assert response.status_code == 200
    assert len(response.json()) == 0

def test_criar_produto(client):
    payload = {"nome": "Teclado", "preco": 350.50, "estoque": 15, "ativo": True}
    response = client.post("/produtos/", json=payload)
    assert response.status_code == 201
    assert response.json()["nome"] == payload["nome"]

def test_criar_e_listar(client):
    client.post("/produtos/", json={"nome": "Mouse", "preco": 150.0})
    response = client.get("/produtos/")
    assert len(response.json()) == 1

def test_buscar_produto_sucesso(client, produto_existente):
    response = client.get(f"/produtos/{produto_existente.id}")
    assert response.status_code == 200

def test_buscar_produto_404(client):
    response = client.get("/produtos/999")
    assert response.status_code == 404

def test_deletar_produto_204(client, produto_existente):
    response = client.delete(f"/produtos/{produto_existente.id}")
    assert response.status_code == 204

def test_deletar_e_confirmar_remocao(client, produto_existente):
    client.delete(f"/produtos/{produto_existente.id}")
    response = client.get(f"/produtos/{produto_existente.id}")
    assert response.status_code == 404

def test_deletar_404(client):
    response = client.delete("/produtos/999")
    assert response.status_code == 404

@pytest.mark.parametrize("payload", [
    {"nome": "", "preco": 100.0},
    {"nome": "Cadeira", "preco": 0.0},
    {"nome": "Mesa", "preco": -50.0},
    {"preco": 100.0},
])
def test_payloads_invalidos(client, payload):
    response = client.post("/produtos/", json=payload)
    assert response.status_code == 422