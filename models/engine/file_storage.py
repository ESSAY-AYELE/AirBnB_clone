#!/usr/bin/python3
"" "whateve"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return objects that has been stored"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        objectName = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objectName, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        ob = FileStorage.__objects
        word = {obj: ob[obj].to_dict() for obj in ob.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(word, file)

    def reload(self):
        """ deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)"""
        try:
            with open(FileStorage.__file_path) as f:
                object_dic = json.load(f)
                for obj in object_dic.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
        except json.JSONDecodeError:
            return
