#coding:utf-8
from baseView import base
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPages(base.Base):
    loc_dneglu=(By.LINK_TEXT,"登录")

    def click_login(self):
        self.driver.find_element(self.loc_dneglu).click()

if __name__=="__mian__":
    driver=webdriver.Chrome()
    driver.get("https://www.baidu.com")
    login=LoginPage(driver)
    login.click_login()