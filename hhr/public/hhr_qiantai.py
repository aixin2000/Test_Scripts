# -*- coding:utf-8 -*-
from selenium import webdriver
import unittest
from time import sleep
from logs.logger import Logger
import os
from tools.test_tools import Test_Tools
logger = Logger(logger="Buy Product").getlog()


image_path = os.path.abspath(os.path.join(os.getcwd(), "../..")) + '\\image\\1.jpg'
item = Test_Tools()
items1 = item.read_config()
executable = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/driver/chromedriver.exe'


class Qian_Tai(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=executable)
        logger.info('打开谷歌浏览器')
        self.driver.get(items1['test3'])
        logger.info('打开网址')
        self.driver.maximize_window()
        logger.info('浏览器最大化')
        # self.driver.find_element_by_class_name('close-img').click()
        # logger.info('关闭弹窗')
        self.driver.implicitly_wait(10)
        logger.info('等待10s')
        sleep(2)

    def tearDown(self):
        sleep(3)
        self.driver.find_element_by_xpath('//a[text() = "退出登录"]').click()
        logger.info('退出登录')
        self.driver.quit()


class WeiDian(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=executable)
        self.driver.get(items1['weidian'])
        self.driver.maximize_window()
        # self.driver.find_element_by_class_name('close-img').click()
        # logger.info('关闭弹窗')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_class_name('login_link').click()
        sleep(1)
        self.driver.find_elements_by_class_name('el-input__inner')[0].send_keys('18273675403')
        sleep(1)
        self.driver.find_elements_by_class_name('el-input__inner')[1].send_keys('aixin96177520000')
        sleep(1)
        self.driver.find_elements_by_class_name('el-input__inner')[2].send_keys('hhr123456')
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "登录"]').click()

    def tearDown(self):
        self.driver.find_element_by_class_name('exit_btn').click()
        sleep(3)
        self.driver.quit()


class ZhiKeLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=executable)
        logger.info('打开谷歌浏览器')
        self.driver.get(items1['test3'])
        logger.info('打开网址')
        self.driver.maximize_window()
        logger.info('浏览器最大化')
        # self.driver.find_element_by_class_name('close-img').click()
        # logger.info('关闭弹窗')
        self.driver.implicitly_wait(10)
        logger.info('等待10s')

        self.driver.find_element_by_xpath('//a[text() = "登录"]').click()
        self.driver.find_element_by_xpath('//*[@id="pane-login"]/form/div[1]/div/div/input').send_keys('15608449287')
        self.driver.find_element_by_xpath('//*[@id="pane-login"]/form/div[2]/div/div/input').send_keys(
            'hhr123456')
        self.driver.find_element_by_xpath('//*[@id="pane-login"]/form/div[3]/div/div/input').send_keys(
            'hhr123456')
        self.driver.find_element_by_xpath('//span[text() = "登录"]').click()

    def tearDown(self):
        sleep(1)
        self.driver.find_element_by_xpath('//a[@href = "/customer/exit.html"]').click()
        logger.info('退出登录')
        self.driver.quit()

    def select_park_service(self, price=0, endprice=0):
        self.driver.find_element_by_class_name('registrationWords').click()
        logger.info('点击注册类型')
        list1 = self.driver.window_handles
        self.driver.switch_to.window(list1[1])
        logger.info('切换窗口')
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[1]/div[8]/div[2]/div[8]/div[1]/input').send_keys(price)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[1]/div[8]/div[2]/div[8]/div[2]/input').send_keys(endprice)
        logger.info('输入价格范围')
        sleep(2)
        self.driver.find_element_by_class_name('price_btn').click()
        logger.info('点击确定')
        sleep(2)
        self.driver.find_element_by_class_name('card-tit1').click()
        logger.info('点击一个直客产品')
        list1 = self.driver.window_handles
        self.driver.switch_to.window(list1[2])
        logger.info('切换窗口')
        self.driver.find_element_by_xpath('//a[text()="立即购买"]').click()
        logger.info('点击立即购买')
        sleep(2)
        self.driver.find_element_by_id('dealTxt').click()
        logger.info('已阅读并同意《用户服务协议》')
        self.driver.find_element_by_class_name('indent-total-button').click()
        logger.info('点击生成订单')
        sleep(2)

    def select_enterprise_service(self, price=0, endprice=0):
        self.driver.find_element_by_id('nav_item_serviceMall').click()
        logger.info('点击企服商城')
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)
        logger.info('执行下滑操作')
        self.driver.find_element_by_xpath('//a[text() = "更多 >"]').click()
        logger.info('点击更多')
        list1 = self.driver.window_handles
        self.driver.switch_to.window(list1[1])
        logger.info('切换窗口')
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div[2]/div[2]/div[2]/section[1]/div[2]/ul/li[7]/input').send_keys(price)
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div[2]/div[2]/div[2]/section[1]/div[2]/ul/li[8]/input').send_keys(endprice)
        logger.info('输入价格范围')
        sleep(1)
        self.driver.find_element_by_class_name('certainBtn').click()
        logger.info('点击确定')
        sleep(2)
        self.driver.find_element_by_class_name('headline').click()
        logger.info('点击一个企服商城产品')
        list2 = self.driver.window_handles
        self.driver.switch_to.window(list2[2])
        logger.info('切换窗口')
        self.driver.find_element_by_class_name('btn1').click()
        logger.info('点击立即购买')
        sleep(3)
        self.driver.find_element_by_xpath('//button[text()="生成订单"]').click()
        logger.info('点击生成订单')
        sleep(2)

    def limited_company_submitting_information(self):
        """直客购买有限注册提交资料"""
        self.driver.find_element_by_class_name('registrationWords').click()
        logger.info('点击注册类型')
        sleep(1)
        list1 = self.driver.window_handles
        self.driver.switch_to.window(list1[1])
        logger.info('切换窗口')
        sleep(1)
        self.driver.find_element_by_xpath('//div[text() = "有限公司注册"]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[1]/div[8]/div[2]/div[8]/div[1]/input').send_keys(0)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[1]/div[8]/div[2]/div[8]/div[2]/input').send_keys(0)
        logger.info('输入价格范围')
        sleep(1)
        self.driver.find_element_by_class_name('price_btn').click()
        logger.info('点击确定')
        sleep(1)
        self.driver.find_element_by_class_name('card-tit1').click()
        logger.info('点击一个直客产品')
        sleep(1)
        list1 = self.driver.window_handles
        self.driver.switch_to.window(list1[2])
        logger.info('切换窗口')
        self.driver.find_element_by_xpath('//a[text()="立即购买"]').click()
        logger.info('点击立即购买')
        sleep(2)
        # list1 = self.driver.window_handles
        # self.driver.switch_to.window(list1[3])
        # logger.info('切换窗口')
        self.driver.find_element_by_id('dealTxt').click()
        logger.info('已阅读并同意《用户服务协议》')
        sleep(1)
        self.driver.find_element_by_class_name('indent-total-button').click()
        logger.info('点击生成订单')
        sleep(1)
        self.driver.find_element_by_class_name('indent-total-button').click()
        logger.info('点击立即支付')
        sleep(3)
        self.driver.find_element_by_xpath('//a[text() = "马上提交"]').click()
        logger.info('点击马上提交')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="mainContainer"]/section[9]/div/div[2]/div[5]/div/div[3]/span/span').click()
        logger.info('点击我已知晓')
        # list1 = self.driver.window_handles
        # self.driver.switch_to.window(list1[1])
        sleep(1)
        self.driver.find_elements_by_class_name('el-input__inner')[0].send_keys(200)
        logger.info('输入注册资金')
        sleep(1)
        self.driver.find_element_by_class_name('company-name').click()
        logger.info('点击行业名称')
        sleep(1)
        self.driver.find_element_by_xpath('//li[text() = "信息科技"]').click()
        logger.info('选择信息科技')
        sleep(1)
        for i in range(3):
            self.driver.find_element_by_class_name('assistant-btn').click()
            sleep(2)
            logger.info('点击起名助手')
            self.driver.find_element_by_xpath('//span[text() = "添加为备选名"]').click()
            sleep(1)
        self.driver.find_element_by_class_name('el-textarea__inner').clear()
        self.driver.find_element_by_class_name('el-textarea__inner').send_keys('经营范围')
        logger.info('输入经营范围')
        js = "var q=document.documentElement.scrollTop=500"
        self.driver.execute_script(js)
        sleep(2)
        logger.info('下拉滚动条')
        sleep(1)

        # 填写股东信息
        self.driver.find_element_by_xpath(
            '//*[@id="shareholder"]/div[1]/form/div[2]/div[2]/div[1]/div/div/div/input').send_keys('龚俊棋')
        logger.info('输入姓名')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="shareholder"]/div[1]/form/div[2]/div[2]/div[2]/div/div/div/input').send_keys('18873665375')
        logger.info('输入联系电话')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="shareholder"]/div[1]/form/div[2]/div[2]/div[3]/div[1]/div/div/input').send_keys(100)
        logger.info('输入出资比例')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="shareholder"]/div[1]/form/div[2]/div[2]/div[3]/div[2]/div/div/input').send_keys('4964694@qq.com')
        logger.info('输入qq邮箱')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="shareholder"]/div[1]/form/div[2]/div[3]/div[1]/div/div/div/input').send_keys('430702199610080514')
        logger.info('输入身份证号码')
        sleep(1)
        # self.driver.find_elements_by_class_name('el-range-input')[0].click()
        sleep(1)
        tran = self.driver.find_element_by_xpath('//*[@id="shareholder"]/div[1]/form/div[2]/div[3]/div['
                                                 '2]/div/div/div[1]/input')
        self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        tran.send_keys('2020-5-23')
        sleep(1)
        # tran1 = self.driver.find_elements_by_class_name('el-range-input')[1]
        # self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran1)
        # tran1.send_keys('2020-5-24')
        logger.info('输入有效期限')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="shareholder"]/div[1]/form/div[2]/div[3]/div[3]/div/div/div/input').click()
        self.driver.find_element_by_xpath(
            '//*[@id="shareholder"]/div[1]/form/div[2]/div[3]/div[3]/div/div/div/input').send_keys('上海市徐汇区锦辉大厦')
        logger.info('输入身份证地址')
        sleep(2)
        self.driver.find_elements_by_name('file')[0].send_keys(image_path)
        logger.info('上传股东身份证人像面')
        sleep(2)
        self.driver.find_elements_by_name('file')[1].send_keys(image_path)
        logger.info('上传身份证国徽面')
        sleep(2)
        # js = "var q=document.documentElement.scrollTop=500"
        # self.driver.execute_script(js)

        # 填写法人信息
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[1]/div[2]/div[2]/div[1]/div/div/div/input').send_keys('徐世伟')
        logger.info('输入法人姓名')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[1]/div[2]/div[2]/div[2]/div/div/div/input').send_keys('18601614687')
        logger.info('输入联系电话')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[1]/div[2]/div[2]/div[3]/div/div/div/input').send_keys(
            '49787864694@qq.com')
        logger.info('输入qq邮箱')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[1]/div[2]/div[3]/div[1]/div/div/div/input').send_keys(
            '622421199408156415')
        logger.info('输入身份证号码')
        sleep(1)
        tran = self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[1]/div[2]/div[3]/div[2]/div/div/div[1]/input')
        self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        tran.send_keys('2020-5-23')
        sleep(1)
        # tran1 = self.driver.find_element_by_xpath(
        #     '//*[@id="corporations"]/div[1]/form[1]/div[2]/div[3]/div[2]/div/div/div/input[2]')
        # self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        # tran1.send_keys('2020-5-24')
        logger.info('输入有效期限')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[3]/div[2]/div[3]/div[3]/div/div/div/input').click()
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[1]/div[2]/div[3]/div[3]/div/div/div/input').send_keys('上海市徐汇区锦辉大厦')
        logger.info('输入身份证地址')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[1]/div[2]/div[1]/div[3]/div/div/div[1]/div/input').send_keys(
            image_path)
        logger.info('上传法人身份证人像面')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[1]/div[2]/div[1]/div[3]/div/div/div[2]/div/input').send_keys(
            image_path)
        logger.info('上传身份证国徽面')

        # 监事信息
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[2]/div[2]/div[2]/div[1]/div/div/div[1]/input').send_keys('龚俊棋')
        logger.info('输入监事姓名')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[2]/div[2]/div[2]/div[2]/div/div/div/input').send_keys('18873665375')
        logger.info('输入联系电话')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[2]/div[2]/div[2]/div[3]/div/div/div/input').send_keys(
            '49787864694@qq.com')
        logger.info('输入qq邮箱')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[2]/div[2]/div[3]/div[1]/div/div/div/input').send_keys(
            '430702199610080514')
        logger.info('输入身份证号码')
        sleep(1)

        tran = self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[2]/div[2]/div[3]/div[2]/div/div/div[1]/input')
        self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        tran.send_keys('2020-5-23')
        sleep(1)
        # tran1 = self.driver.find_element_by_xpath(
        #     '//*[@id="corporations"]/div[1]/form[2]/div[2]/div[3]/div[2]/div/div/div/input[2]')
        # self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        # tran1.send_keys('2020-5-24')
        logger.info('输入有效期限')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[2]/div[2]/div[3]/div[3]/div/div/div/input').click()
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[2]/div[2]/div[3]/div[3]/div/div/div/input').send_keys('上海市徐汇区锦辉大厦')
        logger.info('输入身份证地址')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[2]/div[2]/div[1]/div[3]/div/div/div[1]/div/input').send_keys(
            image_path)
        logger.info('上传监事身份证人像面')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[2]/div[2]/div[1]/div[3]/div/div/div[2]/div/input').send_keys(
            image_path)
        logger.info('上传身份证国徽面')

        # 财务负责人信息
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[3]/div[2]/div[2]/div[1]/div/div/div/input').send_keys('刘刚')
        logger.info('输入财务负责人姓名')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[3]/div[2]/div[2]/div[2]/div/div/div/input').send_keys('15216746163')
        logger.info('输入联系电话')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[3]/div[2]/div[2]/div[3]/div/div/div/input').send_keys(
            '49787864694@qq.com')
        logger.info('输入qq邮箱')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[3]/div[2]/div[3]/div[1]/div/div/div/input').send_keys(
            '340822199607245516')
        logger.info('输入身份证号码')
        sleep(1)
        tran = self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[3]/div[2]/div[3]/div[2]/div/div/div[1]/input')
        self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        tran.send_keys('2020-5-23')
        sleep(1)
        # tran1 = self.driver.find_element_by_xpath(
        #     '//*[@id="corporations"]/div[1]/form[3]/div[2]/div[3]/div[2]/div/div/div/input[2]')
        # self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        # tran1.send_keys('2020-5-24')
        logger.info('输入有效期限')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[3]/div[2]/div[3]/div[3]/div/div/div/input').click()
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[3]/div[2]/div[3]/div[3]/div/div/div/input').send_keys('上海市徐汇区锦辉大厦3')
        logger.info('输入身份证地址')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[3]/div[2]/div[1]/div[3]/div/div/div[1]/div/input').send_keys(
            image_path)
        logger.info('上传财务负责人身份证人像面')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[3]/div[2]/div[1]/div[3]/div/div/div[2]/div/input').send_keys(
            image_path)
        logger.info('上传身份证国徽面')

        # 添加地址
        self.driver.find_element_by_xpath('//*[@id="address"]/div[1]/div[2]/button/span').click()
        logger.info('点击添加地址')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[1]/div/div/input').send_keys('aaa')
        logger.info('填写姓名')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[2]/div/div/input').send_keys(
            18273675403)
        logger.info('填写手机号码')
        sleep(1)
        logger.info('添加省')
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[3]/div/div[1]/div[1]/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "河北省"]').click()
        sleep(1)
        logger.info('添加市')
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[3]/div/div[2]/div[1]/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "石家庄市"]').click()
        sleep(1)
        logger.info('添加区')
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[3]/div/div[3]/div[1]/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "长安区"]').click()
        sleep(1)
        logger.info('填写具体地址')
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[4]/div/div/textarea').send_keys(
            '上海市徐汇区锦辉大厦')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[5]/div/label/span[1]/span').click()
        logger.info('设为默认地址')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[6]/div/button[1]/span').click()
        logger.info('点击确定')
        sleep(1)

        self.driver.find_element_by_xpath('//*[@id="address"]/div[2]/div[3]/form/div/div/div/div/div/input').send_keys(
            '上海市徐汇区')
        logger.info('填写联系地址')
        sleep(2)
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        logger.info('下拉滚动条')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="otherInfo"]/div[1]/div[2]/div/div/input').send_keys(image_path)
        logger.info('上传委托书')
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mainContainer"]/section[9]/div/div[2]/div[1]/button[2]').click()
        logger.info('点击保存并提交')
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mainContainer"]/section[9]/div/div[2]/div[4]/div/div[3]/span/span[1]').click()
        logger.info('点击我已知晓')
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "我已阅读并同意以上内容"]').click()
        logger.info('点击我已阅读并同意以上内容')

    def limited_partnership_submission(self):
        self.driver.find_element_by_class_name('registrationWords').click()
        logger.info('点击注册类型')
        sleep(1)
        list1 = self.driver.window_handles
        self.driver.switch_to.window(list1[1])
        logger.info('切换窗口')
        sleep(1)
        self.driver.find_element_by_xpath('//div[text() = "有限合伙注册"]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[1]/div[8]/div[2]/div[8]/div[1]/input').send_keys(0)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[1]/div[8]/div[2]/div[8]/div[2]/input').send_keys(0)
        logger.info('输入价格范围')
        sleep(1)
        self.driver.find_element_by_class_name('price_btn').click()
        logger.info('点击确定')
        sleep(1)
        self.driver.find_element_by_class_name('card-tit1').click()
        logger.info('点击一个直客产品')
        sleep(1)
        list1 = self.driver.window_handles
        self.driver.switch_to.window(list1[2])
        logger.info('切换窗口')
        self.driver.find_element_by_xpath('//a[text()="立即购买"]').click()
        logger.info('点击立即购买')
        sleep(2)
        # list1 = self.driver.window_handles
        # self.driver.switch_to.window(list1[3])
        # logger.info('切换窗口')
        self.driver.find_element_by_id('dealTxt').click()
        logger.info('已阅读并同意《用户服务协议》')
        sleep(1)
        self.driver.find_element_by_class_name('indent-total-button').click()
        logger.info('点击生成订单')
        sleep(1)
        self.driver.find_element_by_class_name('indent-total-button').click()
        logger.info('点击立即支付')
        sleep(3)
        self.driver.find_element_by_xpath('//a[text() = "马上提交"]').click()
        logger.info('点击马上提交')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="mainContainer"]/section[9]/div/div[2]/div[5]/div/div[3]/span/span').click()
        logger.info('点击我已知晓')
        # list1 = self.driver.window_handles
        # self.driver.switch_to.window(list1[1])
        # sleep(1)
        self.driver.find_elements_by_class_name('el-input__inner')[0].send_keys(200)
        logger.info('输入注册资金')
        sleep(1)
        self.driver.find_element_by_class_name('company-name').click()
        logger.info('点击行业名称')
        sleep(1)
        self.driver.find_element_by_xpath('//li[text() = "信息科技"]').click()
        logger.info('选择信息科技')
        sleep(1)
        for i in range(3):
            self.driver.find_element_by_class_name('assistant-btn').click()
            sleep(2)
            logger.info('点击起名助手')
            self.driver.find_element_by_xpath('//span[text() = "添加为备选名"]').click()
            sleep(1)
        self.driver.find_element_by_class_name('el-textarea__inner').clear()
        self.driver.find_element_by_class_name('el-textarea__inner').send_keys('经营范围')
        logger.info('输入经营范围')
        js = "var q=document.documentElement.scrollTop=500"
        self.driver.execute_script(js)
        sleep(2)
        logger.info('下拉滚动条')
        sleep(1)

        # 填写普通合伙人信息
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[1]/div/div[1]/form/div[2]/div[2]/div[1]/div/div/div/input').send_keys('龚俊棋')
        logger.info('输入普通合伙人姓名')
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[1]/div/div[1]/form/div[2]/div[2]/div[2]/div/div/div/input').send_keys(
            '18873665375')
        logger.info('输入联系电话')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[1]/div/div[1]/form/div[2]/div[2]/div[3]/div[1]/div/div/input').send_keys(50)
        logger.info('输入出资比例')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[1]/div/div[1]/form/div[2]/div[2]/div[3]/div[2]/div/div/input').send_keys(
            '4964694@qq.com')
        logger.info('输入qq邮箱')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[1]/div/div[1]/form/div[2]/div[3]/div[1]/div/div/div/input').send_keys(
            '430702199610080514')
        logger.info('输入身份证号码')
        sleep(1)
        tran = self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[1]/div/div[1]/form/div[2]/div[3]/div[2]/div/div/div[1]/input')
        self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        tran.send_keys('2020-5-23')
        sleep(1)
        logger.info('输入有效期限')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[1]/div/div[1]/form/div[2]/div[3]/div[3]/div/div/div/input').click()
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[1]/div/div[1]/form/div[2]/div[3]/div[3]/div/div/div/input').send_keys(
            '上海市徐汇区锦辉大厦')
        logger.info('输入身份证地址')
        sleep(3)
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[1]/div/div[1]/form/div[2]/div[1]/div[3]/div/div/div[1]/div/input').send_keys(
            image_path)
        logger.info('上传股东身份证人像面')
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[1]/div/div[1]/form/div[2]/div[1]/div[3]/div/div/div[2]/div/input').send_keys(
            image_path)
        logger.info('上传身份证国徽面')
        sleep(1)

        js = "var q=document.documentElement.scrollTop=500"
        self.driver.execute_script(js)
        sleep(1)

        # 填写有限合伙人信息
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[2]/div/div[1]/form/div[2]/div[2]/div[1]/div/div/div/input').send_keys('徐世伟')
        logger.info('输入有限合伙人姓名')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[2]/div/div[1]/form/div[2]/div[2]/div[2]/div/div/div/input').send_keys(
            '18601614687')
        logger.info('输入联系电话')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[2]/div/div[1]/form/div[2]/div[2]/div[3]/div[1]/div/div/input').send_keys(50)
        logger.info('输入出资比例')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[2]/div/div[1]/form/div[2]/div[2]/div[3]/div[2]/div/div/input').send_keys(
            '49787864694@qq.com')
        logger.info('输入qq邮箱')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[2]/div/div[1]/form/div[2]/div[3]/div[1]/div/div/div/input').send_keys(
            '622421199408156415')
        logger.info('输入身份证号码')
        sleep(1)
        tran = self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[2]/div/div[1]/form/div[2]/div[3]/div[2]/div/div/div[1]/input')
        self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        tran.send_keys('2020-5-23')
        sleep(1)
        # tran1 = self.driver.find_element_by_xpath(
        #     '//*[@id="generalPartners"]/div[2]/div/div[1]/form/div[2]/div[3]/div[2]/div/div/div/input[2]')
        # self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        # tran1.send_keys('2020-5-24')
        logger.info('输入有效期限')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[2]/div/div[1]/form/div[2]/div[3]/div[3]/div/div/div/input').click()
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[2]/div/div[1]/form/div[2]/div[3]/div[3]/div/div/div/input').send_keys(
            '上海市徐汇区锦辉大厦')
        logger.info('输入身份证地址')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[2]/div/div[1]/form/div[2]/div[1]/div[3]/div/div/div[1]/div/input').send_keys(
            image_path)
        logger.info('上传有限合伙身份证人像面')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[2]/div/div[1]/form/div[2]/div[1]/div[3]/div/div/div[2]/div/input').send_keys(
            image_path)
        logger.info('上传身份证国徽面')

        # 委派代表信息
        self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[1]/div[2]/div[2]/div[1]/div/div/div/input').send_keys('龚俊棋')
        logger.info('输入委派代表姓名')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[1]/div[2]/div[2]/div[2]/div/div/div/input').send_keys('18873665375')
        logger.info('输入联系电话')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[1]/div[2]/div[2]/div[3]/div/div/div/input').send_keys(
            '49787864694@qq.com')
        logger.info('输入qq邮箱')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[1]/div[2]/div[3]/div[1]/div/div/div/input').send_keys(
            '430702199610080514')
        logger.info('输入身份证号码')
        sleep(1)

        tran = self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[1]/div[2]/div[3]/div[2]/div/div/div[1]/input')
        self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        tran.send_keys('2020-5-23')
        sleep(1)
        # tran1 = self.driver.find_element_by_xpath(
        #     '//*[@id="supervisors"]/div[1]/form[1]/div[2]/div[3]/div[2]/div/div/div/input[2]')
        # self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        # tran1.send_keys('2020-5-24')
        logger.info('输入有效期限')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[1]/div[2]/div[3]/div[3]/div/div/div/input').click()
        self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[1]/div[2]/div[3]/div[3]/div/div/div/input').send_keys('上海市徐汇区锦辉大厦')
        logger.info('输入身份证地址')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[1]/div[2]/div[1]/div[3]/div/div/div[1]/div/input').send_keys(
            image_path)
        logger.info('上传委派代表身份证人像面')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[1]/div[2]/div[1]/div[3]/div/div/div[2]/div/input').send_keys(
            image_path)
        logger.info('上传身份证国徽面')

        # 财务负责人信息
        self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[2]/div[2]/div[2]/div[1]/div/div/div/input').send_keys('刘刚')
        logger.info('输入财务负责人姓名')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[2]/div[2]/div[2]/div[2]/div/div/div/input').send_keys('15216746163')
        logger.info('输入联系电话')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[2]/div[2]/div[2]/div[3]/div/div/div/input').send_keys(
            '49787864694@qq.com')
        logger.info('输入qq邮箱')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[2]/div[2]/div[3]/div[1]/div/div/div/input').send_keys(
            '340822199607245516')
        logger.info('输入身份证号码')
        sleep(1)
        tran = self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[2]/div[2]/div[3]/div[2]/div/div/div[1]/input')
        self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        tran.send_keys('2020-5-23')
        sleep(1)
        # tran1 = self.driver.find_element_by_xpath(
        #     '//*[@id="supervisors"]/div[1]/form[2]/div[2]/div[3]/div[2]/div/div/div/input[2]')
        # self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        # tran1.send_keys('2020-5-24')
        logger.info('输入有效期限')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[2]/div[2]/div[3]/div[3]/div/div/div/input').click()
        self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[2]/div[2]/div[3]/div[3]/div/div/div/input').send_keys('上海市徐汇区锦辉大厦3')
        logger.info('输入身份证地址')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[2]/div[2]/div[1]/div[3]/div/div/div[1]/div/input').send_keys(
            image_path)
        logger.info('上传财务负责人身份证人像面')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[2]/div[2]/div[1]/div[3]/div/div/div[2]/div/input').send_keys(
            image_path)
        logger.info('上传身份证国徽面')
        sleep(1)

        # 添加地址
        self.driver.find_element_by_xpath('//*[@id="address"]/div[1]/div[2]/button/span').click()
        logger.info('点击添加地址')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[1]/div/div/input').send_keys('aaa')
        logger.info('填写姓名')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[2]/div/div/input').send_keys(
            18273675403)
        logger.info('填写手机号码')
        sleep(1)
        logger.info('添加省')
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[3]/div/div[1]/div[1]/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "河北省"]').click()
        sleep(1)
        logger.info('添加市')
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[3]/div/div[2]/div[1]/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "石家庄市"]').click()
        sleep(1)
        logger.info('添加区')
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[3]/div/div[3]/div[1]/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "长安区"]').click()
        sleep(1)
        logger.info('填写具体地址')
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[4]/div/div/textarea').send_keys(
            '上海市徐汇区锦辉大厦')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[5]/div/label/span[1]/span').click()
        logger.info('设为默认地址')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[6]/div/button[1]/span').click()
        logger.info('点击确定')
        sleep(1)

        self.driver.find_element_by_xpath('//*[@id="address"]/div[2]/div[3]/form/div/div/div/div/div/input').send_keys(
            '上海市徐汇区')
        logger.info('填写联系地址')
        sleep(3)
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        logger.info('下拉滚动条')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="otherInfo"]/div[1]/div[2]/div/div/input').send_keys(image_path)
        logger.info('上传委托书')
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mainContainer"]/section[9]/div/div[2]/div[1]/button[2]').click()
        logger.info('点击保存并提交')
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="mainContainer"]/section[9]/div/div[2]/div[4]/div/div[3]/span/span[1]').click()
        logger.info('点击我已知晓')
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "我已阅读并同意以上内容"]').click()
        logger.info('点击我已阅读并同意以上内容')
        # self.driver.find_element_by_xpath(
        #     '//*[@id="mainContainer"]/section[7]/div/div[2]/div[2]/div/div[3]/span/span[1]').click()
        # logger.info('点击确定')
        # sleep(3)

    def sole_proprietorship_submission(self):
        self.driver.find_element_by_class_name('registrationWords').click()
        logger.info('点击注册类型')
        sleep(1)
        list1 = self.driver.window_handles
        self.driver.switch_to.window(list1[1])
        logger.info('切换窗口')
        self.driver.find_element_by_xpath('//div[text() = "个人独资注册"]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[1]/div[8]/div[2]/div[8]/div[1]/input').send_keys(0)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[1]/div[8]/div[2]/div[8]/div[2]/input').send_keys(0)
        logger.info('输入价格范围')
        sleep(1)
        self.driver.find_element_by_class_name('price_btn').click()
        logger.info('点击确定')
        sleep(1)
        self.driver.find_element_by_class_name('card-tit1').click()
        logger.info('点击一个直客产品')
        sleep(1)
        list1 = self.driver.window_handles
        self.driver.switch_to.window(list1[2])
        logger.info('切换窗口')
        self.driver.find_element_by_xpath('//a[text()="立即购买"]').click()
        logger.info('点击立即购买')
        sleep(2)
        # list1 = self.driver.window_handles
        # self.driver.switch_to.window(list1[3])
        # logger.info('切换窗口')
        self.driver.find_element_by_id('dealTxt').click()
        logger.info('已阅读并同意《用户服务协议》')
        sleep(1)
        self.driver.find_element_by_class_name('indent-total-button').click()
        logger.info('点击生成订单')
        sleep(1)
        self.driver.find_element_by_class_name('indent-total-button').click()
        logger.info('点击立即支付')
        sleep(3)
        self.driver.find_element_by_xpath('//a[text() = "马上提交"]').click()
        logger.info('点击马上提交')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="mainContainer"]/section[9]/div/div[2]/div[5]/div/div[3]/span/span').click()
        logger.info('点击我已知晓')
        # list1 = self.driver.window_handles
        # self.driver.switch_to.window(list1[1])
        # sleep(1)
        self.driver.find_elements_by_class_name('el-input__inner')[0].send_keys(200)
        logger.info('输入注册资金')
        sleep(1)
        self.driver.find_element_by_class_name('company-name').click()
        logger.info('点击行业名称')
        sleep(1)
        self.driver.find_element_by_xpath('//li[text() = "信息科技"]').click()
        logger.info('选择信息科技')
        sleep(1)
        for i in range(3):
            self.driver.find_element_by_class_name('assistant-btn').click()
            sleep(2)
            logger.info('点击起名助手')
            self.driver.find_element_by_xpath('//span[text() = "添加为备选名"]').click()
            sleep(1)
        self.driver.find_element_by_class_name('el-textarea__inner').clear()
        self.driver.find_element_by_class_name('el-textarea__inner').send_keys('经营范围')
        logger.info('输入经营范围')
        js = "var q=document.documentElement.scrollTop=500"
        self.driver.execute_script(js)
        sleep(2)
        logger.info('下拉滚动条')
        sleep(1)

        # 填写投资者信息
        self.driver.find_element_by_xpath(
            '//*[@id="investor"]/div[1]/form/div[2]/div[2]/div[1]/div/div/div/input').send_keys('龚俊棋')
        logger.info('输入投资者姓名')
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="investor"]/div[1]/form/div[2]/div[2]/div[2]/div/div/div/input').send_keys(
            '18873665375')
        logger.info('输入联系电话')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="investor"]/div[1]/form/div[2]/div[2]/div[3]/div/div/div/input').send_keys(
            '4964694@qq.com')
        logger.info('输入qq邮箱')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="investor"]/div[1]/form/div[2]/div[3]/div[1]/div/div/div/input').send_keys(
            '430702199610080514')
        logger.info('输入身份证号码')
        sleep(1)
        tran = self.driver.find_element_by_xpath(
            '//*[@id="investor"]/div[1]/form/div[2]/div[3]/div[2]/div/div/div[1]/input')
        self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        tran.send_keys('2020-5-23')
        sleep(1)
        # tran1 = self.driver.find_element_by_xpath(
        #     '//*[@id="investor"]/div[1]/form/div[2]/div[3]/div[2]/div/div/div/input[2]')
        # self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        # tran1.send_keys('2020-5-24')
        logger.info('输入有效期限')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="investor"]/div[1]/form/div[2]/div[3]/div[3]/div/div/div/input').click()
        self.driver.find_element_by_xpath(
            '//*[@id="investor"]/div[1]/form/div[2]/div[3]/div[3]/div/div/div/input').send_keys(
            '上海市徐汇区锦辉大厦')
        logger.info('输入身份证地址')
        sleep(3)
        self.driver.find_element_by_xpath(
            '//*[@id="investor"]/div[1]/form/div[2]/div[1]/div[3]/div/div/div[1]/div/input').send_keys(
            image_path)
        logger.info('上传股东身份证人像面')
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="investor"]/div[1]/form/div[2]/div[1]/div[3]/div/div/div[2]/div/input').send_keys(
            image_path)
        logger.info('上传身份证国徽面')
        sleep(1)

        js = "var q=document.documentElement.scrollTop=500"
        self.driver.execute_script(js)
        sleep(1)

        # 财务负责人信息
        self.driver.find_element_by_xpath(
            '//*[@id="appointedRepresentative"]/div[1]/form/div[2]/div[2]/div[1]/div/div/div/input').send_keys('刘刚')
        logger.info('输入财务负责人姓名')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="appointedRepresentative"]/div[1]/form/div[2]/div[2]/div[2]/div/div/div/input').send_keys(
            '15216746163')
        logger.info('输入联系电话')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="appointedRepresentative"]/div[1]/form/div[2]/div[2]/div[3]/div/div/div/input').send_keys(
            '49787864694@qq.com')
        logger.info('输入qq邮箱')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="appointedRepresentative"]/div[1]/form/div[2]/div[3]/div[1]/div/div/div/input').send_keys(
            '340822199607245516')
        logger.info('输入身份证号码')
        sleep(1)
        tran = self.driver.find_element_by_xpath(
            '//*[@id="appointedRepresentative"]/div[1]/form/div[2]/div[3]/div[2]/div/div/div[1]/input')
        self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        tran.send_keys('2020-5-23')
        sleep(1)
        # tran1 = self.driver.find_element_by_xpath(
        #     '//*[@id="appointedRepresentative"]/div[1]/form/div[2]/div[3]/div[2]/div/div/div/input[2]')
        # self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        # tran1.send_keys('2020-5-24')
        logger.info('输入有效期限')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="appointedRepresentative"]/div[1]/form/div[2]/div[3]/div[3]/div/div/div/input').click()
        self.driver.find_element_by_xpath(
            '//*[@id="appointedRepresentative"]/div[1]/form/div[2]/div[3]/div[3]/div/div/div/input').send_keys(
            '上海市徐汇区锦辉大厦3')
        logger.info('输入身份证地址')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="appointedRepresentative"]/div[1]/form/div[2]/div[1]/div[3]/div/div/div[1]/div/input').send_keys(
            image_path)
        logger.info('上传财务负责人身份证人像面')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="appointedRepresentative"]/div[1]/form/div[2]/div[1]/div[3]/div/div/div[2]/div/input').send_keys(
            image_path)
        logger.info('上传身份证国徽面')
        sleep(1)

        # 添加地址
        self.driver.find_element_by_xpath('//*[@id="address"]/div[1]/div[2]/button/span').click()
        logger.info('点击添加地址')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[1]/div/div/input').send_keys('aaa')
        logger.info('填写姓名')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[2]/div/div/input').send_keys(
            18273675403)
        logger.info('填写手机号码')
        sleep(1)
        logger.info('添加省')
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[3]/div/div[1]/div[1]/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "河北省"]').click()
        sleep(1)
        logger.info('添加市')
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[3]/div/div[2]/div[1]/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "石家庄市"]').click()
        sleep(1)
        logger.info('添加区')
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[3]/div/div[3]/div[1]/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "长安区"]').click()
        sleep(1)
        logger.info('填写具体地址')
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[4]/div/div/textarea').send_keys(
            '上海市徐汇区锦辉大厦')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[5]/div/label/span[1]/span').click()
        logger.info('设为默认地址')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[6]/div/button[1]/span').click()
        logger.info('点击确定')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="address"]/div[2]/div[3]/form/div/div/div/div/div/input').send_keys(
            '上海市徐汇区')
        logger.info('填写联系地址')
        sleep(3)
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        logger.info('下拉滚动条')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="otherInfo"]/div[1]/div[2]/div/div/input').send_keys(image_path)
        logger.info('上传委托书')
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mainContainer"]/section[9]/div/div[2]/div[1]/button[2]').click()
        logger.info('点击保存并提交')
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mainContainer"]/section[9]/div/div[2]/div[4]/div/div[3]/span/span[1]').click()
        logger.info('点击我已知晓')
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "我已阅读并同意以上内容"]').click()
        logger.info('点击我已阅读并同意以上内容')


class HeLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = executable)
        logger.info('打开谷歌浏览器')
        self.driver.get(items1['test3'])
        logger.info('打开网址')
        self.driver.maximize_window()
        logger.info('浏览器最大化')
        # self.driver.find_element_by_class_name('close-img').click()
        # logger.info('关闭弹窗')
        self.driver.implicitly_wait(10)
        logger.info('等待10s')
        self.driver.find_element_by_xpath('//a[text() = "合作商登录"]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="pane-partner"]/form/div[1]/div/div/input').send_keys('ax20')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="pane-partner"]/form/div[2]/div/div/input').send_keys('hhr123456')
        sleep(4)
        self.driver.find_element_by_xpath('//*[@id="pane-partner"]/form/div[3]/div/div/input').send_keys(
            'hhr123456')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="pane-partner"]/form/div[5]/button[1]/span').click()
        sleep(3)

    def tearDown(self):
        self.driver.find_element_by_xpath('//a[@href = "/customer/exit.html"]').click()
        logger.info('退出登录')
        sleep(3)
        self.driver.quit()

    def select_park_service(self, price=0, endprice=0):
        self.driver.find_element_by_class_name('registrationWords').click()
        logger.info('点击注册类型')
        list1 = self.driver.window_handles
        self.driver.switch_to.window(list1[1])
        logger.info('切换窗口')
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[1]/div[8]/div[2]/div[8]/div[1]/input').send_keys(price)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[1]/div[8]/div[2]/div[8]/div[2]/input').send_keys(endprice)
        logger.info('输入价格范围')
        sleep(2)
        self.driver.find_element_by_class_name('price_btn').click()
        logger.info('点击确定')
        sleep(2)
        self.driver.find_element_by_class_name('card-tit1').click()
        logger.info('点击一个直客产品')
        list1 = self.driver.window_handles
        self.driver.switch_to.window(list1[2])
        logger.info('切换窗口')
        self.driver.find_element_by_xpath('//a[text()="立即购买"]').click()
        logger.info('点击立即购买')
        sleep(3)
        self.driver.find_element_by_id('dealTxt').click()
        logger.info('已阅读并同意《用户服务协议》')
        self.driver.find_element_by_class_name('indent-total-button').click()
        logger.info('点击生成订单')
        sleep(2)

    def select_enterprise_service(self, price=0, endprice=0):
        self.driver.find_element_by_id('nav_item_serviceMall').click()
        logger.info('点击企服商城')
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)
        logger.info('执行下滑操作')
        self.driver.find_element_by_xpath('//a[text() = "更多 >"]').click()
        logger.info('点击更多')
        list1 = self.driver.window_handles
        self.driver.switch_to.window(list1[1])
        logger.info('切换窗口')
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div[2]/div[2]/div[2]/section[1]/div[2]/ul/li[7]/input').send_keys(price)
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div[2]/div[2]/div[2]/section[1]/div[2]/ul/li[8]/input').send_keys(endprice)
        logger.info('输入价格范围')
        sleep(1)
        self.driver.find_element_by_class_name('certainBtn').click()
        logger.info('点击确定')
        sleep(2)
        self.driver.find_element_by_class_name('headline').click()
        logger.info('点击一个企服商城产品')
        list2 = self.driver.window_handles
        self.driver.switch_to.window(list2[2])
        logger.info('切换窗口')
        self.driver.find_element_by_class_name('btn1').click()
        logger.info('点击立即购买')
        sleep(3)
        self.driver.find_element_by_xpath('//button[text()="生成订单"]').click()
        logger.info('点击生成订单')
        sleep(2)

    def helimited_company_submitting_information(self):
        """直客购买有限注册提交资料"""
        self.driver.find_element_by_class_name('registrationWords').click()
        logger.info('点击注册类型')
        sleep(1)
        list1 = self.driver.window_handles
        self.driver.switch_to.window(list1[1])
        logger.info('切换窗口')
        sleep(1)
        self.driver.find_element_by_xpath('//div[text() = "有限公司注册"]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[1]/div[8]/div[2]/div[8]/div[1]/input').send_keys(0)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[1]/div[8]/div[2]/div[8]/div[2]/input').send_keys(0)
        logger.info('输入价格范围')
        sleep(1)
        self.driver.find_element_by_class_name('price_btn').click()
        logger.info('点击确定')
        sleep(1)
        self.driver.find_element_by_class_name('card-tit1').click()
        logger.info('点击一个直客产品')
        sleep(1)
        list1 = self.driver.window_handles
        self.driver.switch_to.window(list1[2])
        logger.info('切换窗口')
        self.driver.find_element_by_xpath('//a[text()="立即购买"]').click()
        logger.info('点击立即购买')
        sleep(2)
        # list1 = self.driver.window_handles
        # self.driver.switch_to.window(list1[3])
        # logger.info('切换窗口')
        self.driver.find_element_by_id('dealTxt').click()
        logger.info('已阅读并同意《用户服务协议》')
        sleep(1)
        self.driver.find_element_by_class_name('indent-total-button').click()
        logger.info('点击生成订单')
        sleep(1)
        self.driver.find_element_by_class_name('indent-total-button').click()
        logger.info('点击立即支付')
        sleep(3)
        self.driver.find_element_by_xpath('//a[text() = "马上提交"]').click()
        logger.info('点击马上提交')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="mainContainer"]/section[9]/div/div[2]/div[5]/div/div[3]/span/span').click()
        logger.info('点击我已知晓')
        # list1 = self.driver.window_handles
        # self.driver.switch_to.window(list1[1])
        sleep(1)
        self.driver.find_elements_by_class_name('el-input__inner')[0].send_keys(200)
        logger.info('输入注册资金')
        sleep(1)
        self.driver.find_element_by_class_name('company-name').click()
        logger.info('点击行业名称')
        sleep(1)
        self.driver.find_element_by_xpath('//li[text() = "信息科技"]').click()
        logger.info('选择信息科技')
        sleep(1)
        for i in range(3):
            self.driver.find_element_by_class_name('assistant-btn').click()
            sleep(2)
            logger.info('点击起名助手')
            self.driver.find_element_by_xpath('//span[text() = "添加为备选名"]').click()
            sleep(1)
        self.driver.find_element_by_class_name('el-textarea__inner').clear()
        self.driver.find_element_by_class_name('el-textarea__inner').send_keys('经营范围')
        logger.info('输入经营范围')
        js = "var q=document.documentElement.scrollTop=500"
        self.driver.execute_script(js)
        sleep(2)
        logger.info('下拉滚动条')
        sleep(1)

        # 填写股东信息
        self.driver.find_element_by_xpath(
            '//*[@id="shareholder"]/div[1]/form/div[2]/div[2]/div[1]/div/div/div/input').send_keys('龚俊棋')
        logger.info('输入姓名')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="shareholder"]/div[1]/form/div[2]/div[2]/div[2]/div/div/div/input').send_keys('18873665375')
        logger.info('输入联系电话')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="shareholder"]/div[1]/form/div[2]/div[2]/div[3]/div[1]/div/div/input').send_keys(100)
        logger.info('输入出资比例')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="shareholder"]/div[1]/form/div[2]/div[2]/div[3]/div[2]/div/div/input').send_keys('4964694@qq.com')
        logger.info('输入qq邮箱')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="shareholder"]/div[1]/form/div[2]/div[3]/div[1]/div/div/div/input').send_keys('430702199610080514')
        logger.info('输入身份证号码')
        sleep(1)
        # self.driver.find_elements_by_class_name('el-range-input')[0].click()
        sleep(1)
        tran = self.driver.find_element_by_xpath('//*[@id="shareholder"]/div[1]/form/div[2]/div[3]/div['
                                                 '2]/div/div/div[1]/input')
        self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        tran.send_keys('2020-5-23')
        sleep(1)
        # tran1 = self.driver.find_elements_by_class_name('el-range-input')[1]
        # self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran1)
        # tran1.send_keys('2020-5-24')
        logger.info('输入有效期限')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="shareholder"]/div[1]/form/div[2]/div[3]/div[3]/div/div/div/input').click()
        self.driver.find_element_by_xpath(
            '//*[@id="shareholder"]/div[1]/form/div[2]/div[3]/div[3]/div/div/div/input').send_keys('上海市徐汇区锦辉大厦')
        logger.info('输入身份证地址')
        sleep(2)
        self.driver.find_elements_by_name('file')[0].send_keys(image_path)
        logger.info('上传股东身份证人像面')
        sleep(2)
        self.driver.find_elements_by_name('file')[1].send_keys(image_path)
        logger.info('上传身份证国徽面')
        sleep(2)
        # js = "var q=document.documentElement.scrollTop=500"
        # self.driver.execute_script(js)

        # 填写法人信息
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[1]/div[2]/div[2]/div[1]/div/div/div/input').send_keys('徐世伟')
        logger.info('输入法人姓名')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[1]/div[2]/div[2]/div[2]/div/div/div/input').send_keys('18601614687')
        logger.info('输入联系电话')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[1]/div[2]/div[2]/div[3]/div/div/div/input').send_keys(
            '49787864694@qq.com')
        logger.info('输入qq邮箱')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[1]/div[2]/div[3]/div[1]/div/div/div/input').send_keys(
            '622421199408156415')
        logger.info('输入身份证号码')
        sleep(1)
        tran = self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[1]/div[2]/div[3]/div[2]/div/div/div[1]/input')
        self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        tran.send_keys('2020-5-23')
        sleep(1)
        # tran1 = self.driver.find_element_by_xpath(
        #     '//*[@id="corporations"]/div[1]/form[1]/div[2]/div[3]/div[2]/div/div/div/input[2]')
        # self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        # tran1.send_keys('2020-5-24')
        logger.info('输入有效期限')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[3]/div[2]/div[3]/div[3]/div/div/div/input').click()
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[1]/div[2]/div[3]/div[3]/div/div/div/input').send_keys('上海市徐汇区锦辉大厦')
        logger.info('输入身份证地址')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[1]/div[2]/div[1]/div[3]/div/div/div[1]/div/input').send_keys(
            image_path)
        logger.info('上传法人身份证人像面')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[1]/div[2]/div[1]/div[3]/div/div/div[2]/div/input').send_keys(
            image_path)
        logger.info('上传身份证国徽面')

        # 监事信息
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[2]/div[2]/div[2]/div[1]/div/div/div[1]/input').send_keys('龚俊棋')
        logger.info('输入监事姓名')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[2]/div[2]/div[2]/div[2]/div/div/div/input').send_keys('18873665375')
        logger.info('输入联系电话')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[2]/div[2]/div[2]/div[3]/div/div/div/input').send_keys(
            '49787864694@qq.com')
        logger.info('输入qq邮箱')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[2]/div[2]/div[3]/div[1]/div/div/div/input').send_keys(
            '430702199610080514')
        logger.info('输入身份证号码')
        sleep(1)

        tran = self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[2]/div[2]/div[3]/div[2]/div/div/div[1]/input')
        self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        tran.send_keys('2020-5-23')
        sleep(1)
        # tran1 = self.driver.find_element_by_xpath(
        #     '//*[@id="corporations"]/div[1]/form[2]/div[2]/div[3]/div[2]/div/div/div/input[2]')
        # self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        # tran1.send_keys('2020-5-24')
        logger.info('输入有效期限')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[2]/div[2]/div[3]/div[3]/div/div/div/input').click()
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[2]/div[2]/div[3]/div[3]/div/div/div/input').send_keys('上海市徐汇区锦辉大厦')
        logger.info('输入身份证地址')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[2]/div[2]/div[1]/div[3]/div/div/div[1]/div/input').send_keys(
            image_path)
        logger.info('上传监事身份证人像面')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[2]/div[2]/div[1]/div[3]/div/div/div[2]/div/input').send_keys(
            image_path)
        logger.info('上传身份证国徽面')

        # 财务负责人信息
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[3]/div[2]/div[2]/div[1]/div/div/div/input').send_keys('刘刚')
        logger.info('输入财务负责人姓名')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[3]/div[2]/div[2]/div[2]/div/div/div/input').send_keys('15216746163')
        logger.info('输入联系电话')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[3]/div[2]/div[2]/div[3]/div/div/div/input').send_keys(
            '49787864694@qq.com')
        logger.info('输入qq邮箱')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[3]/div[2]/div[3]/div[1]/div/div/div/input').send_keys(
            '340822199607245516')
        logger.info('输入身份证号码')
        sleep(1)
        tran = self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[3]/div[2]/div[3]/div[2]/div/div/div[1]/input')
        self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        tran.send_keys('2020-5-23')
        sleep(1)
        # tran1 = self.driver.find_element_by_xpath(
        #     '//*[@id="corporations"]/div[1]/form[3]/div[2]/div[3]/div[2]/div/div/div/input[2]')
        # self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        # tran1.send_keys('2020-5-24')
        logger.info('输入有效期限')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[3]/div[2]/div[3]/div[3]/div/div/div/input').click()
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[3]/div[2]/div[3]/div[3]/div/div/div/input').send_keys('上海市徐汇区锦辉大厦3')
        logger.info('输入身份证地址')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[3]/div[2]/div[1]/div[3]/div/div/div[1]/div/input').send_keys(
            image_path)
        logger.info('上传财务负责人身份证人像面')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="corporations"]/div[1]/form[3]/div[2]/div[1]/div[3]/div/div/div[2]/div/input').send_keys(
            image_path)
        logger.info('上传身份证国徽面')

        # 添加地址
        self.driver.find_element_by_xpath('//*[@id="address"]/div[1]/div[2]/button/span').click()
        logger.info('点击添加地址')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[1]/div/div/input').send_keys('aaa')
        logger.info('填写姓名')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[2]/div/div/input').send_keys(
            18273675403)
        logger.info('填写手机号码')
        sleep(1)
        logger.info('添加省')
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[3]/div/div[1]/div[1]/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "河北省"]').click()
        sleep(1)
        logger.info('添加市')
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[3]/div/div[2]/div[1]/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "石家庄市"]').click()
        sleep(1)
        logger.info('添加区')
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[3]/div/div[3]/div[1]/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "长安区"]').click()
        sleep(1)
        logger.info('填写具体地址')
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[4]/div/div/textarea').send_keys(
            '上海市徐汇区锦辉大厦')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[5]/div/label/span[1]/span').click()
        logger.info('设为默认地址')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[6]/div/button[1]/span').click()
        logger.info('点击确定')
        sleep(1)

        self.driver.find_element_by_xpath('//*[@id="address"]/div[2]/div[3]/form/div/div/div/div/div/input').send_keys(
            '上海市徐汇区')
        logger.info('填写联系地址')
        sleep(2)
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        logger.info('下拉滚动条')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="otherInfo"]/div[1]/div[2]/div/div/input').send_keys(image_path)
        logger.info('上传委托书')
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mainContainer"]/section[9]/div/div[2]/div[1]/button[2]').click()
        logger.info('点击保存并提交')
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mainContainer"]/section[9]/div/div[2]/div[4]/div/div[3]/span/span[1]').click()
        logger.info('点击我已知晓')
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "我已阅读并同意以上内容"]').click()
        logger.info('点击我已阅读并同意以上内容')

    def helimited_partnership_submission(self):
        self.driver.find_element_by_class_name('registrationWords').click()
        logger.info('点击注册类型')
        sleep(1)
        list1 = self.driver.window_handles
        self.driver.switch_to.window(list1[1])
        logger.info('切换窗口')
        sleep(1)
        self.driver.find_element_by_xpath('//div[text() = "有限合伙注册"]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[1]/div[8]/div[2]/div[8]/div[1]/input').send_keys(0)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[1]/div[8]/div[2]/div[8]/div[2]/input').send_keys(0)
        logger.info('输入价格范围')
        sleep(1)
        self.driver.find_element_by_class_name('price_btn').click()
        logger.info('点击确定')
        sleep(1)
        self.driver.find_element_by_class_name('card-tit1').click()
        logger.info('点击一个直客产品')
        sleep(1)
        list1 = self.driver.window_handles
        self.driver.switch_to.window(list1[2])
        logger.info('切换窗口')
        self.driver.find_element_by_xpath('//a[text()="立即购买"]').click()
        sleep(3)
        logger.info('点击立即购买')
        # list1 = self.driver.window_handles
        # self.driver.switch_to.window(list1[3])
        # logger.info('切换窗口')
        self.driver.find_element_by_id('dealTxt').click()
        logger.info('已阅读并同意《用户服务协议》')
        sleep(1)
        self.driver.find_element_by_class_name('indent-total-button').click()
        logger.info('点击生成订单')
        sleep(1)
        self.driver.find_element_by_class_name('indent-total-button').click()
        logger.info('点击立即支付')
        sleep(3)
        self.driver.find_element_by_xpath('//a[text() = "马上提交"]').click()
        logger.info('点击马上提交')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="mainContainer"]/section[9]/div/div[2]/div[5]/div/div[3]/span/span').click()
        logger.info('点击我已知晓')
        # list1 = self.driver.window_handles
        # self.driver.switch_to.window(list1[1])
        # sleep(1)
        self.driver.find_elements_by_class_name('el-input__inner')[0].send_keys(200)
        logger.info('输入注册资金')
        sleep(1)
        self.driver.find_element_by_class_name('company-name').click()
        logger.info('点击行业名称')
        sleep(1)
        self.driver.find_element_by_xpath('//li[text() = "信息科技"]').click()
        logger.info('选择信息科技')
        sleep(1)
        for i in range(3):
            self.driver.find_element_by_class_name('assistant-btn').click()
            sleep(2)
            logger.info('点击起名助手')
            self.driver.find_element_by_xpath('//span[text() = "添加为备选名"]').click()
            sleep(1)
        self.driver.find_element_by_class_name('el-textarea__inner').clear()
        self.driver.find_element_by_class_name('el-textarea__inner').send_keys('经营范围')
        logger.info('输入经营范围')
        js = "var q=document.documentElement.scrollTop=500"
        self.driver.execute_script(js)
        sleep(2)
        logger.info('下拉滚动条')
        sleep(1)

        # 填写普通合伙人信息
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[1]/div/div[1]/form/div[2]/div[2]/div[1]/div/div/div/input').send_keys('龚俊棋')
        logger.info('输入普通合伙人姓名')
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[1]/div/div[1]/form/div[2]/div[2]/div[2]/div/div/div/input').send_keys(
            '18873665375')
        logger.info('输入联系电话')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[1]/div/div[1]/form/div[2]/div[2]/div[3]/div[1]/div/div/input').send_keys(50)
        logger.info('输入出资比例')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[1]/div/div[1]/form/div[2]/div[2]/div[3]/div[2]/div/div/input').send_keys(
            '4964694@qq.com')
        logger.info('输入qq邮箱')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[1]/div/div[1]/form/div[2]/div[3]/div[1]/div/div/div/input').send_keys(
            '430702199610080514')
        logger.info('输入身份证号码')
        sleep(1)
        tran = self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[1]/div/div[1]/form/div[2]/div[3]/div[2]/div/div/div[1]/input')
        self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        tran.send_keys('2020-5-23')
        sleep(1)
        logger.info('输入有效期限')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[1]/div/div[1]/form/div[2]/div[3]/div[3]/div/div/div/input').click()
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[1]/div/div[1]/form/div[2]/div[3]/div[3]/div/div/div/input').send_keys(
            '上海市徐汇区锦辉大厦')
        logger.info('输入身份证地址')
        sleep(3)
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[1]/div/div[1]/form/div[2]/div[1]/div[3]/div/div/div[1]/div/input').send_keys(
            image_path)
        logger.info('上传股东身份证人像面')
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[1]/div/div[1]/form/div[2]/div[1]/div[3]/div/div/div[2]/div/input').send_keys(
            image_path)
        logger.info('上传身份证国徽面')
        sleep(1)

        js = "var q=document.documentElement.scrollTop=500"
        self.driver.execute_script(js)
        sleep(1)

        # 填写有限合伙人信息
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[2]/div/div[1]/form/div[2]/div[2]/div[1]/div/div/div/input').send_keys('徐世伟')
        logger.info('输入有限合伙人姓名')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[2]/div/div[1]/form/div[2]/div[2]/div[2]/div/div/div/input').send_keys(
            '18601614687')
        logger.info('输入联系电话')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[2]/div/div[1]/form/div[2]/div[2]/div[3]/div[1]/div/div/input').send_keys(50)
        logger.info('输入出资比例')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[2]/div/div[1]/form/div[2]/div[2]/div[3]/div[2]/div/div/input').send_keys(
            '49787864694@qq.com')
        logger.info('输入qq邮箱')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[2]/div/div[1]/form/div[2]/div[3]/div[1]/div/div/div/input').send_keys(
            '622421199408156415')
        logger.info('输入身份证号码')
        sleep(1)
        tran = self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[2]/div/div[1]/form/div[2]/div[3]/div[2]/div/div/div[1]/input')
        self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        tran.send_keys('2020-5-23')
        sleep(1)
        # tran1 = self.driver.find_element_by_xpath(
        #     '//*[@id="generalPartners"]/div[2]/div/div[1]/form/div[2]/div[3]/div[2]/div/div/div/input[2]')
        # self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        # tran1.send_keys('2020-5-24')
        logger.info('输入有效期限')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[2]/div/div[1]/form/div[2]/div[3]/div[3]/div/div/div/input').click()
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[2]/div/div[1]/form/div[2]/div[3]/div[3]/div/div/div/input').send_keys(
            '上海市徐汇区锦辉大厦')
        logger.info('输入身份证地址')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[2]/div/div[1]/form/div[2]/div[1]/div[3]/div/div/div[1]/div/input').send_keys(
            image_path)
        logger.info('上传有限合伙身份证人像面')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="generalPartners"]/div[2]/div/div[1]/form/div[2]/div[1]/div[3]/div/div/div[2]/div/input').send_keys(
            image_path)
        logger.info('上传身份证国徽面')

        # 委派代表信息
        self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[1]/div[2]/div[2]/div[1]/div/div/div/input').send_keys('龚俊棋')
        logger.info('输入委派代表姓名')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[1]/div[2]/div[2]/div[2]/div/div/div/input').send_keys('18873665375')
        logger.info('输入联系电话')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[1]/div[2]/div[2]/div[3]/div/div/div/input').send_keys(
            '49787864694@qq.com')
        logger.info('输入qq邮箱')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[1]/div[2]/div[3]/div[1]/div/div/div/input').send_keys(
            '430702199610080514')
        logger.info('输入身份证号码')
        sleep(1)

        tran = self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[1]/div[2]/div[3]/div[2]/div/div/div[1]/input')
        self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        tran.send_keys('2020-5-23')
        sleep(1)
        # tran1 = self.driver.find_element_by_xpath(
        #     '//*[@id="supervisors"]/div[1]/form[1]/div[2]/div[3]/div[2]/div/div/div/input[2]')
        # self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        # tran1.send_keys('2020-5-24')
        logger.info('输入有效期限')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[1]/div[2]/div[3]/div[3]/div/div/div/input').click()
        self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[1]/div[2]/div[3]/div[3]/div/div/div/input').send_keys('上海市徐汇区锦辉大厦')
        logger.info('输入身份证地址')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[1]/div[2]/div[1]/div[3]/div/div/div[1]/div/input').send_keys(
            image_path)
        logger.info('上传委派代表身份证人像面')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[1]/div[2]/div[1]/div[3]/div/div/div[2]/div/input').send_keys(
            image_path)
        logger.info('上传身份证国徽面')

        # 财务负责人信息
        self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[2]/div[2]/div[2]/div[1]/div/div/div/input').send_keys('刘刚')
        logger.info('输入财务负责人姓名')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[2]/div[2]/div[2]/div[2]/div/div/div/input').send_keys('15216746163')
        logger.info('输入联系电话')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[2]/div[2]/div[2]/div[3]/div/div/div/input').send_keys(
            '49787864694@qq.com')
        logger.info('输入qq邮箱')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[2]/div[2]/div[3]/div[1]/div/div/div/input').send_keys(
            '340822199607245516')
        logger.info('输入身份证号码')
        sleep(1)
        tran = self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[2]/div[2]/div[3]/div[2]/div/div/div[1]/input')
        self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        tran.send_keys('2020-5-23')
        sleep(1)
        # tran1 = self.driver.find_element_by_xpath(
        #     '//*[@id="supervisors"]/div[1]/form[2]/div[2]/div[3]/div[2]/div/div/div/input[2]')
        # self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        # tran1.send_keys('2020-5-24')
        logger.info('输入有效期限')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[2]/div[2]/div[3]/div[3]/div/div/div/input').click()
        self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[2]/div[2]/div[3]/div[3]/div/div/div/input').send_keys('上海市徐汇区锦辉大厦3')
        logger.info('输入身份证地址')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[2]/div[2]/div[1]/div[3]/div/div/div[1]/div/input').send_keys(
            image_path)
        logger.info('上传财务负责人身份证人像面')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="supervisors"]/div[1]/form[2]/div[2]/div[1]/div[3]/div/div/div[2]/div/input').send_keys(
            image_path)
        logger.info('上传身份证国徽面')
        sleep(1)

        # 添加地址
        self.driver.find_element_by_xpath('//*[@id="address"]/div[1]/div[2]/button/span').click()
        logger.info('点击添加地址')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[1]/div/div/input').send_keys('aaa')
        logger.info('填写姓名')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[2]/div/div/input').send_keys(
            18273675403)
        logger.info('填写手机号码')
        sleep(1)
        logger.info('添加省')
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[3]/div/div[1]/div[1]/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "河北省"]').click()
        sleep(1)
        logger.info('添加市')
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[3]/div/div[2]/div[1]/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "石家庄市"]').click()
        sleep(1)
        logger.info('添加区')
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[3]/div/div[3]/div[1]/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "长安区"]').click()
        sleep(1)
        logger.info('填写具体地址')
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[4]/div/div/textarea').send_keys(
            '上海市徐汇区锦辉大厦')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[5]/div/label/span[1]/span').click()
        logger.info('设为默认地址')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[6]/div/button[1]/span').click()
        logger.info('点击确定')
        sleep(1)

        self.driver.find_element_by_xpath('//*[@id="address"]/div[2]/div[3]/form/div/div/div/div/div/input').send_keys(
            '上海市徐汇区')
        logger.info('填写联系地址')
        sleep(3)
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        logger.info('下拉滚动条')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="otherInfo"]/div[1]/div[2]/div/div/input').send_keys(image_path)
        logger.info('上传委托书')
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mainContainer"]/section[9]/div/div[2]/div[1]/button[2]').click()
        logger.info('点击保存并提交')
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="mainContainer"]/section[9]/div/div[2]/div[4]/div/div[3]/span/span[1]').click()
        logger.info('点击我已知晓')
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "我已阅读并同意以上内容"]').click()
        logger.info('点击我已阅读并同意以上内容')
        # self.driver.find_element_by_xpath(
        #     '//*[@id="mainContainer"]/section[7]/div/div[2]/div[2]/div/div[3]/span/span[1]').click()
        # logger.info('点击确定')
        # sleep(3)

    def hesole_proprietorship_submission(self):
        self.driver.find_element_by_class_name('registrationWords').click()
        logger.info('点击注册类型')
        sleep(1)
        list1 = self.driver.window_handles
        self.driver.switch_to.window(list1[1])
        logger.info('切换窗口')
        self.driver.find_element_by_xpath('//div[text() = "个人独资注册"]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[1]/div[8]/div[2]/div[8]/div[1]/input').send_keys(0)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[1]/div[8]/div[2]/div[8]/div[2]/input').send_keys(0)
        logger.info('输入价格范围')
        sleep(1)
        self.driver.find_element_by_class_name('price_btn').click()
        logger.info('点击确定')
        sleep(1)
        self.driver.find_element_by_class_name('card-tit1').click()
        logger.info('点击一个直客产品')
        sleep(1)
        list1 = self.driver.window_handles
        self.driver.switch_to.window(list1[2])
        logger.info('切换窗口')
        self.driver.find_element_by_xpath('//a[text()="立即购买"]').click()
        logger.info('点击立即购买')
        sleep(4)
        # list1 = self.driver.window_handles
        # self.driver.switch_to.window(list1[3])
        # logger.info('切换窗口')
        self.driver.find_element_by_id('dealTxt').click()
        logger.info('已阅读并同意《用户服务协议》')
        sleep(1)
        self.driver.find_element_by_class_name('indent-total-button').click()
        logger.info('点击生成订单')
        sleep(1)
        self.driver.find_element_by_class_name('indent-total-button').click()
        logger.info('点击立即支付')
        sleep(3)
        self.driver.find_element_by_xpath('//a[text() = "马上提交"]').click()
        logger.info('点击马上提交')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="mainContainer"]/section[9]/div/div[2]/div[5]/div/div[3]/span/span').click()
        logger.info('点击我已知晓')
        # list1 = self.driver.window_handles
        # self.driver.switch_to.window(list1[1])
        # sleep(1)
        self.driver.find_elements_by_class_name('el-input__inner')[0].send_keys(200)
        logger.info('输入注册资金')
        sleep(1)
        self.driver.find_element_by_class_name('company-name').click()
        logger.info('点击行业名称')
        sleep(1)
        self.driver.find_element_by_xpath('//li[text() = "信息科技"]').click()
        logger.info('选择信息科技')
        sleep(1)
        for i in range(3):
            self.driver.find_element_by_class_name('assistant-btn').click()
            sleep(2)
            logger.info('点击起名助手')
            self.driver.find_element_by_xpath('//span[text() = "添加为备选名"]').click()
            sleep(1)
        self.driver.find_element_by_class_name('el-textarea__inner').clear()
        self.driver.find_element_by_class_name('el-textarea__inner').send_keys('经营范围')
        logger.info('输入经营范围')
        js = "var q=document.documentElement.scrollTop=500"
        self.driver.execute_script(js)
        sleep(2)
        logger.info('下拉滚动条')
        sleep(1)

        # 填写投资者信息
        self.driver.find_element_by_xpath(
            '//*[@id="investor"]/div[1]/form/div[2]/div[2]/div[1]/div/div/div/input').send_keys('龚俊棋')
        logger.info('输入投资者姓名')
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="investor"]/div[1]/form/div[2]/div[2]/div[2]/div/div/div/input').send_keys(
            '18873665375')
        logger.info('输入联系电话')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="investor"]/div[1]/form/div[2]/div[2]/div[3]/div/div/div/input').send_keys(
            '4964694@qq.com')
        logger.info('输入qq邮箱')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="investor"]/div[1]/form/div[2]/div[3]/div[1]/div/div/div/input').send_keys(
            '430702199610080514')
        logger.info('输入身份证号码')
        sleep(1)
        tran = self.driver.find_element_by_xpath(
            '//*[@id="investor"]/div[1]/form/div[2]/div[3]/div[2]/div/div/div[1]/input')
        self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        tran.send_keys('2020-5-23')
        sleep(1)
        # tran1 = self.driver.find_element_by_xpath(
        #     '//*[@id="investor"]/div[1]/form/div[2]/div[3]/div[2]/div/div/div/input[2]')
        # self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        # tran1.send_keys('2020-5-24')
        logger.info('输入有效期限')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="investor"]/div[1]/form/div[2]/div[3]/div[3]/div/div/div/input').click()
        self.driver.find_element_by_xpath(
            '//*[@id="investor"]/div[1]/form/div[2]/div[3]/div[3]/div/div/div/input').send_keys(
            '上海市徐汇区锦辉大厦')
        logger.info('输入身份证地址')
        sleep(3)
        self.driver.find_element_by_xpath(
            '//*[@id="investor"]/div[1]/form/div[2]/div[1]/div[3]/div/div/div[1]/div/input').send_keys(
            image_path)
        logger.info('上传股东身份证人像面')
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="investor"]/div[1]/form/div[2]/div[1]/div[3]/div/div/div[2]/div/input').send_keys(
            image_path)
        logger.info('上传身份证国徽面')
        sleep(1)

        js = "var q=document.documentElement.scrollTop=500"
        self.driver.execute_script(js)
        sleep(1)

        # 财务负责人信息
        self.driver.find_element_by_xpath(
            '//*[@id="appointedRepresentative"]/div[1]/form/div[2]/div[2]/div[1]/div/div/div/input').send_keys('刘刚')
        logger.info('输入财务负责人姓名')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="appointedRepresentative"]/div[1]/form/div[2]/div[2]/div[2]/div/div/div/input').send_keys(
            '15216746163')
        logger.info('输入联系电话')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="appointedRepresentative"]/div[1]/form/div[2]/div[2]/div[3]/div/div/div/input').send_keys(
            '49787864694@qq.com')
        logger.info('输入qq邮箱')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="appointedRepresentative"]/div[1]/form/div[2]/div[3]/div[1]/div/div/div/input').send_keys(
            '340822199607245516')
        logger.info('输入身份证号码')
        sleep(1)
        tran = self.driver.find_element_by_xpath(
            '//*[@id="appointedRepresentative"]/div[1]/form/div[2]/div[3]/div[2]/div/div/div[1]/input')
        self.driver.execute_script("arguments[0].removeAttribute('autocomplete');", tran)
        tran.send_keys('2020-5-23')
        sleep(1)
        logger.info('输入有效期限')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="appointedRepresentative"]/div[1]/form/div[2]/div[3]/div[3]/div/div/div/input').click()
        self.driver.find_element_by_xpath(
            '//*[@id="appointedRepresentative"]/div[1]/form/div[2]/div[3]/div[3]/div/div/div/input').send_keys(
            '上海市徐汇区锦辉大厦3')
        logger.info('输入身份证地址')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="appointedRepresentative"]/div[1]/form/div[2]/div[1]/div[3]/div/div/div[1]/div/input').send_keys(
            image_path)
        logger.info('上传财务负责人身份证人像面')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="appointedRepresentative"]/div[1]/form/div[2]/div[1]/div[3]/div/div/div[2]/div/input').send_keys(
            image_path)
        logger.info('上传身份证国徽面')
        sleep(1)

        # 添加地址
        self.driver.find_element_by_xpath('//*[@id="address"]/div[1]/div[2]/button/span').click()
        logger.info('点击添加地址')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[1]/div/div/input').send_keys('aaa')
        logger.info('填写姓名')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[2]/div/div/input').send_keys(
            18273675403)
        logger.info('填写手机号码')
        sleep(1)
        logger.info('添加省')
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[3]/div/div[1]/div[1]/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "河北省"]').click()
        sleep(1)
        logger.info('添加市')
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[3]/div/div[2]/div[1]/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "石家庄市"]').click()
        sleep(1)
        logger.info('添加区')
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[3]/div/div[3]/div[1]/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "长安区"]').click()
        sleep(1)
        logger.info('填写具体地址')
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[4]/div/div/textarea').send_keys(
            '上海市徐汇区锦辉大厦')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[5]/div/label/span[1]/span').click()
        logger.info('设为默认地址')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="address_popUp"]/div[3]/form/div[6]/div/button[1]/span').click()
        logger.info('点击确定')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="address"]/div[2]/div[3]/form/div/div/div/div/div/input').send_keys(
            '上海市徐汇区')
        logger.info('填写联系地址')
        sleep(3)
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        logger.info('下拉滚动条')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="otherInfo"]/div[1]/div[2]/div/div/input').send_keys(image_path)
        logger.info('上传委托书')
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mainContainer"]/section[9]/div/div[2]/div[1]/button[2]').click()
        logger.info('点击保存并提交')
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="mainContainer"]/section[9]/div/div[2]/div[4]/div/div[3]/span/span[1]').click()
        logger.info('点击我已知晓')
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "我已阅读并同意以上内容"]').click()
        logger.info('点击我已阅读并同意以上内容')





