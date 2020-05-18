import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class AddValues(unittest.TestCase):
    def test_adding(self):
        self.driver = webdriver.Chrome(executable_path="D:/NIDHI PANCHAL/PyTest/Drivers/chromedriver.exe")
        self.driver.get("https://www.seleniumeasy.com/test/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        obj = self.driver.find_element_by_xpath("// a[ @ title = 'Close']").click()
        self.driver.implicitly_wait(10)
        obj = self.driver.find_element_by_xpath("(//a[@class='dropdown-toggle'])[1]").click()
        self.driver.implicitly_wait(10)
        obj = self.driver.find_element_by_xpath("(//a[contains(text(),'Simple Form Demo')])[1]").click()
        self.driver.implicitly_wait(10)
        self.driver.execute_script("window.scrollTo(0, 1000);")
        obj = self.driver.find_element_by_xpath("// input[ @ id = 'sum1']").send_keys("10")
        obj = self.driver.find_element_by_xpath("// input[ @ id = 'sum2']").send_keys("20")
        obj = self.driver.find_element_by_xpath("// button[contains(text(), 'Get Total')]").click()
        self.driver.implicitly_wait(90)
        element = self.driver.find_element_by_xpath("// span[ @ id = 'displayvalue']").text
        assert element == '30'
        print("Result Matching!")
        self.driver.close()
