from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage():
    
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
    
    def open(self):
        self.browser.get(self.url)
    
    def is_element_present(self, how, what):
        try:
            element = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True