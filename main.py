from fastapi import FastAPI
from database import engine, Base
from routers import produto_router


app = FastAPI(title="E-commerce API")

app.include_router(produto_router.router)