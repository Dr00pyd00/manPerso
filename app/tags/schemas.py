
from pydantic import BaseModel, ConfigDict


class CreateTagSchema(BaseModel):
    name: str 

class DisplayTagSchema(BaseModel):
    # normalement un Schema prend soin un dict soit **dict 
    # avec model config il peut prendre un objet sqlalchemy ( genre Tag ) 
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str

