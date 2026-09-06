import pytest
import random
import string
from data import Data
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()

    yield driver

    driver.quit()

#функция генерации почты и пароля для передачи в формы регистрации и авторизации
@pytest.fixture(scope="session", autouse=True)
def users():
    random.seed()
    #для большей читаемости кода создаем набор переменных
    email_suffix = random.randint(100, 999) #случайное число в названии
    num_variants_domain = len(Data.EMAIL_DOMAIN)-1 #переменная хранит кол-во вариантов доменов
    email_domain = Data.EMAIL_DOMAIN[random.randint(0, num_variants_domain)] #позволяет увеличить вариативность регистрации

    #Генерация случайного пароля
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    generate_random_password = "".join(random.choice(chars) for _ in range(random.randint(6,16)))

    email = f"aleksey_sergeev_52_{email_suffix}@{email_domain}" #компановка почты
    password = generate_random_password

    return {"email": email, "password": password}


