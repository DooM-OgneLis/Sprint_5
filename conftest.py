import pytest
import random
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()

    yield driver

    driver.quit()
    
@pytest.fixture(scope="session")
def users():
    #для обеспечения корректного тестирования, используется случайное значение в почте для каждого запуска тестов
    return {
        "userName": 'aleksey',
        "eMail": f'aleksey_sergeev_52_{random.randint(100,999)}@yandex.ru',
        "password": 'BackToTests!234'
        }

