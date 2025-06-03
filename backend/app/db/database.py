from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Import DB URL
SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")

# Create an engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)


# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()