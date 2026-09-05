import pytest
import common 
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
        
        #производим вычисление видимости проверяемого объекта в скролле блока
        common.get_scroll_top(driver, container)
        #перемещаемся к последнему элементу в списке, вычисление нужно для уменьшения затрат при добавлении новых кнопок меню раздела
        list_top_menu[len(list_top_menu)-1].click()
        list_top_menu[anhor].click()
        common.wait_scroll_settled(driver, container)
        #заносим результат обнаружения в переменную
        result = common.is_section_visible(driver, container, list_sections[anhor])

        assert result
        