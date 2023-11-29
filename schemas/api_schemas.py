from pydantic import BaseModel


class Item(BaseModel):
    item_id: int
    name:str
