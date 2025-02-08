from typing import Optional

from sqlmodel import create_engine, Field, Session, SQLModel, text

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None

engine = create_engine("sqlite:///sqlmodel_exemple/database.db", echo=True)
SQLModel.metadata.create_all(engine) # necessary to create all sql model tables

def create_heroes():
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

    with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)
        session.commit()

def select_heroes_with_text():
    with Session(engine) as session:
        statement = text('SELECT * FROM hero') # used to avoid sql injection
        result = session.exec(statement=statement)
        
        heroes = result.fetchall()
        print("Herois: ", heroes)

if __name__ == '__main__':
    create_heroes()
    select_heroes_with_text()