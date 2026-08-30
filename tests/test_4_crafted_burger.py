import pytest
from data import Data
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#выбран метод проверки скролла путем отслеживания универсального токена класса в узлах
#Для проверки можно скомпоновать в единый тест скролла меню с использованием параметизщации 

class TestCraftedBurger:

    @pytest.mark.parametrize('anhor',[0,1,2])
    def test_scroll_move_anhor(self,driver,anhor):
        driver.get(Data.stellarburgers_url)

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LIST_ANCHOR_MENU))
        list_anchor = driver.find_elements(*Locators.LIST_ANCHOR_MENU)
        #для проверки перехода к пункту "Булочки" необходимо сместить фокус
        if anhor == 0:
            list_anchor[anhor+1].click()

        list_anchor[anhor].click()

        #обновляем данные в переменной
        list_anchor = driver.find_elements(*Locators.LIST_ANCHOR_MENU)

        #для проверки перехода необходимо получить классы объекта
        class_attr = list_anchor[anhor].get_attribute('class')
        class_names = class_attr.split()

        assert Data.key_anchor_pozition in class_names