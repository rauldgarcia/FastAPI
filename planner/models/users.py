from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional, List
from models.events import Event
from beanie import Document, Link

class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[Event]] = None

    class Settings:
        name = "users"

    model_config = ConfigDict(
        json_schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong",
                "events": [],
            }
        }
    )

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
