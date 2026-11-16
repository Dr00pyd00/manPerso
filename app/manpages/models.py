
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text

from app.core.mixins import TimeStampMixin
from app.core.database import Base 
from app.manpages.tag_association import  page_tags

if TYPE_CHECKING:
    from app.tags.models import Tag


class ManPage(TimeStampMixin, Base):

    __tablename__ = 'man_pages'

    id: Mapped[int] = mapped_column(primary_key=True) 

    title: Mapped[str] = mapped_column(
            String,
            nullable=False, 
            unique=True,
            )

    summary: Mapped[str|None] = mapped_column(
            String, 
            nullable=True,
            )

    text: Mapped[str] = mapped_column(
            Text,
            nullable=False,
            )

    tags: Mapped[list['Tag']] = relationship(secondary=page_tags, back_populates='pages') 

        


