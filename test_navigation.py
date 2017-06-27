import unittest

from selenium import webdriver

from header import Header
from link import Link
from login_page import LoginPage


class TestFooter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()

    def test_footer_links(self):
        links = (
            # MEN
            'View All Men',
            #'New Arrivals',
            'Shirts',
            'Tees, Knits and Polos',
            #'Pants & Denim',
            'Blazers',
            # WOMEN
        )

        head = (
            'Men',
            # 'New Arrivals',
            'Shirts',
            'Tees, Knits and Polos',
            # 'Pants & Denim',
            'Blazers',
        )

        LoginPage(self.browser).open()
        for link, heads in zip(links, head):
            Link(self.browser, 'Men').hover()
            Link(self.browser, link).click()
            self.assertTrue(Header(self.browser, heads).is_visible)