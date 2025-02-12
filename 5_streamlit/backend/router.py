from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from schemas import Product, ProductCreate, ProductUpdate
import controller

router = APIRouter(prefix='/products')

@router.get('/', response_model=list[Product])
def get_products(db: Session = Depends(get_db)):
    """
    Get all products from database
    """
    return controller.get_products(db)

@router.get('/{id}', response_model=Product)
def get_product(id: int, db: Session = Depends(get_db)):
    product = controller.get_product(db, product_id=id)

    if product is None:
        raise HTTPException(404, 'Product not found')
    
    return product

@router.post('/', response_model=Product, status_code=201)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return controller.create_product(db, product)


@router.put('/{id}', response_model=Product)
def update_product(id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    product = controller.update_product(db, product_id=id, product=product)

    if product is None:
        raise HTTPException(404, 'Product not found')
    
    return product
    

@router.delete('/{id}', response_model=Product)
def delete_product(id: int, db: Session = Depends(get_db)):
    product = controller.delete_product(db, product_id=id)

    if product is None:
        raise HTTPException(404, 'Product not found')
    
    return product