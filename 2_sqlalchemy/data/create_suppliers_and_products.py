from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from database import engine
from tables import Supplier, Product

Session = sessionmaker(bind=engine)

try:
    with Session() as session:
        suppliers = [
            Supplier(name='Fornecedor A', phone='12345678', email='contato@a.com', address='Random Address 1'),
            Supplier(name='Fornecedor B', phone='87654321', email='contato@b.com', address='Random Address 2'),
            Supplier(name='Fornecedor C', phone='11223344', email='contato@c.com', address='Random Address 3'),
            Supplier(name='Fornecedor D', phone='44332211', email='contato@d.com', address='Random Address 4'),
            Supplier(name='Fornecedor E', phone='55667788', email='contato@e.com', address='Random Address 5')
        ]

        session.add_all(suppliers)
        session.commit()
except SQLAlchemyError as e:
    print('Error adding new suppliers:', e)

try:
    with Session() as session:
        products = [
            Product(name='Product A', description='Product A made by supplier A', price=999.99, supplier_id=1),
            Product(name='Product B', description='Product B made by supplier B', price=199.99, supplier_id=2),
            Product(name='Product C', description='Product C made by supplier C', price=299.99, supplier_id=3),
            Product(name='Product D', description='Product D made by supplier D', price=399.99, supplier_id=4),
            Product(name='Product E', description='Product E made by supplier E', price=499.99, supplier_id=5)
    ]

    session.add_all(products)
    session.commit()
except SQLAlchemyError as e:
    print('Error adding new products:', e)