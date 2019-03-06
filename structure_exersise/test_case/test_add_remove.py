from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains#操作鼠标事件
from selenium.webdriver.support.select import Select
import time
import unittest

from structure_exersise.data.common_function import Login,Is_Alert_Exist
class Add_Goods(unittest.TestCase):
    '''Add_Goods类，含新增商品及商品的删除'''
    @classmethod
    def setUpClass(cls):##每个class里只执行一次,setUpClass默认传参cls
        profile_directory="C:\\Users\\phyl\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\1gf7zpsd.default"#配置文件地址,r意思是转意，或者两个反斜杠代替
        profile=webdriver.FirefoxProfile(profile_directory)#加载配置
        cls.driver=webdriver.Firefox(profile)#启动浏览器配置
        cls.driver.get("http://39.104.14.232/ecshop/wwwroot/admin/index.php")

        try:##直接调用Login函数或者流水账登陆
            Login(cls.driver,"admin","fengliying123456")
            '''
            cls.driver.find_element_by_name("username").send_keys("admin")
            cls.driver.find_element_by_name("password").send_keys("fengliying123456")
            cls.driver.find_element_by_class_name("button2").click()
            '''
        except :##未清cookie时直接刷新页面进入
            cls.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.delete_all_cookies()#清空cookies
        cls.driver.quit()


    def setUp(self):
        self.driver.switch_to.frame("menu-frame")#切换iframe到商品列表所在frame
        self.driver.find_element_by_link_text("商品管理").click()##进入商品管理页面
    def tearDown(self):
        self.driver.switch_to_default_content()


    # @unittest.skip("跳过原因")###无条件跳过用例1
    #@unittest.skipIf(1>2,"跳过原因为假不跳过，为真时才能跳过")
    # @unittest.skipUnless(1,"1真不跳过，否则跳过")
    def test_001(self):
        '''添加新商品用例'''
        __doc__
        self.driver.find_element_by_link_text("添加新商品").click()
        self.driver.switch_to_default_content()
        ####切入到添加商品时的frame中
        self.driver.switch_to.frame("main-frame")
        self.driver.implicitly_wait(3)

        ##########商品名称及货号
        time.sleep(2)
        # goods_name=['咸鱼','小虾','河虾','花蛤','清江鱼','湄公鱼','草鱼','']
        self.driver.find_element_by_name("goods_name").send_keys("咸鱼5")
        self.driver.find_element_by_name("goods_sn").send_keys("咸鱼005")
        a=self.driver.find_element_by_name("goods_sn").get_attribute("value")
        print("商品名称%s"%a)
        self.assertEquals("咸鱼005",a)
         ###############选择商品分类

        # self.driver.find_element_by_id("cat_name").clear()
        time.sleep(4)
        self.driver.find_element_by_id("cat_name").click()
        self.driver.implicitly_wait(3)
        ##需操作滚动条至可见
        js="var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)

        self.driver.implicitly_wait(3)
        self.driver.find_element_by_xpath("//*[text()='seafood']").click()
        time.sleep(2)

        ###############二级关联项海鲜
        # Select(self.driver.find_element_by_name("other_cat[]")).select_by_index(2)
        Select(self.driver.find_element_by_xpath(".//*[@name='other_cat[]']")).select_by_value("452")
        time.sleep(1)
        print(self.driver.find_element_by_id("cat_name").get_attribute("value"))
        ##############商品品牌选择
        time.sleep(1)
        self.driver.find_element_by_id("brand_search").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("Dior").click()
        ############选择供货商
        Select(self.driver.find_element_by_id("suppliers_id")).select_by_value("2")

        ###########本店售价
        self.driver.find_element_by_name("shop_price").clear()
        time.sleep(1)
        self.driver.find_element_by_name("shop_price").send_keys("10.8")
        ###########手机专享价
        time.sleep(2)
        self.driver.find_element_by_name("exclusive").clear()
        time.sleep(2)
        self.driver.find_element_by_name("exclusive").send_keys("9.7")

        #########普通会员
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='rank_12']").clear()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='rank_12']").send_keys("10.3")

        #########铜牌会员
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='rank_13']").clear()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='rank_13']").send_keys("10.1")
        #########银牌会员
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='rank_14']").clear()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='rank_14']").send_keys("9.9")
        #########金牌会员
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='rank_15']").clear()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='rank_15']").send_keys("9.7")
        #########钻石会员
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='rank_16']").clear()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='rank_16']").send_keys("9.3")
        #########王者会员
        self.driver.find_element_by_xpath("//*[@id='rank_17']").clear()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='rank_17']").send_keys("8.9")

        ##########商品优惠价格
        self.driver.find_element_by_name("volume_number[]").clear()
        self.driver.find_element_by_name("volume_number[]").send_keys("20")
        time.sleep(1)
        self.driver.find_element_by_name("volume_price[]").clear()
        self.driver.find_element_by_name("volume_price[]").send_keys("8.6")
        ##########市场售价
        self.driver.find_element_by_name("market_price").clear()
        self.driver.find_element_by_name("market_price").send_keys("8.7")
        ############赠送消费积分数
        self.driver.find_element_by_name("give_integral").clear()
        self.driver.find_element_by_name("give_integral").send_keys("4")
        ###########赠送等级积分
        self.driver.find_element_by_name("rank_integral").clear()
        self.driver.find_element_by_name("rank_integral").send_keys("2")
        #############促销价
        s=self.driver.find_elements_by_id("is_promote")
        for i in s:
            if i.is_selected():
                pass
            else:
                i.click()
        time.sleep(1)

        self.driver.find_element_by_xpath("//*[@id='promote_1']").send_keys("7.8")
        ##################促销日期需要查js

        #######限购数量，默认，限购日期默认
        ############分成金额
        self.driver.find_element_by_id("promote_1").clear()
        time.sleep(1)
        self.driver.find_element_by_id("promote_1").send_keys("0.3")

        ##############上传商品图片
        self.driver.find_element_by_name("goods_img").send_keys(r"C:\Users\phyl\Pictures\Saved Pictures\\11.png")
        time.sleep(3)
        img=self.driver.find_element_by_name("goods_img").get_attribute("value")
        print("图片上传的是%s"%img)
        handle=self.driver.current_window_handle
        print("当前页面的hanld值是%s"%handle)
        #################
        self.driver.find_element_by_id("goods_info_submit").click()
        time.sleep(1)

    @unittest.skipIf(1>2,"跳过原因为假不跳过，为真时才能跳过")
    def test_02(self):
        '''搜索已添加商品，并将其删除'''
       ###1、购物网站，完成一个删除商品和查询的case
        self.driver.find_element_by_link_text("商品列表").click()
        self.driver.switch_to_default_content()
        ####切入到商品列表的frame中
        self.driver.switch_to.frame("main-frame")
        self.driver.implicitly_wait(3)
        ###############################上架状态判断################

        ##############################关键字搜索#################
        self.driver.find_element_by_xpath("//*[@name='keyword']").send_keys("咸鱼5")
        self.driver.find_element_by_xpath("//input[@type='submit' and @class='button']").click()
        self.driver.implicitly_wait(2)
        try:
             self.driver.find_element_by_xpath("/html/body/form/div[1]/table[1]/tbody/tr[3]/td[13]/a[4]").click()
             self.driver.implicitly_wait(10)
             Is_Alert_Exist(self.driver)
             '''
             alert=self.driver.switch_to_alert()
             print("处理回收站弹框：%s"%alert.text)
             time.sleep(4)
             alert.accept()# alert.dismiss()
             '''

        except Exception as msg:
            print("异常原因%s"%msg)
            ###########图片名称加上时间戳#######
            self.driver.implicitly_wait(3)
            now_time=time.strftime("%Y%M%D.%H.%M.%S")
            t=self.driver.get_screenshot_as_file("msg+%s.png"%now_time)
            self.driver.implicitly_wait(3)
            print("截图结果：%s"%t)
'''
    def test_03(self):
        ###检查商品列表中是否已经有此商品
          print("test_03暂时先pass")
'''


if __name__ == "__main__":
        unittest.main()
