#coding:utf-8
#这里是二次封装，把定位方法简单化
from selenium import webdriver
import unittest
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.ui import WebDriverWait

class Page(object):
    def __init__(self,driver):
        self.driver=driver

    #定位元素
    def find_element(self,loc):
        element=WebDriverWait(self.driver,10).until(EC.presence_of_element_located(loc))
        return element

    def find_elements(self,loc):
        elements=WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located(loc))
        return elements
