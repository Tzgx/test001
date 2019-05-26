#coding:utf-8
from selenium import webdriver
import unittest

class Mytest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__=="__main__":
    unittest.main()