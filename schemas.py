from pydantic import BaseModel    
class MenuItem(BaseModel):
    # id: int
    price: float
    food_item: str
    category:str
    quantity: int

class userlogincheck(BaseModel):
    username:str
    password:str
    role:str
    
class ownerright(BaseModel):
    username:str
    role:str