from pydantic import BaseModel, EmailStr
from datetime import datetime

# User Model (Class)

# Schema of User
class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str
    created_at: datetime = datetime.now()

    model_config = {
        "from_attributes": True
    }

# schema of User Registration
class UserCreate(BaseModel):
    username: str
    full_name: str
    phone: int
    email: EmailStr
    password: str


# Schema of User Login
class UserLogin(BaseModel):
    email: EmailStr
    password: str   