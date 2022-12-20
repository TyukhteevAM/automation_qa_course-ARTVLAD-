from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed() # seed-Функция начального числа используется для хранения случайного метода генерации одних и тех же случайных чисел при многократном выполнении кода на одной или разных машинах.

def generated_person():
    yield Person(
    full_name=faker_ru.first_name() + " " + faker_ru.middle_name() + " " + faker_ru.last_name(),
    email=faker_ru.email(),
    current_address=faker_ru.address(),
    permamemt_address=faker_ru.address(),
    )