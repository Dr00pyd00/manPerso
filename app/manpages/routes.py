
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.manpages.exceptions import ManPageTitleAlreadyExistException, ManPageNotFoundException
from app.manpages.services import create_manpage_service, get_all_manpage_service, get_manpage_by_id_service, get_manpage_by_title_service, send_hello_service, delete_manpage_by_id_service, update_manpage_by_id_service
from app.manpages.schemas import CreateManPageSchema, DisplayManPageSchema, UpdateManPageSchema
from app.manpages.models import ManPage


router = APIRouter(
        prefix='/manpage',
        tags=['ManPage'],
        )

@router.get('/test')
def manpage_test_hello():
    return send_hello_service()

@router.get('/', response_model=list[DisplayManPageSchema])
def get_all_manpage(db:Session = Depends(get_db)):
    return get_all_manpage_service(db=db)


@router.get('/id/{page_id}', response_model= DisplayManPageSchema) 
def get_manpage_by_id(page_id: int, db:Session = Depends(get_db)) -> ManPage:
    try:
        return get_manpage_by_id_service(page_id, db) 
    except ManPageNotFoundException:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail='manpage not found'
                )

@router.get('/{page_title}', response_model=DisplayManPageSchema) 
def get_manpage_by_title(page_title: str,  db:Session = Depends(get_db)) -> ManPage:
    try:
        return get_manpage_by_title_service(page_title, db)
    except ManPageNotFoundException:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail='manpage not found'
                )



@router.post('/')
def create_manpage(new_page_data: CreateManPageSchema, db:Session = Depends(get_db) ):
    try:
        return create_manpage_service(new_page_data, db)
    except ManPageTitleAlreadyExistException:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Title already taken')


@router.delete('/{page_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_manpage_by_id(page_id: int, db:Session = Depends(get_db) )-> None:
    try:
        print('starting try')
        return delete_manpage_by_id_service(page_id, db)
    except ManPageNotFoundException:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail='manpage not found'
                )


@router.patch('/{page_id}', status_code=status.HTTP_200_OK, response_model= DisplayManPageSchema)
def update_manpage_by_id(
        page_id: int,  
        updated_page: UpdateManPageSchema,
        db:Session = Depends(get_db)) -> ManPage:
    try:
        return update_manpage_by_id_service(page_id, updated_page, db)
    except ManPageNotFoundException:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail='manpage not found'
                )


    


