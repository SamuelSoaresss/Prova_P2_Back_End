from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from schemas.produto import ProdutoCreate, ProdutoResponse
from repositories import produto_repository

router = APIRouter(prefix="/produtos", tags=["Produtos"])

@router.post("/", response_model=ProdutoResponse, status_code=status.HTTP_201_CREATED)
def criar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    return produto_repository.create(db, produto)

@router.get("/", response_model=list[ProdutoResponse])
def listar_produtos(db: Session = Depends(get_db)):
    return produto_repository.get_all(db)

@router.get("/{id}", response_model=ProdutoResponse)
def buscar_produto(id: int, db: Session = Depends(get_db)):
    produto = produto_repository.get_by_id(db, id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_produto(id: int, db: Session = Depends(get_db)):
    produto = produto_repository.get_by_id(db, id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    produto_repository.delete(db, produto)
    return None