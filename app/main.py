from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base

app = FastAPI(title="Fintech Payments Ledger")

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)


@app.get("/")
def health_check():
    return {"status": "ok"}
