
import re
import pytest
from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from utils.regex_templates import COST_REGEX

class ProductPage(BasePage):
    
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"
    
    
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
    
    
    def should_be_added_to_basket(self) -> None:
        if not self.is_element_present(*ProductPageLocators.PRODUCT_CARD_BOOK_TITLE):
            pytest.fail("Book title in product card is not presented")
        
        if not self.is_element_present(*ProductPageLocators.POPUP_ADDED_TO_BASKET_BOOK_TITLE):
            pytest.fail("Book title in 'added to basket' popup is not presented")
        
        product_card_book_title = self.browser.find_element(*ProductPageLocators.PRODUCT_CARD_BOOK_TITLE).text
        alert_added_to_basket_book_title = self.browser.find_element(*ProductPageLocators.POPUP_ADDED_TO_BASKET_BOOK_TITLE).text
        assert product_card_book_title == alert_added_to_basket_book_title, f"according to popup, added {alert_added_to_basket_book_title}, expected {product_card_book_title}"
    
    
    def should_be_updated_price(self) -> None:

        if not self.is_element_present(*ProductPageLocators.HEADER_BASKET_TOTAL):
            pytest.fail("Basket total price is not presented in header")
        
        if not self.is_element_present(*ProductPageLocators.POPUP_BASKET_TOTAL):
            pytest.fail("Basket total price is not presented in popup")

        header_basket_total_text = self.browser.find_element(*ProductPageLocators.HEADER_BASKET_TOTAL).text
        header_basket_total_price = re.findall(COST_REGEX, header_basket_total_text)
        if (header_basket_total_price):
            print(f"header basket total text: {re.findall(COST_REGEX, header_basket_total_text)}")
            header_basket_total_price = re.findall(COST_REGEX, header_basket_total_text)[0]
        else:
            pytest.fail(f"Can't find price in header basket total text: {header_basket_total_text}")

        popup_basket_total_text = self.browser.find_element(*ProductPageLocators.POPUP_BASKET_TOTAL).text
        popup_basket_total_price = re.findall(COST_REGEX, popup_basket_total_text)
        if (re.findall(COST_REGEX, popup_basket_total_text)):
            popup_basket_total_price = re.findall(COST_REGEX, popup_basket_total_text)[0]
        else:
            pytest.fail(f"Can't find price in popup basket total text: {popup_basket_total_text}")

        assert header_basket_total_price == popup_basket_total_price, f"different total basket prices in header and popup (in header: {header_basket_total_price}, in popup: {popup_basket_total_price})"
    