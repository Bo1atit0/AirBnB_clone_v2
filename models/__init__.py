#!/usr/bin/python3

"""This module instantiates an object of class FileStorage"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.state import State

import os

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage

    storage = DBStorage()

else:
    storage = FileStorage()

storage.reload()
