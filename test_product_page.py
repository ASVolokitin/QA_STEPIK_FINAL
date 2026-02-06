import pytest
import faker
from pages.basket_page import BasketPage
from pages.locators import MainPageLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage

PRODUCT_PAGE_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
LOGIN_PAGE_LINK = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}?promo=offer{no}" if no != 7
        else pytest.param("bugged_link", marks=pytest.mark.xfail) for no in range(10)]

class TestUserAddToBasketFromProductPage():
    
    @pytest.fixture
    def setup(self, browser) -> ProductPage:
        login_page = LoginPage(browser, LOGIN_PAGE_LINK)
        login_page.open()
        f = faker.Faker()
        login_page.register_new_user(f.email(), f.password())
        main_page = MainPage(browser, browser.current_url)
        if main_page.is_not_element_present(*MainPageLocators.SUCCESS_REGISTER_ALERT):
            pytest.fail("Should be successful registration alert on main page")
        product_page = ProductPage(browser, PRODUCT_PAGE_LINK)
        product_page.open()
        return product_page

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, setup):
        page: ProductPage = setup
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_added_to_basket()
        page.should_be_updated_price()
    
    @pytest.mark.xfail
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, setup):
        page: ProductPage = setup
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_not_be_success_message_after_adding_product_to_basket()


@pytest.mark.need_review
# @pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_PAGE_LINK)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_added_to_basket()
    page.should_be_updated_price()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_PAGE_LINK)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message_after_adding_product_to_basket()

def test_guest_can_see_add_to_basket_button(browser):
    page = ProductPage(browser, PRODUCT_PAGE_LINK)
    page.open()
    page.should_be_add_to_basket_button()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, PRODUCT_PAGE_LINK)
    page.open()
    page.should_not_be_success_message_after_adding_product_to_basket()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_PAGE_LINK)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_disappear_success_message_after_adding_product_to_basket()
    
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, PRODUCT_PAGE_LINK)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_PAGE_LINK)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket_message()
    basket_page.should_not_be_products_in_basket()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_PAGE_LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()