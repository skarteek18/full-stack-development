# full-stack-development

Digital Product Store

A full-stack Digital Product Store built using FastAPI, React Vite, SQLAlchemy, SQLite, JWT Authentication, and Stripe.

The application allows users to register, login, browse digital products, manage their cart, place orders, and make payments.

Technologies Used

Backend

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- JWT Authentication
- Pytest

Frontend

- React
- Vite
- Tailwind CSS
- React Router
- Axios
- React Toastify

Payment

- Stripe Checkout
- Stripe Webhooks

---

Project Structure

digital-product-store/
│
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── auth.py
│   ├── test_main.py
│   ├── requirements.txt
│   ├── .env.example
│   ├── .gitignore
│   └── digital_store.db
│
└── frontend/
    ├── src/
    ├── public/
    ├── package.json
    └── vite.config.js

Backend Features

- User Registration
- User Login
- JWT Authentication
- User Profile
- Product CRUD
- Product Search
- Product Pagination
- Cart Management
- Order Management
- Stripe Payment
- Stripe Webhook
- Admin Authorization
- Sales Statistics
- SQL Reports
- API Validation
- Error Handling
- Pytest Testing

---

Backend Setup

1. Clone Repository

git clone <your-github-repository-url>
cd digital-product-store

2. Create Virtual Environment

Windows

python -m venv venv
venv\Scripts\activate

Linux / Mac

python3 -m venv venv
source venv/bin/activate

3. Install Requirements

pip install -r requirements.txt

4. Environment Variables

Create a ".env" file:

DATABASE_URL=sqlite:///./digital_store.db

SECRET_KEY=your-secret-key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60

STRIPE_SECRET_KEY=sk_test_your_key

STRIPE_WEBHOOK_SECRET=whsec_your_secret

FRONTEND_URL=http://localhost:5173

Do not upload ".env" to GitHub.

---

Run Backend

uvicorn main:app --reload

Backend will run at:

http://127.0.0.1:8000

Swagger Documentation

Open:

http://127.0.0.1:8000/docs

Swagger provides interactive API documentation and allows you to test the APIs.

ReDoc

http://127.0.0.1:8000/redoc

---

API Endpoints

Authentication

POST /register
POST /login
GET  /profile

Products

POST   /products
GET    /products
GET    /products/{product_id}
PUT    /products/{product_id}
DELETE /products/{product_id}

Product Pagination

GET /products?page=1&limit=10

Product Search

GET /products?page=1&limit=10&search=python

Example response:

{
  "items": [],
  "page": 1,
  "limit": 10,
  "total": 25,
  "total_pages": 3
}

---

Cart APIs

GET    /cart
POST   /cart
PUT    /cart/{item_id}
DELETE /cart/{item_id}
DELETE /cart

Users can:

- Add products
- Update quantity
- Remove products
- Clear cart
- View cart
- Calculate total

---

Order APIs

POST /orders
GET  /orders
GET  /orders/{order_id}

Order statuses:

PENDING
PAID
FAILED
CANCELLED

---

Stripe Payment

Stripe is configured using test mode.

Payment flow:

React Cart
     ↓
FastAPI
     ↓
Create Stripe Checkout Session
     ↓
Stripe Payment
     ↓
Stripe Webhook
     ↓
Update Payment
     ↓
Update Order Status

The frontend success page is not trusted for payment confirmation.

The Stripe webhook is responsible for updating the order/payment status.

---

Admin Features

Admin users can:

- Create products
- Update products
- Delete products
- View orders
- View sales statistics

Admin statistics:

Total Products
Total Orders
Paid Orders
Total Revenue

Admin API:

GET /admin/stats
GET /admin/orders

---

SQL Reports

The project includes SQL-based reports for:

Total Revenue

GET /reports/total-revenue

Orders Per User

GET /reports/orders-per-user

Products Never Purchased

GET /reports/never-purchased

---

Database

SQLite is used for simple development.

Database:

digital_store.db

Tables:

users
products
carts
cart_items
orders
order_items
payments

Relationships:

User
 ├── Cart
 │    └── CartItem
 │         └── Product
 │
 └── Order
      ├── OrderItem
      │    └── Product
      │
      └── Payment

---

Frontend Setup

Go to the frontend folder:

cd frontend

Install dependencies:

npm install

Run React:

npm run dev

Frontend:

http://localhost:5173

Frontend Pages

/login
/register
/products
/products/:id
/cart
/orders
/admin/products
/admin/orders

Frontend uses:

- Axios for API calls
- React Router for navigation
- React Toastify for notifications
- Tailwind CSS for styling

---

Toast Notifications

The application uses toast notifications instead of browser alerts.

Examples:

✓ Login successful
✓ Product added to cart
✓ Product removed
✓ Payment successful

✗ Invalid credentials
✗ Payment failed
✗ Something went wrong

---

Testing

Run all tests:

pytest

Run with detailed output:

pytest -v

Tests cover:

- Registration
- Login
- Invalid login
- Product listing
- Pagination
- Unauthorized access
- Cart operations
- Invalid product
- Order access

---

Error Handling

The API handles:

- Duplicate email
- Invalid credentials
- Invalid product
- Invalid quantity
- Empty cart
- Unauthorized access
- Invalid order access
- Stripe errors
- Invalid webhook requests
- Invalid pagination

HTTP status codes include:

200 OK
201 Created
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
422 Validation Error

---

GitHub Upload

Before pushing the project:

git init

git add .

git commit -m "Initial Digital Product Store project"

git branch -M main

git remote add origin <your-github-repository-url>

git push -u origin main

Files Not to Upload

Do not upload:

.env
venv/
__pycache__/
*.pyc

These are already included in ".gitignore".

---

Future Improvements

- PostgreSQL deployment
- Product image upload
- Advanced admin dashboard
- Order email notifications
- Docker deployment
- Production Stripe configuration
- Cloud deployment

---

Author

Python Developer

Digital Product Store — Full Stack Development Task
