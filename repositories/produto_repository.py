from sqlalchemy.orm import Session
from models.produto import Produto
from schemas.produto import ProdutoCreate

def get_all(db: Session):
    return db.query(Produto).all()

def get_by_id(db: Session, produto_id: int):
    return db.query(Produto).filter(Produto.id == produto_id).first()

def create(db: Session, produto_in: ProdutoCreate):
    db_produto = Produto(**produto_in.model_dump())
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto

def delete(db: Session, produto: Produto):
    db.delete(produto)
    db.commit()