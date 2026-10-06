
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


# ---------------- AUTH ----------------

class RegisterRequest(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(min_length=6)


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    is_admin: bool

    class Config:
        from_attributes = True


# ---------------- PRODUCT ----------------

class ProductRequest(BaseModel):
    name: str = Field(min_length=2, max_length=150)
    description: Optional[str] = ""
    price: float = Field(gt=0)
    category: Optional[str] = ""
    image_url: Optional[str] = ""


class ProductResponse(ProductRequest):
    id: int
    is_active: bool

    class Config:
        from_attributes = True


# ---------------- CART ----------------

class CartRequest(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)


class CartItemResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    price: float
    subtotal: float


class CartResponse(BaseModel):
    items: list
    total: float


# ---------------- ORDER ----------------

class OrderItemResponse(BaseModel):
    id: int
    product_id: int
    product_name: str
    price: float
    quantity: int

    class Config:
        from_attributes = True


class OrderResponse(BaseModel):
    id: int
    user_id: int
    total_amount: float
    status: str
    created_at: datetime
    items: list[OrderItemResponse] = []

    class Config:
        from_attributes = True


class OrderListResponse(BaseModel):
    items: list[OrderResponse]
    page: int
    limit: int
    total: int
    total_pages: int


# ---------------- PAYMENT ----------------

class PaymentResponse(BaseModel):
    id: int
    order_id: int
    stripe_session_id: Optional[str] = None
    amount: float
    status: str

    class Config:
        from_attributes = True


# ---------------- PAGINATION ----------------

class ProductListResponse(BaseModel):
    items: list[ProductResponse]
    page: int
    limit: int
    total: int
    total_pages: int


# ---------------- CHECKOUT ----------------

class CheckoutResponse(BaseModel):
    checkout_url: str
    session_id: str


# ---------------- ADMIN ----------------

class AdminStatsResponse(BaseModel):
    total_products: int
    total_orders: int
    paid_orders: int
    total_revenue: float
