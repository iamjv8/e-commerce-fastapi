import time
from typing import Dict
from dotenv import dotenv_values
from passlib.context import CryptContext
import jwt

config = dotenv_values(".env")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
JWT_SECRET = config["SECRET"]
JWT_ALGORITHM = config["ALGORITHM"]


def token_response(token: str):
    return {
        "access_token": token
    }

def sign_jwt(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
    return token_response(token)

def decode_token(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
    
# print(get_password_hash("ABCD"))
# print(verify_password("ABCDE", "$2b$12$cxNSbDeSAlAw./kQuorJHeQpVm7WSXrz47pf.jSN8BUtsgdrV6kci"))
def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
        return pwd_context.hash(password)