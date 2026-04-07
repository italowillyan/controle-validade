# 📦 Controle de Validade

Sistema web para controle de produtos com data de validade, substituindo planilhas Excel por uma solução automatizada com banco de dados e interface web.

---

## 🎯 Objetivo

Permitir o gerenciamento de produtos com validade de forma simples e eficiente, incluindo:

* Cadastro de produtos
* Armazenamento em banco de dados
* Visualização em tabela
* Base para alertas de vencimento

---

## 🧱 Tecnologias utilizadas

* **Backend:** FastAPI
* **Banco de dados:** PostgreSQL
* **ORM:** SQLAlchemy
* **Servidor:** Uvicorn
* **Frontend:** HTML, CSS, JavaScript
* **Versionamento:** Git + GitHub

---

## 🗄️ Estrutura do banco

Tabela: `produtos`

```sql
CREATE TABLE produtos (
    id SERIAL PRIMARY KEY,
    codigo TEXT,
    nome_produto TEXT NOT NULL,
    nome_grupo TEXT,
    nome_local TEXT,
    quantidade INTEGER,
    checkado BOOLEAN DEFAULT FALSE,
    recebimento DATE,
    validade DATE NOT NULL,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🚀 Como rodar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/italowillyan/controle-validade.git
cd controle-validade
```

---

### 2. Criar ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Instalar dependências

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary
```

---

### 4. Configurar banco de dados

No PostgreSQL:

```sql
CREATE DATABASE validade_db;

\c validade_db

CREATE TABLE produtos (
    id SERIAL PRIMARY KEY,
    codigo TEXT,
    nome_produto TEXT NOT NULL,
    nome_grupo TEXT,
    nome_local TEXT,
    quantidade INTEGER,
    checkado BOOLEAN DEFAULT FALSE,
    recebimento DATE,
    validade DATE NOT NULL,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

### 5. Configurar conexão

No arquivo `database.py`:

```python
DATABASE_URL = "postgresql://postgres:SUA_SENHA@localhost:5432/validade_db"
```

---

### 6. Rodar o servidor

```bash
python -m uvicorn main:app --reload
```

---

### 7. Acessar o sistema

* API: http://127.0.0.1:8000
* Documentação: http://127.0.0.1:8000/docs
* Interface: abrir `frontend/index.html`

---



## ✅ Status atual

* ✔️ API funcionando
* ✔️ Banco conectado
* ✔️ Cadastro via interface
* ✔️ Listagem de produtos
* ✔️ Projeto versionado
* ✔️ Rodando em múltiplas máquinas

---

## 🔄 Fluxo do sistema

```
Frontend → API → Banco de dados → API → Frontend
```

---

## 🚀 Próximas melhorias

* Cálculo de dias para vencer
* Status automático (vencido, próximo, válido)
* Filtros e busca
* Ordenação por validade
* Melhorias visuais
* Sistema de login
* Deploy online

---

## 🧠 Aprendizados

* Criação de API REST
* Integração com banco de dados
* Uso de ambiente virtual
* Versionamento com Git
* Estruturação de sistema full stack

---

## 📌 Autor

**Italo Willyan**

---

## 📄 Licença

Projeto para fins de estudo e uso interno.
