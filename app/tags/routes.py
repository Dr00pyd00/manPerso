


from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.tags.exceptions import TagNameAlreadyExistException
from app.tags.models import Tag
from app.tags.schemas import CreateTagSchema, DisplayTagSchema
from app.tags.services import TagNotFoundException, create_tag_service, delete_tag_by_id_service, get_all_tags_serice, get_tag_by_id_service


router = APIRouter(
        prefix='/tag',
        tags=['Tag'],
        )


@router.get('/', response_model=list[DisplayTagSchema])
def get_all_tags(db: Annotated[Session, Depends(get_db)]) ->list[Tag]:
    return get_all_tags_serice(db)  


@router.get('/{tag_id}', response_model=DisplayTagSchema)
def get_tag_by_id(tag_id: int, db: Annotated[Session, Depends(get_db)]) ->Tag:
    try:
        return get_tag_by_id_service(tag_id, db)
    except TagNotFoundException:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Tag not found',
                )


@router.post('/', response_model=DisplayTagSchema)
def create_tag(tag_data: CreateTagSchema, db: Annotated[Session, Depends(get_db)]) -> Tag:
    try:
        return create_tag_service(tag_data, db)
    except TagNameAlreadyExistException:
        raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail='Tag name already taken',
                )


@router.delete('/{tag_id}', status_code=status.HTTP_204_NO_CONTENT) 
def delete_tag_by_id(tag_id: int, db: Annotated[Session, Depends(get_db)]) -> None:
    try:
        return delete_tag_by_id_service(tag_id, db)
    except TagNotFoundException:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Tag not found',
                )









