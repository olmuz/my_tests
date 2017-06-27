from support.pages.base_page import BasePage

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

    def login(self, email, pwd):
        email_input = self.find_element('email')
        pwd_input = self.find_element('password')
        email_input.clear()
        email_input.send_keys(email)
        pwd_input.send_keys(pwd)

        self.find_element('login_button').click()
