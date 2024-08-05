from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from db2 import get_db
from schemas import userlogincheck, MenuItem,ownerright
from ormmodelsrestaurant import Restaurant, User
import uvicorn

app = FastAPI()

# CORS configuration
origins = [
    "http://127.0.0.1:5500",
    "http://localhost:8083",
    "null"  # This allows requests from files opened directly in the browser
]
# This error arises when the cURL request can't connect to the proxy server, either because the 
# server isn't responding or the proxy details are invalid. To solve the cURL (28) error, double-check
#  your proxy IP and port or use another proxy, as it can be down or unresponsive.

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Endpoint to fetch all menu items
@app.get("/menu/")
def get_menu_items(db: Session = Depends(get_db)):
    menu_items = db.query(Restaurant).all()
    return menu_items

# Endpoint to create a new user
@app.post("/user/", response_model=userlogincheck)
def create_user(user_data: userlogincheck, db: Session = Depends(get_db)):
    db_user = User(username=user_data.username, password=user_data.password, role=user_data.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Endpoint to fetch all users
@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

# Endpoint for user authentication
@app.post("/user/authenticate", response_model=userlogincheck)
def authenticate_user(user_data: userlogincheck, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == user_data.username).first()
    if user and user.password == user_data.password:
        return user_data
    raise HTTPException(status_code=404, detail="User not found or incorrect password")


@app.post("/menu/add", response_model=MenuItem)
def add_menu_item(menu: MenuItem, db: Session = Depends(get_db)):
        db_menu_item = Restaurant(
            food_item=menu.food_item,
            price=menu.price,
            category=menu.category,
            quantity=menu.quantity
        )
        db.add(db_menu_item)
        db.commit()
        db.refresh(db_menu_item)
        return menu


@app.post("/order/")
def order_food_item(
    food_item_id: int,
    order_quantity: int,
    db: Session = Depends(get_db)
):
     if order_quantity < 0:
        raise HTTPException(status_code=400, detail="Order quantity cannot be negative")
     menu_item = db.query(Restaurant).filter(Restaurant.id == food_item_id).first()
     if menu_item.quantity >= order_quantity:
        menu_item.quantity -= order_quantity
        db.commit()
        return {"message": "Order placed successfully"}
     else:
        raise HTTPException(status_code=400, detail="Insufficient quantity available")



# to reset password
@app.post("/reset")
def reset_password(username: str, new_password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user.password = new_password
    db.commit()    
    
    return {"message": "Password reset successfully"}

@app.post("/menu/reset_quantity/")
def reset_menu_item_quantity(
    food_item_id: int,
    db: Session = Depends(get_db)
):
    menu_item = db.query(Restaurant).filter(Restaurant.id == food_item_id).first()
    if not menu_item:
        raise HTTPException(status_code=404, detail="Menu item not found")
    if menu_item.quantity != 0:
        raise HTTPException(status_code=400, detail="Cannot reset stock unless it is at 0")
    
    menu_item.quantity = 20  # Reset to a predefined quantity
    db.commit()
    return {"message": "Quantity reset successfully"}

@app.delete("/menu/delete/")
def delete_menu_item(food_item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Restaurant).filter(Restaurant.id == food_item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Food item not found")
    
    db.delete(db_item)
    db.commit()
    return {"message": "Food item with id {food_item_id} has been deleted successfully"}





if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8083)
