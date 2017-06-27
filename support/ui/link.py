from selenium.webdriver import ActionChains


class Link():
    def __init__(self, browser, name):
        self.locator = '//a[text() ="{0}"]'.format(name)
        self.browser = browser

    @property
    def element(self):
        # return WebElements instance
        return self.browser.find_element_by_xpath(self.locator)

    def click(self):
        self.element.click()

    def hover(self):
        # ActionChains is used Drag&Drop and mouse hovering
        ac = ActionChains(self.browser)
        ac.move_to_element(self.element)
        ac.perform()

    def hover_and_click(self):
        ac = ActionChains(self.browser)
        ac.move_to_element(self.element)
        ac.click()
        ac.perform()