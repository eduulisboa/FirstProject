from pydantic import BaseModel


class UserSchema(BaseModel):
    anything: str
