import pytest
from common import is_element_in_container
from data import Data
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCraftedBurger:

    @pytest.mark.parametrize('anhor',[0,1,2])
    def test_scroll_move_anhor_in_container(self,driver,anhor):
        driver.get(Data.STELLARBURGERS_URL)

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LIST_TOP_MENU))
        #Заносим в переменные локаторы
        list_top_menu = driver.find_elements(*Locators.LIST_TOP_MENU)
        container = driver.find_element(*Locators.CONTAINER_ELEMENT_CONSTRUCTOR)
        list_sections = driver.find_elements(*Locators.LIST_SECTIONS)
        last_list_top = len(list_top_menu)-1
        
        #перемещаемся к последнему элементу в списке, вычисление нужно для уменьшения затрат при добавлении новых кнопок меню раздела
        list_top_menu[last_list_top].click()
        WebDriverWait(driver, 10).until(lambda a: Data.KEY_ANCHOR_CLASS in list_top_menu[last_list_top].get_attribute('class'))
        #перемещаемся к проверяемому элементу
        list_top_menu[anhor].click()
        WebDriverWait(driver, 10).until(lambda a: Data.KEY_ANCHOR_CLASS in list_top_menu[anhor].get_attribute('class'))

        #Data.KEY_ANCHOR_CLASS in list_top_menu[anhor] - уже подтвердил наличие CSS якоря в верхнем меню
        #проверяем что элемент названия раздела находится в видимой части блока
        
        assert is_element_in_container(list_sections[anhor], container)
        