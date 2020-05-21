import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import re


class inputForm(unittest.TestCase):
    def test_Form(self):
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
        obj = self.driver.find_element_by_xpath("(//a[contains(text(),'Input Form Submit')])[1]").click()
        obj = self.driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys('Nidhi')
        obj = self.driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys('Panchal')
        obj = self.driver.find_element_by_xpath("//input[@placeholder='E-Mail Address']").send_keys('nidhi_demo@mailinator.com')
        obj = self.driver.find_element_by_xpath("//input[@placeholder='(845)555-1212']").send_keys('7487030648')
        obj = self.driver.find_element_by_xpath("//input[@placeholder='Address']").send_keys('7487030648')
        obj = self.driver.find_element_by_xpath("// input[ @ placeholder = 'city']").send_keys('Ahmadabad')
        obj = self.driver.find_element_by_xpath("//input[@placeholder='Zip Code']").send_keys('380005')
        obj = self.driver.find_element_by_xpath("// input[ @ placeholder = 'Website or domain name']").send_keys('QAble')
        obj = self.driver.find_element_by_xpath("//input[@value='yes']").click()
        obj = self.driver.find_element_by_xpath("// textarea[ @ placeholder = 'Project Description']").send_keys('Nothing Much')
        obj = self.driver.find_element_by_xpath("//button[@type='submit']").click()

        # self.driver.execute_script("window.scrollTo(0, 1000);")
        # obj = self.driver.find_element_by_xpath("// button[contains(text(), 'Get All Selected')]").click()
        # x = self.driver.find_element_by_xpath("// p[ @class ='getall-selected']").text
        # print('Output: \n' + x)
        # if x.split('Options selected are : ')[-1] == "California,New Jersey,Pennsylvania":
        #     print('Selected option and output are equal!')
        self.driver.close()
