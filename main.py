from fastapi import FastAPI, Path, Query
from enum import StrEnum

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
    # Устанавливаем ограничение для path-параметра:
    name: str = Path(min_length=2, max_length=20),
    # Устанавливаем ограничение для query-параметра:
    surname: str = Query(min_length=2, max_length=50),
    age: int | None = None,
    is_staff: bool = False,
    education_level: EducationLevel | None = None,
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
