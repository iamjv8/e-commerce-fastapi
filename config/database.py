from dotenv import dotenv_values
from pymongo import MongoClient


config = dotenv_values(".env")
db_client = MongoClient(config["DATABASE_URI"])
db_database = db_client.eCommerce
db_collection = db_database['users']