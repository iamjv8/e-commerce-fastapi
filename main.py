# main.py
from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
import api

app = FastAPI()


# @app.on_event("startup")
# async def startup_event():
#     app.mongodb_client = MongoClient(config["DATABASE_URI"])
#     app.database = app.mongodb_client[config["DATABASE_NAME"]]
#     # print(app.mongodb_client.list_database_names())


# @app.on_event("shutdown")
# async def shutdown_event():
#     app.mongodb_client.close()


app.include_router(api.api_router)