import unittest
from random import randint

from selenium import webdriver

from support.pages.reg_page import RegPage


class test_reg_page(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()


    def setUp(self):
        RegPage(self.browser).open()


    def testRegSuccess(self):
        page = RegPage(self.browser)


        reg_data = {
            'first name' : 'semen',
            'last name' : 'sosnitski',
            'email' : 'semensosnitski{}@gmail.com'.format(randint(0, 10)),
            'password' : 'abrakadabra',
            'confirm password' : 'abrakadabra'

        }

        for key, value in reg_data.items():
            page.find_element(key).send_keys(value)
        page.find_element('button').click()