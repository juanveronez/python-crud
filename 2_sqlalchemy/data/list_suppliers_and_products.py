from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from database import engine
from tables import Supplier, Product

Session = sessionmaker(bind=engine)

try:
    with Session() as session:
        suppliers = session.query(Supplier).all()
        print('Suppliers:', [supplier.name for supplier in suppliers])
except SQLAlchemyError as e:
    print('Error listing suppliers:', e)

try:
    with Session() as session:
        products = session.query(Product).all()
        print('Products:', [product.name for product in products])
except SQLAlchemyError as e:
    print('Error listing products:', e)


try:
    with Session() as session:
        result = session.query(
            Supplier.name,
            func.sum(Product.price).label('total_price'))\
        .join(Product, Supplier.id == Product.supplier_id)\
        .group_by(Supplier.name)

        for name, total_price in result:
            print(f'Supplier: {name}, Total Price: {total_price}')

except SQLAlchemyError as e:
    print('Error using custom query:'. e)