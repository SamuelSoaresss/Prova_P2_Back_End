# API de Produtos - E-commerce

API REST com FastAPI e testes automatizados (Pytest + PostgreSQL no Docker).

## Subir o banco de testes
```bash
docker-compose up -d
```
Executar os testes
```bash
pytest
```
Isolamento

O isolamento é garantido por uma fixture baseada em yield no conftest.py. Antes de cada teste, Base.metadata.create_all gera as tabelas e o dependency_overrides injeta o banco de testes. Após o teste, drop_all limpa a estrutura.