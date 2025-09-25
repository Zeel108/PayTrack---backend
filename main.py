from fastapi import FastAPI, APIRouter, HTTPException;
from Config import user_collection;
from Database.models.usermodel import users,userverify;
from Database.schemas.userschemas import all_users,single_user;
from fastapi.middleware.cors import CORSMiddleware;
from Database.models.auth_util import hash_password,verify_password;

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


@router.post("/auth/signup")
async def create_user(new_user : users):
    try:
        if user_collection.find_one({"email": new_user.email}):
            raise HTTPException(status_code=400, detail="Email already registered")
        hashed_pw = hash_password(new_user.password)
        create_user = new_user.dict()
        create_user["password"] = hashed_pw
        result = user_collection.insert_one(create_user)
        return {"message": "User created", "id": str(result.inserted_id)}

    except HTTPException as e:
        raise e
    except Exception as e:
        print("Error saving user:", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.post("/auth/login")
async def login(user_check: userverify):

    # Find user by email
    db_user = user_collection.find_one({"email": user_check.email})
    if not db_user:
        # Specific error for email not found
        raise HTTPException(status_code=404, detail="Email not registered")

    # Verify hashed password
    if not verify_password(user_check.password, db_user["password"]):
        # Specific error for wrong password
        raise HTTPException(status_code=401, detail="Incorrect password")

    # Login successful
    return {"message": "Login successful", "user": db_user["email"], "role": db_user.get("role", "USER")}


app.include_router(router)