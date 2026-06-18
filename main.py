from fastapi import FastAPI
from database import engine, Base
from routers import produto_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="E-commerce API")

app.include_router(produto_router.router)