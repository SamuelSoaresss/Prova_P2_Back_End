# API de Produtos - E-commerce

API REST construída com FastAPI e estruturada em camadas profissionais (Routers, Repositories, Schemas, Models), com testes automatizados utilizando Pytest e PostgreSQL no Docker.

## Como rodar a infraestrutura
Para subir os bancos de dados (desenvolvimento e testes isolados),  execute:
```bash
docker-compose up -d
```
## Como executar os testes
Para rodar a suíte de testes e gerar o relatório de cobertura, utilize o módulo do Python:
```bash
python -m pytest
```
## Isolamento dos Testes
O isolamento total do banco de dados é garantido por uma fixture baseada em yield localizada no arquivo conftest.py. O ciclo de vida de cada teste funciona da seguinte maneira:

Antes do teste iniciar, o comando Base.metadata.create_all gera todas as tabelas vazias exclusivamente no banco de testes (porta 5433).

O FastAPI é configurado via app.dependency_overrides para injetar esse banco de testes no lugar do banco principal.

Após a execução da validação (yield), o comando Base.metadata.drop_all destrói as tabelas. Isso garante que nenhum dado "vaze" ou interfira no próximo teste.

## Cobertura de Código (Coverage)
A suíte de testes foi executada com sucesso, validando regras de negócio e retornos de erro (404, 422), atingindo 100% de cobertura do código em 13 testes aprovados.