from fastapi import FastAPI
from enum import StrEnum
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class EducationLevel(StrEnum):
    SECONDARY = 'Среднее образование'
    SPECIAL = 'Среднее специальное образование'
    HIGHER = 'Высшее образование'


class Person(BaseModel):
    name: str
    surname: str
    age: Optional[int] = None
    is_staff: bool = False
    education_level: Optional[EducationLevel] = None


@app.post(
    '/hello',
    tags=['common methods'],
    summary='Общее приветствие',
    response_description='Полная строка приветствия',
)
async def greetings(person: Person) -> dict[str, str]:
    """
    Приветствие пользователя:

    - **name**: имя
    - **surname**: фамилия
    - **age**: возраст (опционально)
    - **education_level**: уровень образования (опционально)
    """
    result = ' '.join([person.name, person.surname])
    result = result.title()
    if person.age is not None:
        result += ', ' + str(person.age)

    if person.education_level is not None:
        result += ', ' + person.education_level.lower()

    if person.is_staff:
        result += ', сотрудник'
    return {'Hello': result}
