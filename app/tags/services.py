
from sqlalchemy.orm import Session

from app.tags.exceptions import TagNameAlreadyExistException, TagNotFoundException
from app.tags.models import Tag
from app.tags.schemas import CreateTagSchema


def get_all_tags_serice(db: Session) ->list[Tag]:
    tags = db.query(Tag).all()
    return tags 


def get_tag_by_id_service(tag_id: int, db: Session) -> Tag:
    tag = db.get(Tag, tag_id)
    if tag is None:
        raise  TagNotFoundException
    return tag


def create_tag_service(tag_data: CreateTagSchema, db: Session) -> Tag:
    existing_tag_name = db.query(Tag).filter(Tag.name == tag_data.name).first()
    if existing_tag_name:
        raise TagNameAlreadyExistException
    tag = Tag(**tag_data.model_dump())
    db.add(tag)
    db.commit()
    return tag


def delete_tag_by_id_service(tag_id: int, db: Session) -> None:
    tag = db.get(Tag, tag_id)
    if tag is None:
        raise TagNotFoundException
    db.delete(tag)
    db.commit()


