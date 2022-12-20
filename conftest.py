import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# фикстура, функция выполняющая что-то до или после теста
@pytest.fixture(scope="function")
def driver():
    '''setup-все что происходит перед запуском теста'''
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window() #открывает окно во весь экран
    yield driver
    '''tirdown-все что происходит после запуска теста'''
    driver.quit()