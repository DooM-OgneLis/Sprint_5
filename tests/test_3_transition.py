from data import Data
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait

#общий модуль проверки авторизации
def login_verification(driver,users):
    if driver.current_url == Data.stellarburgers_login:
        driver.find_element(*Locators.INPUT_MAIL).send_keys(users["eMail"])
        driver.find_element(*Locators.INPUT_PASS).send_keys(users["password"])
                    
        driver.find_element(*Locators.BUTTON_LOG_IN).click()
        
        WebDriverWait(driver, 10).until(lambda d: d.current_url != Data.stellarburgers_login)

        return True
    return False

class TestTransition:    
    #проверка перехода в личный кабинет авторизованного пользователя
    def test_transition_personal_accaunt(self, driver, users):
        driver.get(Data.stellarburgers_url)
        
        driver.find_element(*Locators.URL_PERSONAL_ACCOUNT).click()
        #Проверка выполнен ли вход, если выполняется, повторить переход в кабинет
        if login_verification(driver, users):
            driver.find_element(*Locators.URL_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 10).until(lambda d: d.current_url != Data.stellarburgers_url)
        WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")

        assert driver.current_url in Data.stellarburgers_account

    #проверка перехода в конструктор из личного кабинета авторизованного пользователя
    def test_transition_constructor(self, driver, users):
        driver.get(Data.stellarburgers_url)
        
        driver.find_element(*Locators.URL_PERSONAL_ACCOUNT).click()
        #Проверка выполнен ли вход, если выполняется, повторить переход в кабинет
        if login_verification(driver, users):
            driver.find_element(*Locators.URL_PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 10).until(lambda d: d.current_url != Data.stellarburgers_url)

        driver.find_element(*Locators.URL_CONSTRUCTOR).click()

        WebDriverWait(driver, 10).until(lambda d: d.current_url != Data.stellarburgers_account)
        WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")

        assert driver.current_url == Data.stellarburgers_url