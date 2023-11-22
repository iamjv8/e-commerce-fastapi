import json

from bson import json_util, ObjectId
from fastapi import APIRouter, Request
from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    mobile: int


user_router = APIRouter()


@user_router.get('/user')
def get_all_users(request: Request):
    return json.loads(json_util.dumps(list(request.app.database['users'].find())))

@user_router.post('/user')
def add_new_user(request: Request, user: User):
    user_exist = False
    data = dict(user)

    if len(list(request.app.database.users.find(
            {'email': data['email']}
    ))) > 0:
        print("Customer Exists")
        return {"message": "User Exists"}
    elif not user_exist:
        request.app.database.users.insert_one(data)
        return {"message": "User Created", "email": data['email'], "name": data['name']}

