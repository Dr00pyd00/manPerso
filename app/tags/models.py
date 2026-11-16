
from typing import TYPE_CHECKING 

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.mixins import TimeStampMixin 
from app.core.database import Base
from app.manpages.tag_association import page_tags

if TYPE_CHECKING:
    from app.manpages.models import ManPage


class Tag(TimeStampMixin, Base):

    __tablename__ = 'tags'

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
            String,
            nullable=False,
            unique=True,
            )

    pages: Mapped[list['ManPage']] = relationship(secondary=page_tags, back_populates='tags')


