from app.db.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)    
    full_name = Column(String, nullable=False)                            
    phone = Column(Integer, nullable=False)                                
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    status = Column(Boolean, default=True)