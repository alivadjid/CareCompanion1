import datetime as _dt
import pydantic as _pydantic


class _UserBase(_pydantic.BaseModel):
    email:str
    first_name:str
    last_name:str

class UserCreate(_UserBase):
    hashed_password:str

    class Config:
        from_attributes  = True

class User(_UserBase):
    id: int

    class Config:
        from_attributes = True