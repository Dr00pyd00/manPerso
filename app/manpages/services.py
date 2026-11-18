
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.manpages.models import ManPage
from app.manpages.schemas import CreateManPageSchema, UpdateManPageSchema
from app.manpages.exceptions import ManPageNotFoundException, ManPageTitleAlreadyExistException
from app.tags.services import get_or_create_tags

# test
def send_hello_service():
    return {'message':'Hello World'}


# CRUD 

def get_all_manpage_service(db: Session) -> list[ManPage]:
    all_pages = db.query(ManPage).all()
    return all_pages


def get_manpage_by_id_service(page_id: int, db: Session) -> ManPage:
    page = db.get(ManPage, page_id)
    if page is None:
        raise ManPageNotFoundException 
    return page 

def get_manpage_by_title_service(page_title: str, db: Session) -> ManPage:
    query = select(ManPage).where(ManPage.title == page_title)
    res = db.execute(query).scalar_one_or_none() 
    if res is None:
        raise ManPageNotFoundException
    return res



def create_manpage_service(new_manpage_data: CreateManPageSchema, db: Session) -> ManPage:
    existing_title = db.query(ManPage).filter(ManPage.title == new_manpage_data.title).first()
    if existing_title:
        raise ManPageTitleAlreadyExistException

    new_page = ManPage(**new_manpage_data.model_dump(exclude={'tags'}))
    new_page.tags = get_or_create_tags(new_manpage_data.tags , db) 
    db.add(new_page)
    db.commit() 
    db.refresh(new_page) 
    return new_page


def delete_manpage_by_id_service(page_id: int, db: Session) -> None:
    page = db.get(ManPage, page_id)    
    if page is None:
        raise ManPageNotFoundException
    db.delete(page)
    db.commit 
    return


def update_manpage_by_id_service(page_id: int, updated_page: UpdateManPageSchema, db: Session) -> ManPage:
    page = db.get(ManPage, page_id) 
    if page is None:
        raise ManPageNotFoundException 
    if updated_page:
        data_dict = updated_page.model_dump(exclude_none=True)
        for k,v in data_dict.items():
            setattr(page, k, v) 
    db.commit()
    db.refresh(page)
    return page 


