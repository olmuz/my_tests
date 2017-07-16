from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement:
    def __init__(self, browser, locator):
        self.browser = browser
        self.locator = locator

    @property
    def element(self):
        return self.browser.find_element_by_xpath(self.locator)

    @property
    def is_visible(self):
        try:
            WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located(
                    (By.XPATH, self.locator)
                )
            )
        except TimeoutException:
            return False
        else:
            return True

    def click(self):
        self.element.click()

    def hover(self):
        ac = ActionChains(self.browser)
        ac.move_to_element(self.element)
        ac.perform()


