#coding:utf-8
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import HTMLTestRunner_cn
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import unittest
import time
import os

#查找测试报告目录，找到最新生成的测试报告文件
def new_report(test_report):
    lists = os.listdir(test_report)                                    #列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn:os.path.getmtime(test_report + "\\" + fn))#按创建文件的时间排序
    file_new = os.path.join(test_report,lists[-1])                     #获取最新的文件保存到file_new
    #os.path.join(os.getcwd(), 'data')就是获取当前目录，并组合成新目录
    print(file_new)
    return file_new


    # ==============定义发送邮件==========
def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    #======================================================================
    smtpserver = "smtp.163.com"  # 发件服务器
    port = 0  # 端口
    sender = "15179062604@163.com"  # 账号
    psw = "Z5201314"  # 密码
    receiver = ["3268281172@qq.com"]  # 单个接收人也可以是list
    #=======================================================================
    msg = MIMEMultipart()
    msg["from"] = sender  # 发件人
    # msg["to"] = ";".join(receiver)# 多个收件人list转str
    msg['to'] = "3268281172@qq.com"
    msg["subject"] = "嘿嘿测试报告"  # 主题

    # 正文=============================================================================
    body = MIMEText(mail_body, "html", "utf-8")
    msg.attach(body)

    # 附件，即测试报告
    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="test_report.html"'
    msg.attach(att)


    # ----------3.发送邮件------
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)  # 连服务器
        smtp.login(sender, psw)
    except:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
        smtp.login(sender, psw)  # 登录
    smtp.sendmail(sender, receiver, msg.as_string())  # 发送
    smtp.quit()  # 关闭




if __name__=="__main__":
    now=time.strftime("%Y-%m-%d_%H_%M_%S")#格式化时间，输出的时间格式如：2019-03-27_00_12_13
    print("现在的时间是：",now)
    case_path=os.path.dirname(os.path.realpath(__file__))
    print(case_path) #打印出用例所在的路径
    case=case_path+"\\test_case"
    report_path=case_path+"\\report\\"
    print(report_path) #打印报告要存放的路径
    file_name=report_path+now+"_report.html" #报告的名称，以运行时间作为名称 如：2019-03-27_00_12_13_report.html

    fp=open(file_name,"wb")
    discover=unittest.defaultTestLoader.discover(case,pattern="test*.py",top_level_dir=None)
    runner=HTMLTestRunner_cn.HTMLTestRunner(fp,title="嘿嘿，这是测试报告", description="自动化测试",verbosity=2)
    runner.run(discover)
    fp.close() #关闭报告，意思是前面生成了测试报告，前面是open,生成完后，这里需要把文件关闭close掉

    new_report = new_report(report_path)#调用上面的send_mail类进行邮件发送
    send_mail(new_report)  # 把测试报告以邮件形式发送