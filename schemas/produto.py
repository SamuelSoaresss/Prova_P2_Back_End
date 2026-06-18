from pydantic import BaseModel, Field

class ProdutoCreate(BaseModel):
    nome: str = Field(..., min_length=1, description="Nome não pode ser vazio")
    preco: float = Field(..., gt=0, description="Preço deve ser maior que zero")
    estoque: int = Field(default=0)
    ativo: bool = Field(default=True)

class ProdutoResponse(ProdutoCreate):
    id: int

    class Config:
        from_attributes = True