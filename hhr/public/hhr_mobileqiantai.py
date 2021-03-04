from selenium import webdriver
import unittest
from time import sleep
from logs.logger import Logger
import os
from tools.test_tools import Test_Tools

item = Test_Tools()
items1 = item.read_config()
logger = Logger(logger="Mobile Buy Product").getlog()
executable = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/driver/chromedriver.exe'


class Login(unittest.TestCase):
    def setUp(self) -> None:
        mobileEmulation = {'deviceName': 'iPhone 5'}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(chrome_options=options, executable_path=executable)
        self.driver.get(items1['test3'])
        # self.driver.find_element_by_class_name('close-img').click()
        # logger.info('关闭弹窗')
        self.driver.implicitly_wait(10)
        sleep(2)

    def tearDown(self) -> None:
        self.driver.find_element_by_xpath('//span[text() = "我的"]').click()
        sleep(2)
        self.driver.find_element_by_class_name('userSet').click()
        sleep(2)
        self.driver.quit()


class ZhiKeLogin(unittest.TestCase):
    def setUp(self) -> None:
        mobileEmulation = {'deviceName': 'iPhone 5'}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(chrome_options=options, executable_path=executable)
        self.driver.get(items1['test'])
        # self.driver.find_element_by_class_name('close-img').click()
        # logger.info('关闭弹窗')
        self.driver.implicitly_wait(10)
        sleep(5)
        self.driver.find_element_by_class_name('login').click()
        logger.info('点击登录按钮')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[2]/div[1]/input').send_keys('18273675403')
        logger.info('输入手机号码')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[2]/div[2]/input').send_keys(
            'hhr123456')
        logger.info('输入验证码')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[2]/div[3]/input[1]').send_keys(
            'hhr123456')
        logger.info('输入手机验证码')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[2]/div[5]/button').click()
        logger.info('点击登录')
        sleep(1)

    def tearDown(self) -> None:
        self.driver.find_element_by_xpath('//span[text() = "我的"]').click()
        sleep(2)
        self.driver.find_element_by_class_name('userSet').click()
        logger.info('退出登录')
        self.driver.quit()

    def mobile_parkplayment(self, number=1):
        """
        购买园区产品
        :param number:
        :return:
        """
        self.driver.find_element_by_xpath('//span[text() = "园区服务"]').click()
        logger.info('点击园区服务')
        sleep(2)
        for i in range(number):
            self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[3]/div[1]/div/div/div[2]/div').click()
        sleep(2)
        self.driver.find_element_by_class_name('service_period').click()
        logger.info('点击0元套餐')
        sleep(1)
        self.driver.find_element_by_class_name('start_zc').click()
        logger.info('点击立即购买')
        sleep(1)
        self.driver.find_element_by_id('payDeal').click()
        logger.info('点击已阅读并同意《用户服务协议》')
        sleep(1)
        self.driver.find_element_by_xpath('//a[text() = "生成订单"]').click()
        logger.info('点击生成订单')
        sleep(1)
        self.driver.find_element_by_class_name('confirm_pay_btn').click()
        logger.info('点击立即支付')
        sleep(3)

    def mobile_playment(self, number=1):
        """
        购买企服产品
        :param number:
        :return:
        """
        self.driver.find_element_by_class_name('icon-tab5').click()
        logger.info('点击企服商城')
        sleep(1)
        self.driver.find_element_by_xpath('//p[text() = "知识产权"]').click()
        logger.info('点击知识产权')
        sleep(1)
        for i in range(number):
            self.driver.find_element_by_class_name('two-li').click()
        logger.info('点击价格升序显示')
        sleep(1)
        self.driver.find_element_by_class_name('shop-logo').click()
        logger.info('点击套餐')
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "立即购买"]').click()
        logger.info('点击立即购买')
        sleep(4)
        self.driver.find_element_by_xpath('//a[text() = "生成订单"]').click()
        logger.info('点击生成订单')
        sleep(2)
        self.driver.find_element_by_class_name('confirm_pay_btn').click()
        logger.info('点击立即支付')
        sleep(2)

    def mobile_add_shopping(self):
        """
        添加园区产品到购物车结算
        :return:
        """
        self.driver.find_element_by_xpath('//span[text() = "园区服务"]').click()
        logger.info('点击园区服务')
        sleep(1)
        for i in range(2):
            self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[3]/div[1]/div/div/div[2]/div').click()
            sleep(1)
        sleep(1)
        self.driver.find_element_by_class_name('service_period').click()
        logger.info('点击0元套餐')
        sleep(1)
        self.driver.find_element_by_class_name('put_into_cart').click()
        logger.info('点击加入购物车')
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "购物车"]').click()
        logger.info('点击购物车按钮')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div[1]/div[1]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div/i').click()
        logger.info('点击选择购物车产品')
        sleep(1)
        self.driver.find_element_by_class_name('span-btn').click()
        logger.info('去结算')
        sleep(1)
        self.driver.find_element_by_id('payDeal').click()
        logger.info('点击已阅读并同意《用户服务协议》')
        sleep(1)
        self.driver.find_element_by_xpath('//a[text() = "生成订单"]').click()
        logger.info('点击生成订单')
        sleep(1)
        self.driver.find_element_by_class_name('confirm_pay_btn').click()
        logger.info('点击立即支付')
        sleep(3)

    def mobile_qifuadd_shopping(self):
        """
        添加企服产品到购物车结算
        :return:
        """
        self.driver.find_element_by_class_name('icon-tab5').click()
        logger.info('点击企服商城')
        sleep(1)
        self.driver.find_element_by_xpath('//p[text() = "知识产权"]').click()
        logger.info('点击知识产权')
        sleep(1)
        self.driver.find_element_by_class_name('two-li').click()
        logger.info('点击价格升序显示')
        sleep(1)
        self.driver.find_element_by_class_name('shop-logo').click()
        logger.info('点击0元套餐')
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "加入购物车"]').click()
        logger.info('点击加入购物车')
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "购物车"]').click()
        logger.info('点击购物车按钮')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div[1]/div[1]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div/i').click()
        logger.info('点击选择购物车产品')
        sleep(4)
        self.driver.find_element_by_class_name('span-btn').click()
        logger.info('去结算')
        sleep(4)
        self.driver.find_element_by_xpath('//a[text() = "生成订单"]').click()
        logger.info('点击生成订单')
        sleep(2)
        self.driver.find_element_by_class_name('confirm_pay_btn').click()
        logger.info('点击立即支付')
        sleep(4)

