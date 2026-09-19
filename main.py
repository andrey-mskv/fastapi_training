from fastapi import FastAPI, Path, Query
from enum import StrEnum
from typing import Annotated, Optional

app = FastAPI()


class EducationLevel(StrEnum):
    SECONDARY = 'Среднее образование'
    SPECIAL = 'Среднее специальное образование'
    HIGHER = 'Высшее образование'


@app.get('/me', tags=['special methods'], summary='Приветствие автора')
async def hello_author():
    return {'Hello': 'dear author'}


@app.get(
    '/{name}',
    tags=['common methods'],
    summary='Общее приветствие',
    response_description='Полная строка приветствия',
)
async def greetings(
    name: Annotated[
        str,
        Path(
            min_length=2,
            max_length=20,
            title='Полное имя',
            description='Можно вводить в любом регистре',
        ),
    ],
    surname: Annotated[str, Query(min_length=2, max_length=50)],
    age: Annotated[Optional[int], Query(gt=4, lt=100)] = None,
    is_staff: Annotated[bool, Query(alias='is-staff')] = False,
    education_level: Annotated[
        Optional[EducationLevel], Query(alias='education-level')
    ] = None,
) -> dict[str, str]:
    """
    Приветствие пользователя:

    - **name**: имя
    - **surname**: фамилия
    - **age**: возраст (опционально)
    - **is_staff**: является ли пользователь сотрудником
    - **education_level**: уровень образования (опционально)
    """
    result = ' '.join([name, surname])
    result = result.title()
    if age is not None:
        result += ', ' + str(age)

    if education_level is not None:
        result += ', ' + education_level.lower()

    if is_staff:
        result += ', сотрудник'
    return {'Hello': result}
