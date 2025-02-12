from sqlalchemy.orm import Session

from schemas import ProductCreate, ProductUpdate, Product
from models import ProductModel

def get_products(db: Session):
    return db.query(ProductModel).all()

def get_product(db: Session, product_id: int):
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()

def create_product(db: Session, product: ProductCreate):
    db_product = ProductModel(**product.model_dump())

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product

def update_product(db: Session, product_id: int, product: ProductUpdate):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if db_product is None:
        return None

    for k, v in product.model_dump().items():
        if v is not None:
            db_product[k] = v
    
    db.commit()
    db.refresh(db_product)
    
    return db_product

    

def delete_product(db: Session, product_id: int):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    db.delete(db_product)
    db.commit()

    return db_product