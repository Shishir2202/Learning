# Address Model

# city → string (minimum length 3)
# pincode → string (must be exactly 6 digits)
# User Model

# user_id → integer
# name → string
# email → email string
# age → integer (must be ≥ 18)
# address → nested Address model
# is_premium → optional boolean (default = False)

from pydantic import BaseModel,Field, ConfigDict, EmailStr
from typing import Optional

# Address Model

# city → string (minimum length 3)
# pincode → string (must be exactly 6 digits)


class Address(BaseModel):
    city:str = Field (...,min_length=3)
    pincode: str = Field (...,pattern= r"^\d{6}$")

    model_config = ConfigDict(validate_assignment=True)

# User Model

# user_id → integer
# name → string
# email → email string
# age → integer (must be ≥ 18)
# address → nested Address model
# is_premium → optional boolean (default = False)

class User(BaseModel):
    user_id: int
    name: str
    email: EmailStr
    age: int = Field(..., ge=18)
    address: Address
    is_premium: Optional[bool] = False
    model_config=ConfigDict(validate_assignment=True)

addr = Address(city='Mumbai',pincode ='411057')
user = User(
    user_id=1,
    name='Shishir',
    email='shishir@gmaail.com',
    age=32,
    address=addr
)

print(user)



