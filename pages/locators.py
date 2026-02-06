from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//*[contains(@href, 'basket')]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    SUCCESS_REGISTER_ALERT = (By.CLASS_NAME, "alert-success")
    
class BasketPageLocators():
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    
class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL_FIELD = (By.ID, "id_registration-email")
    REGISTER_PASSWORD_FIELD = (By.ID, "id_registration-password1")
    REGISTER_CONFIRM_PASSWORD_FIELD = (By.ID, "id_registration-password2")
    REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"][type="submit"]')

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_CARD_BOOK_TITLE = (By.CSS_SELECTOR, '.product_main > h1')
    POPUP_ADDED_TO_BASKET_BOOK_TITLE = (By.XPATH, "//*[@id='messages']//strong[1]")
    HEADER_BASKET_TOTAL = (By.XPATH, "//header[contains(@class, 'header')]//div[contains(@class, 'basket')]")
    POPUP_BASKET_TOTAL = (By.CSS_SELECTOR, '#messages > div:nth-child(3) .alertinner')