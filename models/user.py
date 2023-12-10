#!/usr/bin/python3
""" holes User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """ represents User calsss the that inherit form BaseModel
    
    Attributes

    email: string - empty string
    password: string - empty string
    first_name: string - empty string
    last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
