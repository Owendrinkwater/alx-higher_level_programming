#!/usr/bin/python3
"""
Defines the State class with relationship to City
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import City, Base


class State(Base):
    """State class linked to the states table"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False) 
    cities = relationship(
        "City",
        back_populates="state",
        cascade="all, delete, delete-orphan"
    )                            
