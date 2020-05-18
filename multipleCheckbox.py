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
        self.driver.execute_script("window.scrollTo(0, 1000);")
        obj = self.driver.find_element_by_xpath("//input[@id='check1']").click()
        self.driver.implicitly_wait(80)
        element = self.driver.find_element_by_xpath("(//input[@class='cb1-element'])[1]").is_selected()
        element = self.driver.find_element_by_xpath("(//input[@class='cb1-element'])[2]").is_selected()
        element = self.driver.find_element_by_xpath("(//input[@class='cb1-element'])[3]").is_selected()
        element = self.driver.find_element_by_xpath("(//input[@class='cb1-element'])[4]").is_selected()
        self.driver.implicitly_wait(80)
        print("All Checkbox is selected")
        self.driver.close()




