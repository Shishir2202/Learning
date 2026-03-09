from pydantic import BaseModel,Field,EmailStr,field_validator

class UserRegister(BaseModel):
    username: str = Field(min_length=5)
    email: EmailStr
    age: int = Field(ge=18)

user_input = {'username' : 'Shishir', 'email': 'shishir_shrivastava@gmail.com','age':19}

user=UserRegister(**user_input)

print(user)