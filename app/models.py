
from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, Table, Text, func, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship 

from app.database import Base

# MIXINS ----------------------------------------------------------------------


class TimeStampMixin():
    '''
    Mixin to add:
        -created_at (datetime)  

        -updated_at (datetime)
    '''

    created_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            nullable=False,
            server_default=func.now(),
            )


    updated_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            nullable=False,
            server_default=func.now(),
            onupdate=func.now(),
            )


# JOIN man_pages tags ---------------------------

page_tags = Table(
        'page_tags',
        Base.metadata,
        Column('man_page_id', Integer, ForeignKey('man_pages.id', ondelete='CASCADE'), primary_key=True),
        Column('tag_id', Integer, ForeignKey('tags.id', ondelete='CASCADE'), primary_key=True),
)




# PAGE -------------------------------------------------------------------------

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

        

# TAG -------------------------------------------------------------------------

class Tag(TimeStampMixin, Base):

    __tablename__ = 'tags'

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
            String,
            nullable=False,
            unique=True,
            )

    pages: Mapped[list[ManPage]] = relationship(secondary=page_tags, back_populates='tags')


