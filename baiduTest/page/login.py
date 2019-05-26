#coding:utf-8
from common.base import Page
from selenium.webdriver.common.by import By
import time
class Login(Page):
    #这里是登陆页面的一些定位信息
    # denglu_loc=(By.LINK_TEXT,"登录") #登陆链接,link_text定位
    denglu_loc = (By.NAME, "tj_login") #登陆链接，name定位，这里写了两种定位方法，element与elements

    userdenglu_loc=(By.ID,"TANGRAM__PSP_10__footerULoginBtn") #使用用户名密码登陆按钮
    username_loc=(By.ID,"TANGRAM__PSP_10__userName") #用户名输入框
    password_loc=(By.ID,"TANGRAM__PSP_10__password") #密码输入框
    button_loc=(By.ID,"TANGRAM__PSP_10__submit") #登陆按钮
    error_loc=(By.ID,"TANGRAM__PSP_10__error") #提示错误信息定位


    #点击登陆链接
    def click_denglu(self):
        self.find_elements(self.denglu_loc)[1].click()
    #点击使用用户名，密码登陆
    def click_user(self):
        self.find_element(self.userdenglu_loc).click()
    #输入用户名
    def send_useranme(self,username):
        self.find_element(self.username_loc).send_keys(username)
    #输入密码
    def send_password(self,password):
        self.find_element(self.password_loc).send_keys(password)
    #点击另一个登陆按钮，和上面的登陆按钮不一样哦
    def click_submit(self):
        self.find_element(self.button_loc).click()

    #登陆流程
    def login_flow(self,username,password):
        self.click_denglu() #点击登陆链接，进入到登陆页面
        time.sleep(3)
        self.click_user() #点击使用用户名密码登陆
        time.sleep(2)
        self.send_useranme(username) #输入用户名
        time.sleep(2)
        self.send_password(password) #输入密码
        time.sleep(2)
        self.click_submit() #点击登陆
        time.sleep(3)

    #用于断言，判断预期结果与实际结果是否一致
    def error(self):
        return self.find_element(self.error_loc).text
        #有以下3种错误提示
        #请您输入密码
        #请您输入手机/邮箱/用户名
        #帐号或密码错误，请重新输入或者找回密码