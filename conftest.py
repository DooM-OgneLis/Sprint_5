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

#фикстура генерации данных для авторизации, по примеру генерации пароля от AI
@pytest.fixture(scope="session", autouse=True)
def _seed_random():
    # Фиксируем seed для всей сессии тестов
    random.seed()

#Генерация случайного пароля с единственным условием больше 6 символов
def generate_random_password(length = random.randint(6,16)):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(chars) for _ in range(length))

#функция генерации почты и пароля для передачи в формы регистрации и авторизации
@pytest.fixture(scope="session")
def users():
    #для большей читаемости кода создаем набор переменных
    email_suffix = random.randint(100, 999) #случайное число в названии
    num_variants_domain = len(Data.EMAIL_DOMAIN)-1 #переменная хранит кол-во вариантов доменов
    email_domain = Data.EMAIL_DOMAIN[random.randint(0, num_variants_domain)] #позволяет увеличить вариативность регистрации

    email = f"aleksey_sergeev_52_{email_suffix}@{email_domain}" #компановка почты
    password = generate_random_password()

    return {"email": email, "password": password}


