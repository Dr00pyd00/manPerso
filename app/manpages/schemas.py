
from pydantic import BaseModel, ConfigDict

from app.tags.schemas import DisplayTagSchema

# MANPAGES --------------------------------------------------------------------------
class CreateManPageSchema(BaseModel):
    title: str
    summary: str | None = None 
    text: str 
    tags: list = []


class DisplayManPageSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str 
    summary: str | None = None 
    text: str 
    tags: list[DisplayTagSchema]

class UpdateManPageSchema(BaseModel):
    title: str | None = None 
    summary: str | None = None 
    text: str | None = None 
    tags: list | None = None 



