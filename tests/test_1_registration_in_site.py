from data import Data
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistration:
    #проверка вывода ошибки при вводе пароля менее 6 символов
    def test_input_error_text_password_visiblity(self, driver):
        driver.get(Data.stellarburgers_register)

        driver.find_element(*Locators.INPUT_PASS).send_keys("adgj") 
        driver.find_element(*Locators.INPUT_MAIL).click()

        input_error = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.INPUT_ERROR_PASS))

        assert input_error.is_displayed()

    #проверка вывода ошибки при попытке регистрации с некорректной почтой
    def test_input_error_text_form_registration_visiblity(self, driver):
        driver.get(Data.stellarburgers_register)
    
        driver.find_element(*Locators.INPUT_NAME).send_keys("a")
        driver.find_element(*Locators.INPUT_MAIL).send_keys("a")
        driver.find_element(*Locators.INPUT_PASS).send_keys("qazwsx")
        
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()
        
        input_error = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.INPUT_ERROR_FORM_REG))
    
        assert input_error.is_displayed()

    #проверка успешной регистрации
    def test_registration_successfully(self, driver, users):
        global regUserEmail
        driver.get(Data.stellarburgers_register)

        driver.find_element(*Locators.INPUT_NAME).send_keys(users["userName"])
        driver.find_element(*Locators.INPUT_MAIL).send_keys(users["eMail"])
        driver.find_element(*Locators.INPUT_PASS).send_keys(users["password"])
 
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()

        WebDriverWait(driver, 10).until(lambda d: d.current_url != Data.stellarburgers_register)

        assert driver.current_url == Data.stellarburgers_login

    #проверка вывода ошибки при попытке регистрации с уже зарегистрированной почтой
    def test_registration_error_mail_busy(self, driver, users):
        driver.get(Data.stellarburgers_register)
    
        driver.find_element(*Locators.INPUT_NAME).send_keys(users["userName"])
        driver.find_element(*Locators.INPUT_MAIL).send_keys(users["eMail"])
        driver.find_element(*Locators.INPUT_PASS).send_keys(users["password"])
    
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()

        input_error = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.INPUT_ERROR_FORM_REG))
                
        assert input_error.is_displayed()