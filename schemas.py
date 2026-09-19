from enum import Enum
from typing import Optional, Union

from pydantic import BaseModel, Field


class EducationLevel(str, Enum):
    SECONDARY = 'Среднее образование'
    SPECIAL = 'Среднее специальное образование'
    HIGHER = 'Высшее образование'


class Person(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=20,
        title='Полное имя',
        description='Можно вводить в любом регистре',
    )
    surname: Union[str, list[str]]
    age: int | None = Field(
        None,
        gt=4,
        le=99,
    )
    is_staff: bool = Field(
        False,
        alias='is-staff',
    )
    education_level: Optional[EducationLevel] = None
