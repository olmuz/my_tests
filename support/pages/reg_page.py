from selenium.common.exceptions import NoSuchElementException

from support.pages.base_page import BasePage


class RegPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.url = "http://magento-demo.lexiconn.com/customer/account/create/"
        self.locators = {
            # fields
            'first name' : '//input[@name="firstname"]',
            'last name' : '//input[@name="lastname"]',
            'email' : '//input[@name="email"]',
            'password' : '//input[@name="password"]',
            'confirm password' : '//input[@name="confirmation"]',
            'password_error' : '//div[@id="advice-validate-cpassword-confirmation"]',

            #buttons
            'button' : '//button[@title="Register" and @type="submit"]'

        }


    @property
    def is_password_validation_error(self):
        try:
            self.find_element('password_error')
        except NoSuchElementException:
            return False
        else:
            return True

    def open(self):
        self.browser = self.browser.get(self.url)

