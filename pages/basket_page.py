from training_project.pages.locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY), 'Basket is not empty, but should be'

    def should_be_empty_basket_message(self):
        required_text = 'basket is empty'
        empty_basket_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert required_text in empty_basket_message, 'Empty basket message is not present'
