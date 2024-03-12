#!/usr/bin/python3
"""Defining all State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Representing the state.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
