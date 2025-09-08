#!/usr/bin/python3
"""Defines State class and Base instance for SQLAlchemy ORM"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base is the foundation for all mapped classes
Base = declarative_base()


class State(Base):
    """State class mapped to 'states' table"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
