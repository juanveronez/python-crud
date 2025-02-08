from sqlalchemy.orm import sessionmaker
from database import engine
from tables import User

def create_user_without_with():
    Session = sessionmaker(bind=engine)
    session = Session()
    
    try:
        new_user = User(name='João', age=32)
        session.add(new_user)
        session.commit()
    except:
        session.rollback()
        raise
    finally: session.close()

    print('Usuário inserido com sucesso!')

def create_user():
    Session = sessionmaker(bind=engine)

    with Session() as session:
        new_user = User(name='Clara', age=25)
        session.add(new_user)
        session.commit()

    print('Usuário inserido com sucesso!')

create_user()