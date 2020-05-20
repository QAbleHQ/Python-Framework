import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import re


class singleDropdown(unittest.TestCase):
    def test_dropdown(self):
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
        select = Select(self.driver.find_element_by_id('select-demo'))
        weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        for day in weekdays:
            select.select_by_visible_text(day)
            x = self.driver.find_element_by_xpath("//option[@value='" + day + "']").text
            print('Output: ' + x)
            if x.split('Day selected :- ')[-1] == day:
                print('Selected day is', day)
            else:
                print('Selected day and output are not equal!')
        # length=len(x)
        # if x.find('Wednesday') == -1/!= -1:       Else is not necessary while write !=-1
        #     print('Wednesday not found')
        # else:
        #     print("Wednesday Found")
        self.driver.close()
