"""This is the module for database models
"""
from sqlalchemy import Column, Integer, String, Date
from db.database import Base 

class petadoption(Base):
    """This represents db tables
    """
    __tablename__ = "petadoption"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    species = Column(String)
    breed = Column(String)
    age = Column(String)
    health_status = Column(String)
    location = Column(String)
    status = Column(String)
    added_date = Column(Date)
