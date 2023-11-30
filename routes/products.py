from bson import ObjectId
from fastapi import APIRouter
from config.database import db_database as db
from models.product import Category, Product
from schemas.products import list_serial, individual_serial, list_serial_category

product_route = APIRouter()

@product_route.get("/products",tags=["Products"])
async def get_all_products():
    return list_serial(db['products'].find())

@product_route.get("/product/{id}",tags=["Products"])
async def get_single_product(id: str):
    return individual_serial(db['products'].find_one({
        "_id": ObjectId(id)
    }))

@product_route.get("/product/category/{category}", tags=["Products"])
async def get_products_by_category(category: str):
    return list_serial(db['products'].find({
        "category": category
    }))

@product_route.post("/product",tags=["Products"])
async def add_product(product: Product):
    db['products'].insert_one(dict(product))
    return {"message": "Product inserted successfully"}

@product_route.put("/product/{id}",tags=["Products"])
async def update_product(id: str, product: Product):
    db['products'].find_one_and_update({"_id": ObjectId(id)}, {"$set":dict(product)})
    return {"message": "Product updated successfully"}

@product_route.delete("/product/{id}",tags=["Products"])
async def delete_single_product(id: str):
    db['products'].find_one_and_delete({
        "_id": ObjectId(id)
    })
    return {"message": "Product deleted successfully"}

@product_route.get("/category",tags=["Products"])
async def get_all_categories():
    return list_serial_category(db['category'].find())

@product_route.post("/category",tags=["Products"])
async def add_category(category: Category):
    db['category'].insert_one(dict(category))
    return {"message": "Category added successfully"}