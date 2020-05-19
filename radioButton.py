import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import re


class radioButtonDemo(unittest.TestCase):
    def test_radio(self):
        self.driver = webdriver.Chrome(executable_path="D:/NIDHI PANCHAL/PyTest/Drivers/chromedriver.exe")
        self.driver.get("https://www.seleniumeasy.com/test/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        obj = self.driver.find_element_by_xpath("// a[ @ title = 'Close']").click()
        self.driver.implicitly_wait(20)

        src = self.driver.find_element_by_xpath("//a[contains(text(),'Selenium Easy')]")
        if src.is_displayed():
            print('Home page is displayed!!')
        #print(type(src))

        obj = self.driver.find_element_by_xpath("(//a[@class='dropdown-toggle'])[1]").click()
        self.driver.implicitly_wait(50)
        obj = self.driver.find_element_by_xpath("(//a[contains(text(),'Radio Buttons Demo')])[1]").click()
        self.driver.implicitly_wait(60)
        obj = self.driver.find_element_by_xpath("(//input[@value='Male'])[1]").click()
        self.driver.implicitly_wait(60)
        obj = self.driver.find_element_by_xpath("// button[contains(text(), 'Get Checked value')]").click()
        self.driver.implicitly_wait(150)
        src = self.driver.find_element_by_xpath("(//input[@value='Male'])[1]")
        assert(src.is_selected())
        print('Male Radiobutton is selected!')

        obj = self.driver.find_element_by_xpath("(//input[@value='Female'])[1]").click()
        self.driver.implicitly_wait(60)
        obj = self.driver.find_element_by_xpath("// button[contains(text(), 'Get Checked value')]").click()
        self.driver.implicitly_wait(150)
        src1 = self.driver.find_element_by_xpath("(//input[@value='Female'])[1]")
        if src1.is_selected():
            print('Female Radiobutton is selected!')
        else:
            print('Female Radiobutton is not selected!')
        self.driver.close()
