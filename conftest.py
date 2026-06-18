import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from main import app
from database import Base, get_db
from models.produto import Produto

TEST_DATABASE_URL = "postgresql://test_user:test_password@localhost:5433/test_db"
engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def client():
    Base.metadata.create_all(bind=engine)

    def override_get_db():
        try:
            db = TestingSessionLocal()
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as c:
        yield c

    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def produto_existente(client):
    db = TestingSessionLocal()
    produto = Produto(nome="Notebook", preco=3500.00, estoque=10, ativo=True)
    db.add(produto)
    db.commit()
    db.refresh(produto)
    db.close()
    return produto