# coding=utf-8
import unittest
import time
import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os

# 这个是优化版执行所有用例并发送报告，分四个步骤
# 第一步加载用例
# 第二步执行用例
# 第三步获取最新测试报告
# 第四步发送邮箱 （这一步不想执行的话，可以注释掉最后面那个函数就行）

# 当前脚本所在文件真实路径
cur_path = os.path.dirname(os.path.realpath(__file__))#F:\PythonScripts\structure_exersise

def add_case(caseName="test_case", rule="test*.py"):
    '''第一步：加载所有的测试用例'''
    case_path = os.path.join(cur_path, caseName)  # 用例文件夹
    # 如果不存在这个case文件夹，就自动创建一个
    if not os.path.exists(case_path):os.mkdir(case_path)
    print("test case path:%s"%case_path)
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path,
                                                  pattern=rule,
                                                  top_level_dir=None)
    print(discover)
    return discover


def run_case(all_case, reportName="report"):
    '''第二步：执行所有的用例, 并把结果写入HTML测试报告'''
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = os.path.join(cur_path, reportName)  # 用例文件夹
    # 如果不存在这个report文件夹，就自动创建一个
    if not os.path.exists(report_path):os.mkdir(report_path)
    report_abspath = os.path.join(report_path, now+"result.html")
    print("report path:%s"%report_abspath)
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：',
                                           retry=0)#是否需要重复跑一次用例

    # 调用add_case函数返回值
    runner.run(all_case)
    fp.close()

def get_report_file(report_path):
    '''第三步：获取最新的测试报告'''
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    print (u'最新测试生成的报告： '+lists[-1])
    # 找到最新生成的报告文件
    report_file = os.path.join(report_path, lists[-1])
    return report_file

def send_mail(sender, psw, receiver, smtpserver, report_file, port):
    '''第四步：发送最新的测试报告内容'''
    with open(report_file, "rb") as f:
        mail_body = f.read()
    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = u"自动化测试报告"
    msg["from"] = sender
    msg["to"] = psw
    msg.attach(body)
    # 添加附件
    att = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename= "report.html"'
    msg.attach(att)


    try:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
    except:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver, port)

    # 用户名密码
    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('test report email has send out !')


if __name__ == "__main__":
    all_case = add_case()   # 1加载用例
    # 生成测试报告的路径
    run_case(all_case)        # 2执行用例
    # 获取最新的测试报告文件
    report_path = os.path.join(cur_path, "report")  # 用例文件夹
    report_file = get_report_file(report_path)  # 3获取最新的测试报告

    #邮箱配置
    from structure_exersise.config import ReadConfig
    sender=ReadConfig.sender
    psw=ReadConfig.psw
    smtp_server=ReadConfig.smtp_server
    port=ReadConfig.port
    receiver=ReadConfig.receiver
    send_mail(sender,psw,receiver,smtp_server,report_file,port)##4.发送报告





'''

3.导入模块的部分函数或类
from time import  *
--import*是导入全部功能

4.导入自己写的模块
--同文件夹，直接import 模块名
--跨文件夹，from 文件夹.文件夹.模块 import 类（或函数）
--注意文件夹内必需要有__init__.py文件

##########################定时器
import os
import time
while 1:
    now_time=time.strptime("%H:%M")
    if now_time=="23:00" or now_time=="10:00":
        #打开待执行的脚本（相当于dos里执行cd）
        os.chdir("F:\PythonScripts\structure_exersise")
        ##运行脚本
        os.system("python run_main.py")
        print("运行完成退出！")
        break
    else:
        time.sleep(30)
        print(now_time)
 '''
