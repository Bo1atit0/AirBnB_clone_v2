#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    city = relationship("City", backref="state", cascade="all, delete-orphan")


    @property
    def cities(self):
        """
        Getter attribute cities that return
        the list of city instances
        """
        from models.city import City
        city_list = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
                return city_list
