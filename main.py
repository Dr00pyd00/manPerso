
from fastapi import FastAPI, Request
from sqlalchemy import text

from app.core.database import Base, engine 
from app.manpages.models import ManPage
from app.tags.models import Tag 
from app.manpages.routes import router as manpage_router

# test de reception de data 
app = FastAPI() 
app.include_router(manpage_router)

@app.post('/json')
def test_json(data: dict):
    print('Test json')
    print(f'recu: {data}')

from pydantic import BaseModel

class Sch(BaseModel):
    name: str 
    age: int 

@app.post('/schema')
def test_schema(data: Sch):
    print('test schema')
    print(f'sch: {data}')

@app.post('/brut')
async def test_brut(request: Request):
    data = await request.body()
    print('test brut')
    print(data)


#
# Base.metadata.create_all(bind=engine)
#
# try:
#     with engine.connect() as co:
#         res = co.execute(text("SELECT 1")) 
#         print(res.scalar())
#         print('connexion reussi')
#
# except Exception as e:
#     print(f'ERROR: {e}')
#
#
#
     


