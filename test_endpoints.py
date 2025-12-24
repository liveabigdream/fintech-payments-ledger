from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

# Root endpoint
@app.get("/")
def root():
    return {"status": "ok"}

# Sample in-memory payments data
payments_data = [
    {"id": 1, "amount": 100, "status": "paid"},
    {"id": 2, "amount": 250, "status": "pending"},
    {"id": 3, "amount": 75, "status": "failed"},
]

# GET all payments
@app.get("/payments")
def get_payments():
    return payments_data

# GET a single payment by ID
@app.get("/payments/{payment_id}")
def get_payment(payment_id: int):
    for payment in payments_data:
        if payment["id"] == payment_id:
            return payment
    return {"detail": "Payment not found"}

# -----------------------------
# Testing directly inside FastAPI
# -----------------------------
if __name__ == "__main__":
    client = TestClient(app)
    
    endpoints = [
        "/",           # Root endpoint
        "/payments",   # All payments
        "/payments/1", # Single payment
        "/payments/999", # Non-existent payment
    ]
    
    for endpoint in endpoints:
        response = client.get(endpoint)
        print(f"GET {endpoint} -> Status: {response.status_code}, Response: {response.json()}")
