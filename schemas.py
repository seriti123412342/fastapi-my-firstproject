from pydantic import BaseModel, Field, EmailStr, ConfigDict
class NewBook(BaseModel):
    title: str
    theme: int



class UserSchema(BaseModel):
    
    username: str = Field(max_length=50)
    email: EmailStr
    full_name: str | None = None
    is_active: bool
    age: int = Field(ge=0, le=125)



class UserHobbyandJob(UserSchema):
    hobby: str | None = None
    job: str = Field(le=50)