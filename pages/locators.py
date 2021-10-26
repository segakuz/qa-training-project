from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_FORM_MAIL = (By.NAME, "login-username")
    LOGIN_FORM_PASSWORD = (By.NAME, "login-password")

    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_MAIL = (By.NAME, "register-username")
    REGISTER_FORM_PASSWORD = (By.NAME, "register-password1")
    REGISTER_FORM_PASSWORD_CONFIRMATION = (By.NAME, "register-password2")

class ProductPageLocators():
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:first-child .alertinner")
    BASKET_VALUE_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:last-child .alertinner p")
