from fastapi import FastAPI
import uvicorn

# import datetime

# Создание объекта приложения.
app = FastAPI()  # (docs_url=None, redoc_url=None) для отключения документации


# Новый эндпоинт: приветствие для автора.
@app.get('/me')
async def hello_author():
    return {'Hello': 'dear author'}


# Декоратор, определяющий, что GET-запросы к основному URL приложения
# должны обрабатываться этой функцией.
@app.get('/{name}')
async def greetings(
    name: str,
    surname: str,
    age: int | None = None,
) -> dict[str, str]:
    result = f'Hello: {name.capitalize()}'
    return {'greetings': result}


# А почему async? А потому что мы пишем асинхронное приложение!
# Все обработчики запросов будем объявлять через async def.
if __name__ == '__main__':
    # Команда на запуск uvicorn. При необходимости здесь же можно указать
    #  хост, порт и другие параметры сервера.
    uvicorn.run('main:app', reload=True)
