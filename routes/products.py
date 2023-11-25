from bson import ObjectId
from fastapi import APIRouter
from config.database import db_database as db
from models.product import Product
from schemas.products import list_serial, individual_serial

product_route = APIRouter()

@product_route.get("/products",tags=["Products"])
async def get_all_products():
    return list_serial(db['products'].find())

@product_route.post("/product",tags=["Products"])
async def add_product(product: Product):
    db['products'].insert_one(dict(product))
    return {"message": "Product inserted successfully"}

@product_route.get("/product/{id}",tags=["Products"])
async def get_single_product(id: str):
    return individual_serial(db['products'].find_one({
        "_id": ObjectId(id)
    }))

