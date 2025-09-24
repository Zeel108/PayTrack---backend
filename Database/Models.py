from pydantic import BaseModel

class users(BaseModel):
    first_name: str
    last_name: str
    office_id: int
    email: str