from fastapi import FastAPI, APIRouter, HTTPException;
from Config import collection
from Database.Schemas import all_users
from Database.Models import users

app = FastAPI();
router = APIRouter();

@router.get("/")
async def get_all_users():
    data = collection.find( );
    return all_users(data);

@router.post("/")
async def create_user(new_user : users):
    try:
        response = collection.insert_one(dict(new_user));
        return {"status_code":200, "id":str(response.inserted_id)};
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Some error occured in creating user{e}");

app.include_router(router)