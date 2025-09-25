from Config import user_collection,get_next_id;
from pydantic import BaseModel;
from ..models.usermodel import users;


def single_user(user):
    return {
        "id": str(user["_id"]),
        "first_name": user["first_name"],
        "last_name": user["last_name"],
        "office_id": user["office_id"],
        "email": user["email"]
    };

def all_users(users):
    return [single_user(user) for user in users];