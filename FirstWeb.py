
from sys import executable
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class FirstWeb(unittest.TestCase):
   def test_setup(self):
       self.driver = webdriver.Chrome(executable_path="D:/NIDHI PANCHAL/PyTest/Drivers/chromedriver.exe")
       self.driver.get("https://www.google.com/")
       self.driver.maximize_window()
       que = self.driver.find_element_by_xpath("//input[@name='q']")
       que.send_keys("Automation testing tool")
       que.send_keys(Keys.RETURN)
       self.driver.close()



