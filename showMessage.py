import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class InputForms(unittest.TestCase):
    def test_Form(self):
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
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        obj = self.driver.find_element_by_xpath("// input[ @ placeholder = 'Please enter your Message']").send_keys(
            "Have a wonderful day")
        self.driver.implicitly_wait(20)
        obj = self.driver.find_element_by_xpath("//button[contains(text(),'Show Message')]").click()
        self.driver.implicitly_wait(40)
        element = self.driver.find_element_by_xpath("//span[@id='display']").text
        assert element == 'Have a wonderful day'
        print("Matching text successfully!")
        self.driver.close()
