from fastapi import FastAPI, APIRouter, HTTPException;
from Config import user_collection;
from Database.models.usermodel import users;
from Database.schemas.userschemas import all_users;
from fastapi.middleware.cors import CORSMiddleware;

app = FastAPI();
router = APIRouter();

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
router = APIRouter(prefix="/api")


@router.post("/saveuser")
async def create_user(new_user : users):
    new_user=user_collection.insert_one(dict(new_user));
    return {"message": "user created"};

app.include_router(router)