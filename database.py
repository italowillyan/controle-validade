from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:JVC123@localhost/validade_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)