class HeLogin(unittest.TestCase):
    def setUp(self) -> None:
        mobileEmulation = {'deviceName': 'iPhone 5'}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(chrome_options=options, executable_path=executable)
        self.driver.get(items1['test3'])
        self.driver.maximize_window()
        # self.driver.find_element_by_class_name('close-img').click()
        # logger.info('关闭弹窗')
        self.driver.implicitly_wait(10)
        sleep(5)
        self.driver.find_element_by_class_name('login').click()
        logger.info('点击登录按钮')
        sleep(1)
        self.driver.find_element_by_xpath('//a[text() = "合作商登录>>"]').click()
        logger.info('切换到合作商登录')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[2]/div[1]/input').send_keys('liuhan')
        logger.info('输入合作商账号')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[2]/div[2]/input').send_keys('hhr123456')
        logger.info('输入密码')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[2]/div[3]/input').send_keys(
            'hhr123456')
        logger.info('输入验证码')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[2]/div[5]/button').click()
        logger.info('点击登录')
        sleep(1)

    def tearDown(self) -> None:
        self.driver.find_element_by_xpath('//span[text() = "我的"]').click()
        sleep(2)
        self.driver.find_element_by_class_name('userSet').click()
        logger.info('退出登录')
        self.driver.quit()

    def mobile_heparkplayment(self, number=1):
        """
        购买园区产品
        :param number:
        :return:
        """
        self.driver.find_element_by_xpath('//span[text() = "园区服务"]').click()
        logger.info('点击园区服务')
        sleep(2)
        for i in range(number):
            self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[3]/div[1]/div/div/div[2]/div').click()
        sleep(2)
        self.driver.find_element_by_class_name('service_period').click()
        logger.info('点击0元套餐')
        sleep(1)
        self.driver.find_element_by_class_name('start_zc').click()
        logger.info('点击立即购买')
        sleep(1)
        self.driver.find_element_by_id('payDeal').click()
        logger.info('点击已阅读并同意《用户服务协议》')
        sleep(1)
        self.driver.find_element_by_xpath('//a[text() = "生成订单"]').click()
        logger.info('点击生成订单')
        sleep(1)
        self.driver.find_element_by_class_name('confirm_pay_btn').click()
        logger.info('点击立即支付')
        sleep(3)

    def mobile_heplayment(self, number=1):
        """
        购买企服产品
        :param number:
        :return:
        """
        self.driver.find_element_by_class_name('icon-tab5').click()
        logger.info('点击企服商城')
        sleep(1)
        self.driver.find_element_by_xpath('//p[text() = "知识产权"]').click()
        logger.info('点击知识产权')
        sleep(1)
        for i in range(number):
            self.driver.find_element_by_class_name('two-li').click()
        logger.info('点击价格升序显示')
        sleep(1)
        self.driver.find_element_by_class_name('shop-logo').click()
        logger.info('点击套餐')
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "立即购买"]').click()
        logger.info('点击立即购买')
        sleep(4)
        self.driver.find_element_by_xpath('//a[text() = "生成订单"]').click()
        logger.info('点击生成订单')
        sleep(2)
        self.driver.find_element_by_class_name('confirm_pay_btn').click()
        logger.info('点击立即支付')
        sleep(2)

    def mobile_headd_shopping(self):
        """
        添加园区产品到购物车结算
        :return:
        """
        self.driver.find_element_by_xpath('//span[text() = "园区服务"]').click()
        logger.info('点击园区服务')
        sleep(1)
        for i in range(2):
            self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[3]/div[1]/div/div/div[2]/div').click()
            sleep(1)
        sleep(1)
        self.driver.find_element_by_class_name('service_period').click()
        logger.info('点击0元套餐')
        sleep(1)
        self.driver.find_element_by_class_name('put_into_cart').click()
        logger.info('点击加入购物车')
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "购物车"]').click()
        logger.info('点击购物车按钮')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div[1]/div[1]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div/i').click()
        logger.info('点击选择购物车产品')
        sleep(1)
        self.driver.find_element_by_class_name('span-btn').click()
        logger.info('去结算')
        sleep(1)
        self.driver.find_element_by_id('payDeal').click()
        logger.info('点击已阅读并同意《用户服务协议》')
        sleep(1)
        self.driver.find_element_by_xpath('//a[text() = "生成订单"]').click()
        logger.info('点击生成订单')
        sleep(1)
        self.driver.find_element_by_class_name('confirm_pay_btn').click()
        logger.info('点击立即支付')
        sleep(3)

    def mobile_heqifuadd_shopping(self):
        """
        添加企服产品到购物车结算
        :return:
        """
        self.driver.find_element_by_class_name('icon-tab5').click()
        logger.info('点击企服商城')
        sleep(1)
        self.driver.find_element_by_xpath('//p[text() = "知识产权"]').click()
        logger.info('点击知识产权')
        sleep(1)
        self.driver.find_element_by_class_name('two-li').click()
        logger.info('点击价格升序显示')
        sleep(1)
        self.driver.find_element_by_class_name('shop-logo').click()
        logger.info('点击0元套餐')
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "加入购物车"]').click()
        logger.info('点击加入购物车')
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "购物车"]').click()
        logger.info('点击购物车按钮')
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div[1]/div[1]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div/i').click()
        logger.info('点击选择购物车产品')
        sleep(4)
        self.driver.find_element_by_class_name('span-btn').click()
        logger.info('去结算')
        sleep(4)
        self.driver.find_element_by_xpath('//a[text() = "生成订单"]').click()
        logger.info('点击生成订单')
        sleep(2)
        self.driver.find_element_by_class_name('confirm_pay_btn').click()
        logger.info('点击立即支付')
        sleep(4)


