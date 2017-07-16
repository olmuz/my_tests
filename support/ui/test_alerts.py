import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

import support.ui as ui
from support.pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class TestAlert(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()

    '''def test_simple_alert(self):
    # create alert with JavaScript injection
        LoginPage(self.browser).open()
        self.browser.execute_script('alert("Simple alert");')
        # wait for alert
        WebDriverWait(self.browser, 5).until(
            EC.alert_is_present()
        )
        sleep(2)
        self.browser.switch_to.alert.accept()

    def test_confirmation_alert(self):
        LoginPage(self.browser).open()
        self.browser.execute_script('confirm("Confirm alert");')
       # wait for alert
        WebDriverWait(self.browser, 5).until(
            EC.alert_is_present()
       )
        sleep(2)
        # Cancel alert
        self.browser.switch_to.alert.dismiss()
        # Accept alert
        self.browser.switch_to.alert.accept()

    def test_prompt_alert(self):
        LoginPage(self.browser).open()
        self.browser.execute_script('prompt("Prompt alert");')
       # wait for alert
        WebDriverWait(self.browser, 5).until(
            EC.alert_is_present()
        )

        # Send some text
        alert = self.browser.switch_to.alert
        alert.send_keys('some text')
        sleep(2)
        self.browser.switch_to.alert.accept()'''

    def test_cookies(self):
        self.browser = webdriver.Chrome()
        ac = ActionChains(self.browser)
        ac.send_keys(Keys.CONTROL)
        ac.send_keys(Keys.SHIFT)
        ac.send_keys('N')
        ac.perform()

        page = LoginPage(self.browser)
        page.open()
        page.login('semensosnitski@gmail.com', 'abrakadabra')




