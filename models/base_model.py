#!/usr/bin/python3
""" that defines all common attributes/methods for other classes """
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ represent a basemodel class"""
    def __init__(self, *args, **kargs):
        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if (len(kargs) == 0):
            models.storage.new(self)
            return
        for key, value in kargs.items():
            if (key == "__class__"):
                continue
            elif (key == "created_at" or key == "updated_at"):
                self.__dict__[key] = datetime.strptime(value, timeformat)
            else:
                self.__dict__[key] = value

    def __str__(self):
        clsName = self.__class__.__name__
        return "[{}] ({}) {}".format(clsName, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result
