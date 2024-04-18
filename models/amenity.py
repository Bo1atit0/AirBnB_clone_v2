#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """Amenity class"""

    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    place_amenities = relationship("Place", secondary=place_amenity)
