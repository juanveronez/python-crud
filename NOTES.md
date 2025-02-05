## SQL Model

O SQL Model é uma solução de **ORM** (Object Relational Mapping) moderna usada para lidarmos com SQL de forma simplificada em aplicações com Python. Com essa solução podemos interagir com tabelas SQL como se fossem classes Python, flexibilizando o uso do SQL e dando velocidade e simplicidade para criarmos aplicações.

O SQL Model usa o SQL Alchemy para conseguir se conectar com diferentes sistemas de forma simplificada, tendo bancos tradicionais como SQLite, MySQL e PostgreSQL. Além de bancos e estruturas de terceiros, como Google Sheets, Google Big Query e Snowflake.

Além disso tudo, ele ainda utiliza o Pydantic para validação dos objetos criados, dessa forma garantindo que uma instância de objeto siga regras pré-estabelecidas e garantindo a integridade do banco.

Por fim, ele utiliza como padrão um padrão de **transações atômicas, dessa forma utilizando sessões para que alterações só sejam feitas no banco com o comando de COMMIT**, dessa forma garantindo a segurança e integridade nos dados.

### Exemplo de uso do SQL Model

```py
from typing import Optional

from sqlmodel import create_engine, Field, Session, SQLModel

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None

engine = create_engine("sqlite:///database.db", echo=True)
SQLModel.metadata.create_all(engine) # necessary to create all sql model tables

hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

with Session(engine) as session:
    session.add(hero_1)
    session.add(hero_2)
    session.add(hero_3)
    session.commit()
```

No exemplo acima criamos uma classe que herda de `SQLModel` e que está definida como `table=True`, sendo assim uma tabela física no banco. Tendo id como um campo _Optional_ e sendo instanciado como um `Field`, para que dessa forma possa ser definido como uma **PK** (Primary Key).

Para conexão com o banco é criada uma engine, usada para lidar com diferentes bancos de forma análoga. Simplificando o uso do ORM como já mencionado antes. Usando `create_engine` para tal.

Além disso, para fazermos transações no banco, como um insert no banco, usamos o with para iniciar e fechar uma função, usando isso para adicionar os herois na tabela, **sendo necessário o commit dessa mudança**.
