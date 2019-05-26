#coding:utf-8
#这里我写一个截图函数，有时用例失败了，就用这个截图
import os
import time
from driver.driver1 import browser
def insert_img(driver,file_name):
    base_path=os.path.dirname(os.path.realpath(__file__))
    print(base_path)
    base_path=base_path.split("\\function")[0]
    print(base_path)
    base_path=base_path+"\\report\\img"
    print(base_path)
    driver.get_screenshot_as_file(base_path+"\\"+file_name)
if __name__=="__main__":
    driver=browser()
    driver.get("https://www.baidu.com")
    insert_img(driver,"a.png")
    driver.find_element_by_link_text(u"登录").click()
    time.sleep(2)
    driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
    driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("15179062604")
    driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys("Z5201314")
    driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
    driver.close()