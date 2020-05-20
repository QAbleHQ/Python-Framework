import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import re


class multiSelectDropdown(unittest.TestCase):
    def test_Multidropdown(self):
        self.driver = webdriver.Chrome(executable_path="D:/NIDHI PANCHAL/PyTest/Drivers/chromedriver.exe")
        self.driver.get("https://www.seleniumeasy.com/test/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        obj = self.driver.find_element_by_xpath("// a[ @ title = 'Close']").click()
        self.driver.implicitly_wait(20)

        src = self.driver.find_element_by_xpath("//a[contains(text(),'Selenium Easy')]")
        if src.is_displayed():
            print('Home page is displayed!!')

        obj = self.driver.find_element_by_xpath("(//a[@class='dropdown-toggle'])[1]").click()
        obj = self.driver.find_element_by_xpath("(//a[contains(text(),'Select Dropdown List')])[1]").click()
        self.driver.execute_script("window.scrollTo(0, 1000);")
        sel = self.driver.find_element_by_xpath("//option[@value='California']")
        sel1 = self.driver.find_element_by_xpath("//option[@value='New Jersey']")
        sel2 = self.driver.find_element_by_xpath("//option[@value='Pennsylvania']")
        ActionChains(self.driver).key_down(Keys.CONTROL).click(sel).key_up(Keys.CONTROL).perform()
        ActionChains(self.driver).key_down(Keys.CONTROL).click(sel1).key_up(Keys.CONTROL).perform()
        ActionChains(self.driver).key_down(Keys.CONTROL).click(sel2).key_up(Keys.CONTROL).perform()
        obj = self.driver.find_element_by_xpath("// button[contains(text(), 'Get All Selected')]").click()
        x = self.driver.find_element_by_xpath("// p[ @class ='getall-selected']").text
        print('Output: \n' + x)
        if x.split('Options selected are : ')[-1] == "California,New Jersey,Pennsylvania":
            print('Selected option and output are equal!')
        self.driver.close()
