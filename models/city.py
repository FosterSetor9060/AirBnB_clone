#!/usr/bin/python3
"""Defining all City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Representing the city.

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
