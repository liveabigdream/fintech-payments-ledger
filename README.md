# fintech-payments-ledger
FastAPI-based payment ledger backend system
# Fintech Payments Ledger API

A lightweight **payment ledger backend service** built with **FastAPI** and **PostgreSQL**.  
This project demonstrates how payment transactions can be recorded, queried, and tracked in a fintech system.

> This is a **ledger system**, not a payment gateway.  
> It is designed to integrate with external providers (Paystack, Stripe, Flutterwave) via APIs or webhooks.

---

##  Features

- RESTful API built with FastAPI
- PostgreSQL database with SQLAlchemy ORM
- Payment transaction recording
- Fetch all payments
- Fetch single payment by ID
- Clear separation of concerns (API, models, schemas)
- Easily extendable for authentication and webhooks

---

##  Project Structure

