import pytest
from pages.product_page import ProductPage

PAGE_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}?promo=offer{no}" if no != 7
        else pytest.param("bugged_link", marks=pytest.mark.xfail) for no in range(10)]


def test_guest_can_see_add_to_basket_button(browser):
    page = ProductPage(browser, PAGE_LINK)
    page.open()
    page.should_be_add_to_basket_button()


@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_added_to_basket()
    page.should_be_updated_price()