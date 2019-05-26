#coding:utf-8
from selenium import webdriver
from baseView import base
from common import myTest
from webTest.page import loginPage

class Login(myTest.MyUnittest):
    def testcase_001(self):
        login=loginPage.LoginPages(self.driver)
        login.click_login()
    def testcase_002(self):
        login=loginPage.LoginPages(self.driver)
        login.click_login()

