from data import Data
from locators import Locators
from common import send_data_in_form_reg
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistration:
    #переменная класса для всех тестов регистрации, она нужна для поля "Имя"
    user_name = "Aleksey"   #не назначается константной переменной, так как может быть изменена в коде при необходимости
                            #не внесена в Data, используется только при регистрации

    #проверка успешной регистрации
    def test_registration_successfully(self, driver, users):

        driver.get(Data.STELLARBURGERS_REGISTER)

        send_data_in_form_reg(driver, self.user_name, users["email"], users["password"])

        WebDriverWait(driver, 10).until(lambda d: d.current_url != Data.STELLARBURGERS_REGISTER)

        assert driver.current_url == Data.STELLARBURGERS_LOGIN

    #проверка вывода ошибки при вводе пароля менее 6 символов
    def test_input_error_text_password_visiblity(self, driver):
        driver.get(Data.STELLARBURGERS_REGISTER)

        send_data_in_form_reg(driver, '', '', '1234')
    
        input_error = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.INPUT_ERROR_PASS))
    
        assert input_error.is_displayed()
    
    #проверка вывода ошибки при попытке регистрации с некорректной почтой
    def test_input_error_text_form_registration_visiblity(self, driver, users):
        driver.get(Data.STELLARBURGERS_REGISTER)
        
        send_data_in_form_reg(driver, self.user_name, 'vasya_pupkin.yandex.ru', users['password'])
            
        input_error = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.INPUT_ERROR_FORM_REG))
        
        assert input_error.is_displayed()

    #проверка вывода ошибки при попытке регистрации с уже зарегистрированной почтой
    def test_registration_error_mail_busy(self, driver, users):
        driver.get(Data.STELLARBURGERS_REGISTER)
    
        send_data_in_form_reg(driver, self.user_name, users["email"], users["password"])

        input_error = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.INPUT_ERROR_FORM_REG))
                
        assert input_error.is_displayed()
