from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert 'login' in current_url, 'There is an incorrect login page url.'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented.'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not presented.'

    def register_new_user(self, email, password):
        register_form_mail = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_MAIL)
        register_form_mail.send_keys(email)
        
        register_form_password = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD)
        register_form_confirmation = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_CONFIRMATION)
        register_form_password.send_keys(password)
        register_form_confirmation.send_keys(password)

        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    def get_fake_email(self):
        return self.rand_str() + '@testmail.ru'

    def get_fake_password(self):
        return self.rand_str(size=9)
