from pydantic import BaseModel, PositiveFloat, PositiveInt

class ItemBase(BaseModel):
    name: str
    price: PositiveFloat
    is_offer: bool | None = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: PositiveInt
