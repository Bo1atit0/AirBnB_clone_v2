#!/usr/bin/python3

"""
Represents MySQL DB table
"""

import os
from models.base_model import Base


class DBStorage:
    """
    DB storage
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        constructor
        """
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        db = os.getenv(HBNB_MYSQL_DB)

        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{passwd}@{host}:3306/{db}',
            pool_pre_ping=True
        )

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query objects
        """
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        objects = {}
        if cls is None:
            classes = {'User': User, 'Place': Place,
                       'Amenity': Amenity, 'City': City,
                       'Review': Review
                       }

            for classname, klass in classes.items():
                obj_list = self.__session.query(klass).all()
                for obj in obj_list:
                    key = f"{classname}.{obj.id}"
                    objects[key] = obj
        else:
            obj_list = self.__session.query(cls).all()
            for obj in obj_list:
                key = f"{__class__.__name__}.{obj.id}"
                objects[key] = obj

        return objects

    def new(self, obj):
        """
        add obj to DB
        """
        self.__session.add(obj)

    def save(self):
        """commit changes of current DB"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from DB"""

        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create tables in DB"""
        from sqlalchemy.orm import sessionmaker, scoped_session
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.session = scoped_session(Session)
