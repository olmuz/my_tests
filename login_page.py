from base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.url = 'http://magento-demo.lexiconn.com/customer/account/login/'
        self.locators = {
            'email' : '//input[@name="login[username]"]',
            'password' : '//input[@name="login[password]"]',
            'login_button' : '//button[@title="Login" and @type="submit"]'

        }

    def open(self):
        self.browser = self.browser.get(self.url)
