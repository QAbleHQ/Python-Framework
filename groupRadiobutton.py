import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import re


class groupradioButtonDemo(unittest.TestCase):
    def test_groupradio(self):
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
        self.driver.execute_script("window.scrollTo(0, 1000);")
        obj = self.driver.find_element_by_xpath("(//input[@value='Male'])[2]").click()
        obj = self.driver.find_element_by_xpath("// input[ @ value = '0 - 5']").click()
        obj = self.driver.find_element_by_xpath("// button[contains(text(), 'Get values')]").click()
        self.driver.implicitly_wait(150)
        src = self.driver.find_element_by_xpath("//p[@class='groupradiobutton']").text
        print(src)

        obj = self.driver.find_element_by_xpath("(//input[@value='Male'])[2]").click()
        obj = self.driver.find_element_by_xpath("// input[ @ value = '5 - 15']").click()
        obj = self.driver.find_element_by_xpath("// button[contains(text(), 'Get values')]").click()
        self.driver.implicitly_wait(150)
        src = self.driver.find_element_by_xpath("//p[@class='groupradiobutton']").text
        print(src)

        obj = self.driver.find_element_by_xpath("(//input[@value='Male'])[2]").click()
        obj = self.driver.find_element_by_xpath("// input[ @ value = '15 - 50']").click()
        obj = self.driver.find_element_by_xpath("// button[contains(text(), 'Get values')]").click()
        self.driver.implicitly_wait(150)
        src = self.driver.find_element_by_xpath("//p[@class='groupradiobutton']").text
        print(src)

        obj = self.driver.find_element_by_xpath("(//input[@value='Female'])[2]").click()
        obj = self.driver.find_element_by_xpath("// input[ @ value = '0 - 5']").click()
        obj = self.driver.find_element_by_xpath("// button[contains(text(), 'Get values')]").click()
        self.driver.implicitly_wait(150)
        src = self.driver.find_element_by_xpath("//p[@class='groupradiobutton']").text
        print('\n\n')
        print(src)

        obj = self.driver.find_element_by_xpath("(//input[@value='Female'])[2]").click()
        obj = self.driver.find_element_by_xpath("// input[ @ value = '5 - 15']").click()
        obj = self.driver.find_element_by_xpath("// button[contains(text(), 'Get values')]").click()
        self.driver.implicitly_wait(150)
        src = self.driver.find_element_by_xpath("//p[@class='groupradiobutton']").text
        print(src)

        obj = self.driver.find_element_by_xpath("(//input[@value='Female'])[2]").click()
        obj = self.driver.find_element_by_xpath("// input[ @ value = '15 - 50']").click()
        obj = self.driver.find_element_by_xpath("// button[contains(text(), 'Get values')]").click()
        self.driver.implicitly_wait(150)
        src = self.driver.find_element_by_xpath("//p[@class='groupradiobutton']").text
        print(src)
        self.driver.close()
