from selenium.webdriver.common.by import By

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
