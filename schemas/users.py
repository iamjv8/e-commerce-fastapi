from models.users import User


def individual_serial(user: User) -> dict:
    if user:
        return {
            "id": str(user["_id"]),
            "name": user["name"],
            "email": user["email"],
            "password": user["password"]
        }
    else: 
        return {}

def list_serial(users) -> list:
    return[individual_serial(user) for user in users]