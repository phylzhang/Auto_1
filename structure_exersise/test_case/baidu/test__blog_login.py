import requests
import unittest
from structure_exersise.data.logger import Log
# 禁用安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
#####################3cookie添加绕过登陆，通过update方法直接更新cookie


class LOGIN(unittest.TestCase):
    log = Log()
    def login(self, username, psw, reme=True):
        url="https://passport.cnblogs.com/user/signin"
        header={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
            "Acccpt":"application/json, text/javascript, */*; q=0.01",
            "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
             "Connection":"close",
             "Content-Type":"application/json; charset=utf-8",
            "X-Requested-With": "XMLHttpRequest",
        }
        #s就是session,自动保存cookie信息
        s=requests.session()
        #先通过get方法获取部分cookie,走登陆页面的正常cookie
        r1=self.s.post(self.url,headers=self.header,verify=False)
        print(r1.cookies)

        # #添加登陆需要的两个cookie
        c=requests.cookies.RequestsCookieJar()###返回CookieJar的实例
        c.set('.CNBlogsCookie',
              "20B58B5179E744845DE9672A485F1EB176577B5CAC84EFAFCB2E2597B734C378126A04AD6600D3204AAB1BC8CAE39DA43BE319C38DDF4D324E878BC14D553059B584451CFE9867AD946AB61D90F7ECBAF940BE4D")
        c.set(".Cnblogs.AspNetCore.Cookies",
              "CfDJ8J0rgDI0eRtJkfTEZKR_e80tVPgdPhTOCmeoaRJgA7-S-n9TbAtxdxFUMX-5oA6xgTrhESHKKJDJ9YnQEn0zJPexRXo9PyjrIbOWa5Di4eu1ydM1TDtQhftumuPUEkXRAbGU_gcsdT6hwioK9v1sFRDE8xGoXlDQ5iHB6YM4h9bmuiAcF-vWzejRbvkVdgvzG5qG2Di3mMv15R89vab6wuQ1ZA6b3krxNLqFEpJsk1-3r5Lh6wR0BoxJcnTDTaQcfOd58j_PdD_sK9Pj8yaC9WauOW2nyETfHymVyJPEuwHh")
        c.set("domain","cnblogs.com")
        c.set("expiry",1543198500)###有效期
        self.s.cookies.update(c)
        '''三个参数：账号：username，密码：psw,记住登录：reme=True'''
        json_data = {"input1": username,
                "input2": psw,
                "remember": reme}

        res = requests.post(self.url, headers=self.header, json=json_data, verify=False)
        result1 = res.content  # 字节输出
        self.log.info("博客园登录结果：%s"%result1)
        return res.json()      # 返回json

    def test_login1(self):
        u'''测试登录：正确账号，正确密码'''
        self.log.info("------登录成功用例：start!---------")
        username = "这里是抓包后获取的博客园的加密账号",
        self.log.info("输入正确账号：%s"%username)
        psw = "这里是抓包后获取的博客园的加密密码",
        self.log.info("输入正确密码：%s"%psw )
        result = self.login(username, psw)
        self.log.info("获取测试结果：%s"%result)
        self.assertEqual(result["success"], True)
        self.log.info("------pass!---------")

    def test_login2(self):
        u'''测试登录：正确账号，错误密码'''
        self.log.info("------登录失败用例：start!---------")
        username = "这里是抓包后获取的博客园的加密账号",
        self.log.info("输入正确账号：%s"%username)
        psw = "xxx",
        self.log.info("输入错误密码：%s"%username)
        result = self.login(username, psw)
        self.log.info("获取测试结果：%s"%result)
        self.assertEqual(result["success"], False)
        self.log.info("------pass!---------")

if __name__=="__main__":
    unittest.main()



