import random

from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()  # seed-Функция начального числа используется для хранения случайного метода генерации одних и тех же случайных чисел при многократном выполнении кода на одной или разных машинах.


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.middle_name() + " " + faker_ru.last_name(),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        email=faker_ru.email(),
        age=random.randint(10, 80),
        salary=random.randint(1000, 5000),
        department=faker_ru.job(),
    )
