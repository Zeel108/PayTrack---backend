from pydantic import BaseModel, EmailStr

class users(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    phoneNumber: int
    departmentId: int
    positionId: int
    officeId: int
    salary: int
    age: int
    password: str
    role: str

class userverify(BaseModel):
    email: EmailStr
    password: str

class userOut(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    phoneNumber: int
    departmentId: int
    positionId: int
    officeId: int
    salary: int
    age: int
    role: str
