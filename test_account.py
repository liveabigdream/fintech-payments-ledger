from app.db.session import SessionLocal
from app.db.models import Account

# Open a database session
db = SessionLocal()

# Create a new account
new_account = Account(name="Alice", balance=1000)
db.add(new_account)
db.commit()
db.refresh(new_account)

print(f"Created account: {new_account.id}, {new_account.name}, {new_account.balance}")

# Close session
db.close()
