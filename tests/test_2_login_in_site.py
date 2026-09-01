import pytest
from data import Data
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#компановка дубля кода в единую общую функцию
def autorization(driver, users):
    driver.find_element(*Locators.INPUT_MAIL).send_keys(users["eMail"])
    driver.find_element(*Locators.INPUT_PASS).send_keys(users["password"])

    driver.find_element(*Locators.BUTTON_LOG_IN).click()

    WebDriverWait(driver, 10).until(lambda d: d.current_url != Data.stellarburgers_login)
    #проверка входа в аккаун производится входом в профиль
    driver.find_element(*Locators.URL_PERSONAL_ACCOUNT).click()

    WebDriverWait(driver, 10).until(lambda d: d.current_url != Data.stellarburgers_url)
    WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")

class TestLogin:
    #проверка перехода на страницу авторизации из разных мест и авторизация 
    @pytest.mark.parametrize('url, locator',[[Data.stellarburgers_url, Locators.URL_PERSONAL_ACCOUNT],[Data.stellarburgers_url, Locators.BUTTON_LOG_IN_ACCOUNT],[Data.stellarburgers_forgot_password, Locators.URL_AUTHORIZATION],[Data.stellarburgers_register, Locators.URL_AUTHORIZATION]])
    def test_goto_login_form_open_url(self, driver, users, url, locator):
        driver.get(url)

        driver.find_element(*locator).click()
        #ожидаем не только смену страницы, но и полную ее загрузку
        WebDriverWait(driver, 10).until(lambda d: d.current_url != url)
        WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
        
        autorization(driver, users)
        #в некоторых случая возникает конфликт проверки ввиду отсутствия "/profile" в адресе при переходе в личный кабинет
        assert driver.current_url in Data.stellarburgers_account

    #проверка прямой авторизации на сайте
    def test_loggin_autorization_complite(self, driver, users):
        driver.get(Data.stellarburgers_login)

        autorization(driver, users)
        #в некоторых случая возникает конфликт проверки ввиду отсутствия "/profile" в адресе при переходе в личный кабинет
        assert driver.current_url in Data.stellarburgers_account

    #проверка выхода из аккаунта после авторизации
    def test_log_off_accaunt(self, driver, users):
        driver.get(Data.stellarburgers_url)
        #для обеспечения точности теста необходима проверка сохранения входа в аккаунт
        driver.find_element(*Locators.URL_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 10).until(lambda d: d.current_url != Data.stellarburgers_url)
        if driver.current_url == Data.stellarburgers_login:
            driver.find_element(*Locators.INPUT_MAIL).send_keys(users["eMail"])
            driver.find_element(*Locators.INPUT_PASS).send_keys(users["password"])
            
            driver.find_element(*Locators.BUTTON_LOG_IN).click()

            WebDriverWait(driver, 10).until(lambda d: d.current_url != Data.stellarburgers_login)
            #так как сайт перенаправляет на домашнюю страницу после авторизации, повторно проходим в личный кабинет
            driver.find_element(*Locators.URL_PERSONAL_ACCOUNT).click()

        input_error = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.BUTTON_LOG_OFF))
        driver.find_element(*Locators.BUTTON_LOG_OFF).click()

        WebDriverWait(driver, 10).until(lambda d: d.current_url != Data.stellarburgers_account)
        #для подтверждения выхода из профиля повторно входим в личный кабинет
        driver.find_element(*Locators.URL_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 10).until(lambda d: d.current_url != Data.stellarburgers_url)
        WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
        #в некоторых случая возникает конфликт проверки ввиду отсутствия "/profile" в адресе при переходе в личный кабинет
        assert driver.current_url in Data.stellarburgers_login