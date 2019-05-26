#coding=utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC


class Base():
    def __init__(self,driver):
        self.driver=driver

    def find_element(self,loc):
        return WebDriverWait(self.driver,10).until(EC.presence_of_element_located(loc))

    def find_elements(self,loc):
        try:
            ele=WebDriverWait(self.driver,10).until(lambda x:x.find_elements(loc))
        except:
            print("wei")
        else:
            ele.click()

    def js(self,js1):
        self.driver.excute_scripts(js1)
