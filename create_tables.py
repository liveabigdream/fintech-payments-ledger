from app.db.base import Base
from app.db.models import Account  # Import your models
from app.db.session import engine

# Create all tables
Base.metadata.create_all(bind=engine)

print("Tables created successfully!")
