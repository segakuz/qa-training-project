from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_to_basket(self):
        btn_element = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn_element.click()

    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), 'Add to basket button is not present'

    def should_be_success_messages(self):
        self.should_be_product_title_in_success_message(self.get_product_title())
        self.should_be_product_price_in_success_message(self.get_product_price())

    def should_be_product_title_in_success_message(self, product_title):
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        required_message = f"{product_title} has been added to your basket."

        assert required_message in success_message, 'Product title is not in the success message'

    def should_be_product_price_in_success_message(self, product_price):
        basket_value_message = self.browser.find_element(*ProductPageLocators.BASKET_VALUE_MESSAGE).text
        required_message = f"Your basket total is now {product_price}"

        assert required_message in basket_value_message, 'Incorrect basket change message'

    def get_product_title(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
