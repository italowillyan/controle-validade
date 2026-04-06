from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.orm import declarative_base
from database import engine

Base = declarative_base()

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String)
    nome_produto = Column(String, nullable=False)
    nome_grupo = Column(String)
    nome_local = Column(String)
    quantidade = Column(Integer)
    checkado = Column(Boolean, default=False)
    recebimento = Column(Date)
    validade = Column(Date, nullable=False)

Base.metadata.create_all(bind=engine)