from pydantic import BaseModel, EmailStr, field_validator

class User(BaseModel):
    name: str
    email: EmailStr #check if it is valid email
    account_id: int

    #custom validation model
    @field_validator("account_id")
    def validate_account_id(cls, value):
        if value <= 0:
            raise ValueError(f"account_id must be positive: {value}")
        return value



#first way to create instances
user = User(
    name = 'jack',
    email = 'jack@gmail.com',
    account_id = 10
)

#second way to create instances
# user_data = {
#     'name' : 'Jack',
#     'email': 'jack@123.com',
#     'account_id': 12345
# }
# user = User(**user_data)

print(user.name)
print(user.email)
print(user.account_id)

#convert pydantic model to json
user_json_str = user.model_dump_json()
print(user_json_str)



