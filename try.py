
from app.database import get_db, engine, Base , LocalSession
from app.models import ManPage, Tag

from pydantic import BaseModel

class Sch(BaseModel):
    name: str 
    age: int 

d = {'name':'koko','age':'32'}

print(f'd = {d}')

pd = Sch.model_validate(d)

print(f'pd avec model_validate = {pd}')

print(type(pd.age))

d2 = pd.model_dump() 
print(f'd2 = {d2}')

djson = pd.model_dump_json()

print(f'djson = {djson}')


#
# Base.metadata.create_all(bind=engine)
#
# t1 = Tag(name='Linux')
#
# p1 = ManPage(title='cd',summary='change directory tool',text='tool linux, thing for for change directory, usage: cd <truc>.')
# p1.tags.append(t1)
#
# print(t1.pages)
#
#
# with LocalSession() as db:
#     db.add(p1)
#     db.commit()
#
# print('programme fini')
#
#
#


