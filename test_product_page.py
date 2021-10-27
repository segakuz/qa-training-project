from training_project.pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest

@pytest.mark.need_review
@pytest.mark.long
@pytest.mark.parametrize('promo_offer', [pytest.param(i, marks=pytest.mark.xfail(i==7, reason='Temporary bug')) for i in range(1)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_btn()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_success_messages()

@pytest.mark.xfail(reason="Should fail")
def test_guest_cant_see_success_message_after_adding_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link, 1)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link, 1)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason='Should fail')
def test_success_message_disappeared_after_adding_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link, 1)
    page.open()
    page.add_product_to_basket()
    page.should_disappear_of_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link, 1)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link, 1)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
@pytest.mark.basket
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link, 1)
    page.open()
    page.go_to_basket_page()

    basket_page = BasketPage(browser, link, 1)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_message()

class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        page = LoginPage(browser, link, 1)
        page.open()
        page.register_new_user(page.get_fake_email(), page.get_fake_password())
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        page = ProductPage(browser, link, 1)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link, 1)
        page.open()
        page.should_be_add_to_basket_btn()
        page.add_product_to_basket()
        page.should_be_success_messages()
