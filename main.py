# main.py
from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routes import user, products


app = FastAPI()

app.include_router(user.user_router)
app.include_router(products.product_route)