from fastapi import FastAPI
import uvicorn
from enum import StrEnum

# import datetime

# Создание объекта приложения.
app = FastAPI()  # (docs_url=None, redoc_url=None) для отключения документации


class EducationLevel(StrEnum):
    SECONDARY = 'Среднее образование'
    SPECIAL = 'Среднее специальное образование'
    HIGHER = 'Высшее образование'


@app.get('/me')
async def hello_author():
    return {'Hello': 'dear author'}


@app.get('/{name}')
async def greetings(
    name: str,
    surname: str,
    age: int | None = None,
    is_staff: bool = False,
    # Добавляем новый параметр: образование.
    education_level: EducationLevel | None = None,
) -> dict[str, str]:
    result = ' '.join([name, surname])
    result = result.title()
    if age is not None:
        result += ', ' + str(age)

    # Добавляем проверку — передан ли параметр education_level:
    if education_level is not None:
        # Чтобы текст смотрелся грамотно,
        # переведём строку education_level в нижний регистр.
        result += ', ' + education_level.lower()

    if is_staff:
        result += ', сотрудник'
    return {'Hello': result}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
