import pytest
from selenium import webdriver


class TestSelenium:
    def test_OpenURL(self, Url):
        self.driver.get(Url)

    def test_findElementByXpath(self, Xpath):
        element = self.self.driver.find_element_by_xpath(Xpath)
        return element