import time
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

#для решения задачи с тестом скролла требуется написание скрипта на javascript
#ввиду нехватки времени изучать базовый синтаксис JS, код хелпера запрошен у AI
#по запросу "определение видимости элемента в блоке со скролом"

def scroll_to_element(driver, element):
    #Скроллит контейнер к элементу.
    driver.execute_script("arguments[0].scrollIntoView({block: 'start'});", element)


def get_scroll_top(driver, container):
    #Возвращает текущий scrollTop контейнера.
    return driver.execute_script("return arguments[0].scrollTop;", container)


def is_section_visible(driver, container, section):
    #Проверяет, что секция видна в видимой области контейнера.
    return driver.execute_script("""
    var c = arguments[0], s = arguments[1]; 
    var rc = c.getBoundingClientRect(); 
    var rs = s.getBoundingClientRect(); 
    return rs.top >= rc.top - 2 && rs.top < rc.bottom - 2;"""
    , container, section)


def wait_scroll_settled(driver, container, timeout=5, delay=0.2):
    #Ждёт, пока scrollTop перестанет меняться (для плавного скролла).
    prev = get_scroll_top(driver, container)
    deadline = time.time() + timeout
    while time.time() < deadline:
        time.sleep(delay)
        curr = get_scroll_top(driver, container)
        if curr == prev:
            return curr
        prev = curr
    return curr


def get_section_offset_top(driver, container, section):
    #Возвращает offsetTop секции внутри контейнера — куда должен прийти скролл.
    return driver.execute_script("""
        var c = arguments[0], s = arguments[1]; 
        var offset = 0; 
        var el = s; while (el && el !== c) {
            offset += el.offsetTop; 
            el = el.offsetParent;
        }
        return offset;"""
    , container, section)
    