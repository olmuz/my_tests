import unittest

from selenium import webdriver
from support.pages.login_page import LoginPage
from support.ui.link import Link
from support.ui.product import Product
from support.ui.button import Button


class TestPurchase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()

    def test_purchase(self):
        LoginPage(self.browser).open()
        LoginPage(self.browser).login('semensosnitski@gmail.com', 'abrakadabra')

        Link(self.browser, 'Accessories').hover()
        Link(self.browser, 'Jewelry').click()

        Product(self.browser, 'Swing Time Earrings').select()
        Button(self.browser, 'Add to Cart').click()
        self.assertEqual(self.browser.title, 'Shopping Cart')
