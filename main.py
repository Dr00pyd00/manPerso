
from sqlalchemy import text

from app.database import Base, engine 
from app.models import ManPage, Tag

Base.metadata.create_all()

try:
    with engine.connect() as co:
        res = co.execute(text("SELECT 1")) 
        print(res.scalar())
        print('connexion reussi')

except Exception as e:
    print(f'ERROR: {e}')



     


