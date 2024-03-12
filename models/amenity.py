#!/usr/bin/python3
"""Defining all Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Representing the amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
