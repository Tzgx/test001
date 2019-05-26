#coding:utf-8
from selenium import webdriver
#定义浏览器，使用谷歌浏览器运行测试用例
def browser():
    driver=webdriver.Chrome()
    # driver = webdriver.Firefox()
    return driver
