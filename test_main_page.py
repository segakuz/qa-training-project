from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.locators import MainPageLocators
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():

    def test_guest_can_go_to_login_page(self, browser):
        link = MainPageLocators.MAIN_PAGE_URL
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()

        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = MainPageLocators.MAIN_PAGE_URL
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


@pytest.mark.basket
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = MainPageLocators.MAIN_PAGE_URL
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()

    basket_page = BasketPage(browser, link, 1)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_message()
