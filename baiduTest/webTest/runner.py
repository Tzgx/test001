#coding=utf-8
from selenium import webdriver
import time
import os
import unittest
import HTMLTestRunner_cn

if __name__=="__main__":
    now=time.strftime("%Y-%m-%d_%H_%M_%S")
    print(now)
    path=os.path.dirname(os.path.realpath(__file__))
    print(path)
    case_path=os.path.join(path,"testcase")
    print(case_path)
    report_path=os.path.join(path,"report")
    print(report_path)
    fp=open(report_path,"wb")

    discover=unittest.defaultTestLoader.discover(case_path,pattern="*.py",top_level_dir=None)
    runner=HTMLTestRunner_cn.HTMLTestRunner(fp,title="",description="xxx",verbosity=2)
    runner.run(discover)

