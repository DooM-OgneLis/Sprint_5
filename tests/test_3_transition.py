from data import Data
from locators import Locators
from common import autorization
from selenium.webdriver.support.ui import WebDriverWait

class TestTransition:    
    #проверка перехода в личный кабинет авторизованного пользователя
    def test_transition_personal_accaunt(self, driver, users):
        driver.get(Data.STELLARBURGERS_URL)
        
        driver.find_element(*Locators.URL_PERSONAL_ACCOUNT).click()
        #выполнение авторизации
        autorization(driver, users)

        WebDriverWait(driver, 10).until(lambda d: d.current_url != Data.STELLARBURGERS_URL)
        WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")

        assert driver.current_url in Data.STELLARBURGERS_ACCOUNT

    #проверка перехода в конструктор из личного кабинета авторизованного пользователя
    def test_transition_constructor(self, driver, users):
        driver.get(Data.STELLARBURGERS_URL)
        
        driver.find_element(*Locators.URL_PERSONAL_ACCOUNT).click()
        #выполнение авторизации
        autorization(driver, users)

        WebDriverWait(driver, 10).until(lambda d: d.current_url != Data.STELLARBURGERS_URL)

        driver.find_element(*Locators.URL_CONSTRUCTOR).click()

        WebDriverWait(driver, 10).until(lambda d: d.current_url != Data.STELLARBURGERS_ACCOUNT)
        WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")

        assert driver.current_url == Data.STELLARBURGERS_URL
