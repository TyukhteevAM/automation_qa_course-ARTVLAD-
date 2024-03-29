import random

from data.data import Person, Color, Date
from faker import Faker

faker_ru = Faker('ru_RU')
faker_en = Faker('EN')
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
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile_number=faker_ru.msisdn()
    )

def generated_file():
    path = rf'C:\Users\79825\PycharmProjects\automation_qa_course-ARTVLAD-\filetest{random.randint(0, 999)}.txt' # r-регулярное выражение (чтобы не экранировать слэши)
    file = open(path, 'w+')
    file.write(f'Hello, world{random.randint(0, 999)}')
    file.close()
    return file.name, path

def generated_subject():
    data = ["Hindi", "English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science", "Commerce", "Accounting", "Economics", "Arts", "Social Studies", "History", "Civics"]
    subject = (random.choice(data))
    return subject

def generated_color():
    yield Color(
        color_name=["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta","Aqua"]
    )

def generated_date():
    yield Date(
        year=faker_en.year(),
        month=faker_en.month_name(),
        day=faker_en.day_of_month(),
        time="12:00"
    )