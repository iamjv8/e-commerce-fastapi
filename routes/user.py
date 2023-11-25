from fastapi import APIRouter, Depends
from models.users import Login, User
from config.database import db_database as db
from schemas.users import individual_serial, list_serial
from bson import ObjectId
from utils.auth_bearer import JWTBearer

from utils.auth_handler import get_password_hash, sign_jwt, verify_password

user_router = APIRouter()

@user_router.post("/login",tags=["Authentication"])
async def login_user(user: Login):
    db_user = individual_serial(db['users'].find_one(
            {'email': user.email}
    ))
    if db_user:
        if verify_password(user.password, db_user["password"]):
            token = sign_jwt(db_user['id'])
            return {"message": "Login Successfull", "access_token": token["access_token"]} 
        else:
            return {"message": "Password is wrong"} 
    else:
        return {"message": "User Not found"}


@user_router.post("/signup", tags=["Authentication"])
async def signup_user(user: User):
    if len(list_serial(db['users'].find(
            {'email': user.email}
    ))) > 0:
        return {"message": "User already Exists"} 
    else:
        user.password = get_password_hash(user.password)
        db['users'].insert_one(dict(user))
        return {"message": "User Created", "name" : user.name, "email" : user.email}
    

@user_router.get("/users", dependencies=[Depends(JWTBearer())], tags=["Users"])
async def get_all_users():
    return list_serial(db['users'].find())