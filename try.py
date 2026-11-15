
from app.database import get_db, engine, Base , LocalSession
from app.models import ManPage, Tag

Base.metadata.create_all(bind=engine)

t1 = Tag(name='Linux')

p1 = ManPage(title='cd',summary='change directory tool',text='tool linux, thing for for change directory, usage: cd <truc>.')
p1.tags.append(t1)

print(t1.pages)


with LocalSession() as db:
    db.add(p1)
    db.commit()

print('programme fini')
    



