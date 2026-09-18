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
    is_staff: bool = False,
) -> dict[str, str]:
    # Объединяем имя и фамилию в единую строку:
    result = ' '.join([name, surname])
    # Выводим все слова с заглавной буквы:
    result = result.title()
    if age is not None:
        # Добавляем к выводу возраст (если есть);
        # приводим число age к строке.
        result += ', ' + str(age)
    # Если is_staff равен True...
    if is_staff:
        # ...дописываем слово "сотрудник".
        result += ', сотрудник'
    return {'Hello': result}


# А почему async? А потому что мы пишем асинхронное приложение!
# Все обработчики запросов будем объявлять через async def.
if __name__ == '__main__':
    # Команда на запуск uvicorn. При необходимости здесь же можно указать
    #  хост, порт и другие параметры сервера.
    uvicorn.run('main:app', reload=True)
