
from math import ceil

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import User, Product, Cart, CartItem, Order, OrderItem, Payment
from auth import (
    hash_password,
    verify_password,
    create_access_token,
    get_current_user
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Digital Product Store API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# ---------------- SCHEMAS ----------------

class RegisterRequest(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(min_length=6)


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class ProductRequest(BaseModel):
    name: str = Field(min_length=2)
    description: str = ""
    price: float = Field(gt=0)
    category: str = ""
    image_url: str = ""


class CartRequest(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)


# ---------------- ADMIN ----------------

def admin_required(user: User):
    if not user.is_admin:
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )


# ---------------- HOME ----------------

@app.get("/")
def home():
    return {"message": "Digital Product Store API is running"}


# ---------------- AUTHENTICATION ----------------

@app.post("/register", status_code=201)
def register(
    data: RegisterRequest,
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(
        User.email == data.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    user = User(
        name=data.name,
        email=data.email,
        password=hash_password(data.password)
    )

    db.add(user
