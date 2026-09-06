from data import Data
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait

#функция регистрации
def send_data_in_form_reg (driver, user_name, email, password):
    driver.find_element(*Locators.INPUT_NAME).send_keys(user_name)
    driver.find_element(*Locators.INPUT_MAIL).send_keys(email)
    driver.find_element(*Locators.INPUT_PASS).send_keys(password)

    #нажатие на кнопку регистрации
    driver.find_element(*Locators.BUTTON_REGISTRATION).click()

#функция авторизации
def autorization(driver, users):
    driver.find_element(*Locators.INPUT_MAIL).send_keys(users["email"])
    driver.find_element(*Locators.INPUT_PASS).send_keys(users["password"])

    driver.find_element(*Locators.BUTTON_LOG_IN).click()

    WebDriverWait(driver, 10).until(lambda d: d.current_url != Data.STELLARBURGERS_LOGIN)
    #проверка входа в аккаун производится входом в профиль
    driver.find_element(*Locators.URL_PERSONAL_ACCOUNT).click()

    WebDriverWait(driver, 10).until(lambda d: d.current_url != Data.STELLARBURGERS_URL)
    WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")

#Проверяет, попадает ли элемент в видимую область контейнера
def is_element_in_container(element, container_el):
    el_rect = element.rect
    cont_rect = container_el.rect
    return (
        cont_rect["y"] <= el_rect["y"]
        and el_rect["y"] + el_rect["height"] <= cont_rect["y"] + cont_rect["height"]
    )