from fastapi import APIRouter
from models.users import User
from config.database import db_collection
from schemas.users import list_serial
from bson import ObjectId

user_router = APIRouter()

@user_router.get("/user")
async def get_users():
    print(db_collection.find())
    users = list_serial(db_collection.find())
    return users


@user_router.post("/user")
async def post_users(user: User):
    if len(list_serial(db_collection.find(
            {'email': user.email}
    ))) > 0:
        return {"message": "User already Exists"} 
    else:
        db_collection.insert_one(dict(user))
    return {"message": "User Created", "name" : user.name, "email" : user.email}
    
