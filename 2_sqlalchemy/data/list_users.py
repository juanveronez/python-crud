from sqlalchemy.orm import sessionmaker
from database import engine
from tables import User

Session = sessionmaker(bind=engine)

def list_users_without_with():
    session = Session()

    users = session.query(User).all()
    print('Lista de usuários:', [user.name for user in users])

    session.close()

def list_users():
    with Session() as session:
        users = session.query(User).all()
        print('Lista de usuários:', [user.name for user in users])

list_users()