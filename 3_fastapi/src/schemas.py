from pydantic import BaseModel

class PokemonSchema(BaseModel):
    name: str
    types: str

    class Config:
        from_attributes = True # Define que será usado em um ORM