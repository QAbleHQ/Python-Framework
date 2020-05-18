import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class CheckboxDemo(unittest.TestCase):
    def test_check(self):
        self.driver = webdriver.Chrome(executable_path="D:/NIDHI PANCHAL/PyTest/Drivers/chromedriver.exe")
        self.driver.get("https://www.seleniumeasy.com/test/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        obj = self.driver.find_element_by_xpath("// a[ @ title = 'Close']").click()
        self.driver.implicitly_wait(20)
        obj = self.driver.find_element_by_xpath("(//a[@class='dropdown-toggle'])[1]").click()
        self.driver.implicitly_wait(50)
        obj = self.driver.find_element_by_xpath("(//a[contains(text(),'Checkbox Demo')])[1]").click()
        self.driver.implicitly_wait(60)
        obj = self.driver.find_element_by_xpath("// input[ @ id = 'isAgeSelected']").click()
        self.driver.implicitly_wait(80)
        element = self.driver.find_element_by_xpath("// div[ @ id = 'txtAge']").text
        assert element == 'Success - Check box is checked'
        print("Checkbox is selected")
        self.driver.close()
