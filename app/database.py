
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.settings import POSTGRES_URL


class Base(DeclarativeBase):
    pass 

engine = create_engine(POSTGRES_URL, echo=True) #type:ignore

LocalSession = sessionmaker(
        bind=engine,
        autoflush=False,
        autocommit=False,
        )


# dependance ----------------------------
def get_db():
    db = LocalSession() 
    try:
        yield db
    finally:
        db.close





