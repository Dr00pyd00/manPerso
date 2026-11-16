
from sqlalchemy import Table, Column, Integer, ForeignKey

from app.core.database import Base



page_tags = Table(
        'page_tags',
        Base.metadata,
        Column('man_page_id', Integer, ForeignKey('man_pages.id', ondelete='CASCADE'), primary_key=True),
        Column('tag_id', Integer, ForeignKey('tags.id', ondelete='CASCADE'), primary_key=True),
)



