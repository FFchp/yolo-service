from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://postgres:Frt65502366!@localhost/Coop'
                        #"postgresql://postgres:Frt65502366!@localhost/Coop"

#engine = create_engine(SQLALCHEMY_DATABASE_URL)
engine = create_engine('postgresql+psycopg2://postgres:Frt65502366!@localhost/Coop')

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()