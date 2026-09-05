import pytest
from data import Data
from locators import Locators
from common import autorization
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin:
    #проверка перехода на страницу авторизации из разных мест и авторизация 
    @pytest.mark.parametrize('url, locator',[[Data.STELLARBURGERS_URL, Locators.URL_PERSONAL_ACCOUNT],[Data.STELLARBURGERS_URL, Locators.BUTTON_LOG_IN_ACCOUNT],[Data.STELLARBURGERS_FORGOT_PASSWORD, Locators.URL_AUTHORIZATION],[Data.STELLARBURGERS_REGISTER, Locators.URL_AUTHORIZATION]])
    def test_goto_login_form_open_url(self, driver, users, url, locator):
        driver.get(url)

        driver.find_element(*locator).click()
        #ожидаем не только смену страницы, но и полную ее загрузку
        WebDriverWait(driver, 10).until(lambda d: d.current_url != url)
        WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
        
        autorization(driver, users)
        #в некоторых случая возникает конфликт проверки ввиду отсутствия "/profile" в адресе при переходе в личный кабинет
        assert driver.current_url in Data.STELLARBURGERS_ACCOUNT

    #проверка прямой авторизации на сайте
    def test_loggin_autorization_complite(self, driver, users):
        driver.get(Data.STELLARBURGERS_LOGIN)

        autorization(driver, users)
        #в некоторых случая возникает конфликт проверки ввиду отсутствия "/profile" в адресе при переходе в личный кабинет
        assert driver.current_url in Data.STELLARBURGERS_ACCOUNT

    #проверка выхода из аккаунта после авторизации
    def test_log_off_accaunt(self, driver, users):
        driver.get(Data.STELLARBURGERS_LOGIN)
        #для проверки выхода из аккаунта, в него необходимо зайти
        autorization(driver, users)

        #ожидаем пока кнопка выхода загрузится на странице, после чего производим выход из аккаунта нажатием на нее
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.BUTTON_LOG_OFF))
        driver.find_element(*Locators.BUTTON_LOG_OFF).click()

        WebDriverWait(driver, 10).until(lambda d: d.current_url != Data.STELLARBURGERS_ACCOUNT)
        #для подтверждения выхода из профиля повторно входим в личный кабинет
        driver.find_element(*Locators.URL_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 10).until(lambda d: d.current_url != Data.STELLARBURGERS_URL)
        WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
        
        assert driver.current_url in Data.STELLARBURGERS_LOGIN
