#coding:utf-8
from selenium import webdriver
import unittest
from driver.driver1 import browser

class MyUnittest(unittest.TestCase):
    #前置
    def setUp(self):
        self.driver=browser()
        self.driver.get("https://www.baidu.com")
        self.driver.maximize_window()

    #后置
    def tearDown(self):
        self.driver.close()