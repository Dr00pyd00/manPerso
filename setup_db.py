

from app.core.database import Base, engine 
from app.core.all_models import *

def create_db():
    print('starting DB setup . . . ')
    Base.metadata.create_all(bind=engine)
    print('DB created !!!')


if __name__ == '__main__':
    create_db()






