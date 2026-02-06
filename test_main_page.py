import pytest
from pages.basket_page import BasketPage
from pages.main_page import MainPage
from pages.login_page import LoginPage

MAIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="function", autouse=True)
def setup(browser) -> MainPage:
    page = MainPage(browser, MAIN_PAGE_LINK)
    page.open()
    return page

@pytest.mark.login_guest
class TestLoginFromMainPage():
    
    def test_guest_can_go_to_login_page(self, setup, browser):
        page: MainPage = setup
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, setup):
        page:MainPage = setup
        page.should_be_login_link()
   
    
def test_guest_cant_see_product_in_basket_opened_from_main_page(setup, browser):
    page: MainPage = setup
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket_message()
    basket_page.should_not_be_products_in_basket()