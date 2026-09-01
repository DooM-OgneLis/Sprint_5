from selenium.webdriver.common.by import By 

class Locators:
    #локаторы общих полей на сайте
    #Используется поиск полей ввода по тексу для имени и почты, ввиду отсутствия уникальных параметров в тегах
    INPUT_MAIL = (By.XPATH, "//label[text() = 'Email']/../input") #поле ввода почты в формах
    #для поля пароль в родительском теге присутствует уникальное значение
    INPUT_PASS = (By.XPATH, "//*[contains(@class, 'input_type_password')]/input") #поле ввода пароля в формах
    INPUT_ERROR_PASS = (By.XPATH, "//*[contains(@class, 'input_type_password')]/../p[contains(@class, 'input__error')]") #выводимая ошибка при некорректном пароле (поиск тега с классом пароль необходим для уточнения рассположения выводимой ошибки, так как все выводимые ошибки имеют одинаковые строения)

    #Локаторы формы регистрации
    INPUT_NAME = (By.XPATH, "//label[text() = 'Имя']/../input") #поле ввода почты в формах
    BUTTON_REGISTRATION = (By.XPATH, "//button[text() = 'Зарегистрироваться']") #кнопка "Зарегистрироваться"
    INPUT_ERROR_FORM_REG = (By.XPATH, "//form/../p[contains(@class, 'input__error')]") #ошибка заполнения формы

    #кнопки навигации на сайте
    URL_PERSONAL_ACCOUNT = (By.XPATH, "//a[contains(@href, 'account')]") #Ссылка в личный кабинет
    URL_AUTHORIZATION = (By.XPATH, "//a[contains(@href, 'login')]") #Ссылка на авторизацию из форм регистрации и восстановления пароля
    URL_CONSTRUCTOR = (By.XPATH, "//p[text() = 'Конструктор']/..")
    BUTTON_LOG_IN_ACCOUNT = (By.XPATH, "//button[text() = 'Войти в аккаунт']") #Кнопка входа в аккаунт с главной страницы

    #локаторы страницы входа в аккаунт
    BUTTON_LOG_IN = (By.XPATH, "//button[text() = 'Войти']") #Кнопка входа в аккаунт со страницы авторизации

    #локаторы страницы профиля
    BUTTON_LOG_OFF = (By.XPATH, "//button[text() = 'Выход']") #Кнопка выхода из аккаунта в личном кабинете

    #локаторы главной страницы "Конструктор"
    LIST_ANCHOR_MENU = (By.XPATH, "//div[contains(@style, 'display: flex;')]/div") #собирает все объекты верхнего меню сборки бургера