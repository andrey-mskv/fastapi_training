from enum import Enum
from typing import Optional, Union, Self

from pydantic import (
    BaseModel,
    Field,
    ConfigDict,
    field_validator,
    model_validator,
)

import re


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

    # «убрать лишние пробелы в строковых значениях»
    model_config = ConfigDict(
        str_strip_whitespace=True,
    )

    # Первый параметр функции-валидатора должен называться строго cls.
    # Во второй параметр передаётся значение проверяемого поля.
    @field_validator('name', 'surname')
    def cannot_be_numbers(cls, value: str):
        # в assert указываем проверочное условие
        # и сообщение об ошибке (опционально)
        assert (
            not value.isnumeric()
        ), 'Имя и фамилия не должны состоять из цифр'

        return value

    @model_validator(mode='after')
    def using_different_languages(self) -> Self:
        surname = ''.join(self.surname)

        checked_value = self.name + surname

        if re.search('[а-я]', checked_value, re.IGNORECASE) and re.search(
            '[a-z]', checked_value, re.IGNORECASE
        ):
            raise ValueError(
                'Пожалуйста, не смешивайте русские и латинские буквы'
            )

        return self
