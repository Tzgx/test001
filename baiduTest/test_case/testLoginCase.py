#coding:utf-8
from page.login import Login
from common import myTest,excel1
import unittest
import time,os
from selenium import webdriver
from logs import log

# 测试数据
data_path = os.path.dirname(os.path.dirname(__file__))
data_path = data_path+"\\data\\data.xlsx"
print(data_path) #打印出测试数据存放的路径

sheetName = "Sheet1" #测试数据的第一张表sheet
data = excel1.ExcelUtil(data_path, sheetName)

testData = data.dict_data()
print(testData) #打印出data.excel中的数据

print(testData[2]["username"])#这是打印第三行的username数据,索引从0开始
print(testData[2]["password"])#这是打印第三行的password数据，索引从0开始

logg=log.Log()
logg.info("这是日志开始哦")

class LoginCase(myTest.MyUnittest):
    '''测试集合组'''
    def test001(self):
        """第一条测试用例"""
        logg.info("第一条用例开始执行")
        try:
            po=Login(self.driver)
            po.login_flow("","")#输入空的用户名和空的密码
            self.assertNotEqual(po.error(),"请您输入手机/邮箱/用户名")
        except Exception as e:
            print("打印错误信息：%s",e)

    def test002(self):
        """第二条测试用例，输入错误的用户名密码，并且数据来自的是excel表格"""
        #失败用例
        po=Login(self.driver)
        po.login_flow(testData[2]["username"],testData[2]["password"])
        print("用户名：",testData[2]["username"])
        print("密码：", testData[2]["password"])
        self.assertEqual(po.error(),"帐号或密码错误") #这是断言，因为实际提示信息是“账号或密码错误，或者找回密码”
        logg.info("这是日志结束哦")


    def test003(self):
        """第三条测试用例，输入正确的用户名密码"""
        try:
            po = Login(self.driver)
            po.login_flow("15179062604", "Z520314")
            self.assertNotEqual(po.error(), "登陆成功")
        except:
            print("登陆成功")


if __name__=="__main__":
     unittest.main()