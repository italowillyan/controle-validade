from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date
from database import SessionLocal
from models import Produto

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de entrada (POST)

class ProdutoCreate(BaseModel):
    codigo: str
    nome_produto: str
    nome_grupo: str
    nome_local: str
    quantidade: int
    checkado: bool
    recebimento: date
    validade: date


# Função de status

def calcular_status(validade):
    hoje = date.today()
    dias = (validade - hoje).days

    if dias < 0:
        return "Vencido"
    elif dias <= 30:
        return "Proximo"
    else:
        return "Valido"


# Rota inicial

@app.get("/")
def home():
    return {"mensagem": "API rodando"}


# Listar produtos

@app.get("/produtos")
def listar_produtos():
    db = SessionLocal()
    produtos = db.query(Produto).all()

    resultado = []
    for p in produtos:
        resultado.append({
            "id": p.id,
            "codigo": p.codigo,
            "nome_produto": p.nome_produto,
            "nome_grupo": p.nome_grupo,
            "nome_local": p.nome_local,
            "quantidade": p.quantidade,
            "validade": p.validade,
            "status": calcular_status(p.validade)
        })

    return resultado


# Criar produto

@app.post("/produtos")
def criar_produto(produto: ProdutoCreate):
    db = SessionLocal()

    novo = Produto(
        codigo=produto.codigo,
        nome_produto=produto.nome_produto,
        nome_grupo=produto.nome_grupo,
        nome_local=produto.nome_local,
        quantidade=produto.quantidade,
        checkado=produto.checkado,
        recebimento=produto.recebimento,
        validade=produto.validade
    )

    db.add(novo)
    db.commit()

    return {"mensagem": "Produto criado com sucesso"}