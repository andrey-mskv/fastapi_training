from fastapi import FastAPI
import uvicorn
from enum import StrEnum
from random import randint, choice
from secrets import token_hex
from uuid import uuid4

# import datetime

# Создание объекта приложения.
app = FastAPI()  # (docs_url=None, redoc_url=None) для отключения документации


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
    # description='Приветствие человека по имени и фамилии; '
    # 'опционально указывается возраст, образование и статус сотрудника',
    response_description='Полная строка приветствия',
)
async def greetings(
    name: str,
    surname: str,
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


class Tag(StrEnum):
    FRONT = 'Для фронтендера'
    BACK = 'Для бэкендера'
    ALL = 'Для всех'


@app.get(
    '/hexcolor',
    tags=[Tag.FRONT],
    summary='Случайный hex',
    description='Возвращает код цвета в формате HEX',
    response_description='Полная строка приветствия',
)
async def get_hex_color() -> str:
    return f'#{token_hex(3)}'


@app.get(
    '/uuid',
    tags=[Tag.BACK],
    summary='Рандомный uuid',
    description='Возвращает случайный уникальный идентификатор UUIDv4',
    response_description='Полная строка приветствия',
)
async def get_random_uuid() -> str:
    return str(uuid4())


HELLO_WORLD_LIST = [
    'Hello world',
    'Hola mundo',
    'Bonjour le monde',
    'Hallo Welt',
    'Ciao mondo',
    'Olá mundo',
    'Привет мир',
    'こんにちは世界',
    '你好世界',
    'مرحبا بالعالم',
]


@app.get(
    '/helloworld',
    tags=[Tag.BACK],
    summary='multilangeage',
    description='Возвращает фразу Hello world на случайно выбранном языке',
    response_description='Полная строка приветствия',
)
async def get_hello_world() -> str:
    return choice(HELLO_WORLD_LIST)


@app.get(
    '/dumplings',
    tags=[Tag.ALL],
    summary='Пельмени',
    description='Возвращает количество пельменей,'
    'которые следует сварить для поддержания сил (в диапазоне от 5 до 20)',
    response_description='Полная строка приветствия',
)
async def get_dumplings_count() -> int:
    return randint(5, 20)


@app.get(
    '/coin',
    tags=[Tag.ALL],
    summary='Красное&Белое',
    description='Помогает принять важное решение:'
    'подбрасывает виртуальную монетку и возвращает True или False',
    response_description='Полная строка приветствия',
)
async def toss_a_coin() -> bool:
    return choice([True, False])


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
