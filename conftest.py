from datetime import datetime

import allure
import pytest
from allure_commons._allure import attach
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from data import data


# фикстура, функция выполняющая что-то до или после теста
@pytest.fixture(scope="function")
def driver():
    '''setup-все что происходит перед запуском теста'''
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()  # открывает окно во весь экран
    yield driver
    '''tiredown-все что происходит после запуска теста'''
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
    driver.quit()
