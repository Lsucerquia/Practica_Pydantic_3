from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import ProductDatabase

app = FastAPI()
db = ProductDatabase()

class Product(BaseModel):
    name: str
    price: float
    quantity: int

@app.get("/")  # Endpoint raíz
def read_root():
    return {"message": "Welcome to the Product API!"}

@app.post("/products/")
def create_product(product: Product):
    return db.create_product(product.name, product.price, product.quantity)

@app.get("/products/{product_id}")
def read_product(product_id: int):
    product = db.read_product(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    updated_product = db.update_product(product_id, product.name, product.price, product.quantity)
    if updated_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    deleted_product = db.delete_product(product_id)
    if deleted_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"detail": "Product deleted"}

@app.get("/products/")
def list_products():
    return db.list_products()