from dataclasses import dataclass
from typing import List

@dataclass
class Student:
    name :str
    interests :List(str)
    age :int
    has_read :bool
    how_many :int
