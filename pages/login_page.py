import pytest
from time import sleep
from .locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        print(self.browser.current_url)
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        
    def register_new_user(self, email, password):

        if not self.is_element_present(*LoginPageLocators.REGISTER_EMAIL_FIELD):
            pytest.fail("Email field is not presented")

        if not self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_FIELD):
            pytest.fail("Password field is not presented")

        if not self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_FIELD):
            pytest.fail("Password confirmation field is not presented")

        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT_BUTTON).click()