class WeiDian(unittest.TestCase):
    def setUp(self) -> None:
        mobileEmulation = {'deviceName': 'iPhone 5'}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        self.driver = webdriver.Chrome(chrome_options=options, executable_path=executable)
        self.driver.get(items1['weidian'])
        self.driver.implicitly_wait(10)
        sleep(2)
        self.driver.find_element_by_class_name('close-img').click()
        sleep(1)
        self.driver.find_element_by_xpath('//p[text() = "我的"]').click()
        logger.info('点击我的')
        sleep(1)
        self.driver.find_element_by_class_name('loginBtn').click()
        logger.info('点击账号登录')
        sleep(1)
        self.driver.find_element_by_xpath('//input[@placeholder = "请输入您的手机号"]').send_keys('15608449287')
        logger.info('输入手机号码')
        sleep(1)
        self.driver.find_element_by_xpath('//input[@placeholder = "请输入右侧验证码"]').send_keys(
            'hhr123456')
        logger.info('输入验证码')
        sleep(1)
        self.driver.find_element_by_xpath('//input[@placeholder = "请输入手机验证码"]').send_keys(
            'hhr123456')
        logger.info('输入手机验证码')
        sleep(2)
        self.driver.find_element_by_class_name('mobile-inp-btn').click()
        logger.info('点击登录')
        sleep(2)

    def tearDown(self) -> None:
        self.driver.find_element_by_xpath('//div[text() = "订单中心"]').click()
        logger.info('点击订单中心')
        sleep(1)
        self.driver.find_element_by_xpath('//p[text() = "我的"]').click()
        sleep(1)
        self.driver.find_element_by_class_name('userSet').click()
        sleep(2)
        logger.info('退出登录')
        self.driver.quit()









