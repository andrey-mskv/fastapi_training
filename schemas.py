from enum import Enum
from pydantic import BaseModel
from typing import Optional


class EducationLevel(str, Enum):
    SECONDARY = 'Среднее образование'
    SPECIAL = 'Среднее специальное образование'
    HIGHER = 'Высшее образование'


class Person(BaseModel):
    name: str
    surname: str | list[str]
    age: Optional[int] = None
    is_staff: bool = False
    education_level: Optional[EducationLevel] = None
