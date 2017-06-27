import unittest

from selenium import webdriver

from support.pages.login_page import LoginPage


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()

    def setUp(self):
        LoginPage(self.browser).open()

    def testLoginSuccess(self):
        login = LoginPage(self.browser)
        log_data = {
            'email' : 'semensosnitski@gmail.com',
            'password' : 'abrakadabra',
        }

        for key, value in log_data.items():

            login.find_element(key).send_keys(value)
        login.find_element('login_button').click()

        self.assertIn('My Account', self.browser.title)


