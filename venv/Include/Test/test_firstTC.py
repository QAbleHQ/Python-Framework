import pytest
from Include.config.General.test_selenium import TestSelenium

@pytest.mark.usefixtures("setup")
class FirstTest:
    def test_TCFrist(self):
        objSelenium = TestSelenium()
        objSelenium.test_OpenURL("http://seleniumeasy.com/test")
        ProBars= objSelenium.test_findElementByXpath("//li/a[contains(text(), 'Progress Bars')]")
        ProBars.click()