from selenium import webdriver
driver=webdriver.Firefox()
import unittest


def Login(driver,name,password):
    '''登陆函数账号密码参数化'''
    driver.get("http://39.104.14.232/ecshop/wwwroot/admin/index.php")
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys(name)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_class_name("button2").click()




def Is_Alert_Exist(driver):
    '''弹窗出现后处理'''
    try:
        a=driver.switch_to.alert#切入弹窗
        t=a.text#如果没有alert会报异常
        a.accept()
        print("alert内容:%s"%t)
        return t
    except:
        print("没有捕捉到alert")
        return""
if __name__ == "__main__":
        unittest.main()
