# -*- coding:utf-8 -*-
import unittest
from logs.logger import Logger
from public.hhr_qiantai import Qian_Tai
from time import sleep
from tools.test_tools import Test_Tools

# 1.注册直客账号
# 2.直客/合作商登录，后台登录
# 3.注册大厅/企服商城下单
# 4.支付
a = Test_Tools()
random = a.randomPhone()
logger = Logger(logger="Login").getlog()


class Test_Login(Qian_Tai):
    # @unittest.skip('12')
    def test_case01(self):
        """注册直客账号"""
        self.driver.find_element_by_xpath('//a[text() = "登录"]').click()
        logger.info('点击登录按钮')
        self.driver.find_element_by_id('tab-register').click()
        logger.info('点击免费注册')
        self.driver.find_element_by_xpath('//*[@id="pane-register"]/form/div[1]/div/div/input').send_keys(random)
        logger.info('输入手机号码')
        # self.driver.find_element_by_name('mobilePhone').send_keys('18273675403')
        # sleep(1)
        self.driver.find_element_by_xpath('//*[@id="pane-register"]/form/div[2]/div/div/input').send_keys('hhr123456')
        logger.info('输入密码')
        self.driver.find_element_by_xpath('//*[@id="pane-register"]/form/div[3]/div/div/input').send_keys('hhr123456')
        logger.info('输入验证码')
        self.driver.find_element_by_xpath('//*[@id="pane-register"]/form/div[4]/div/div/input').send_keys('hhr123456')
        logger.info('输入短信验证码')
        self.driver.find_element_by_xpath('//*[@id="pane-register"]/form/div[5]/div/label/span[1]/span').click()
        logger.info('点击我已阅读并同意')
        self.driver.find_element_by_xpath('//*[@id="pane-register"]/form/div[6]/button').click()
        sleep(1)
        logger.info('点击同意协议并注册按钮')
        actual = self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/div[1]/div/div[2]/span/span/span').text
        self.assertEqual('{}'.format(random), actual)
        logger.info('断言')

    # @unittest.skip('12')
    def test_case02(self):
        """直客登录"""
        self.driver.find_element_by_xpath('//a[text() = "登录"]').click()
        logger.info('点击登录按钮')
        self.driver.find_element_by_xpath('//*[@id="pane-login"]/form/div[1]/div/div/input').send_keys('18273675403')
        logger.info('输入账号')
        self.driver.find_element_by_xpath('//*[@id="pane-login"]/form/div[2]/div/div/input').send_keys(
            'hhr123456')
        logger.info('输入密码')
        self.driver.find_element_by_xpath('//*[@id="pane-login"]/form/div[3]/div/div/input').send_keys('hhr123456')
        logger.info('输入验证码')
        self.driver.find_element_by_xpath('//span[text() = "登录"]').click()
        logger.info('点击登录按钮')
        sleep(1)
        actual = self.driver.find_element_by_class_name('line_vertical').text
        self.assertEqual('欢迎 18273675403 来到禾获仁！', actual)
        logger.info('断言')

    # @unittest.skip('12')
    def test_case03(self):
        """合作商登录"""
        self.driver.find_element_by_xpath('//a[text() = "合作商登录"]').click()
        logger.info('点击合作商登录按钮')
        self.driver.find_element_by_xpath('//*[@id="pane-partner"]/form/div[1]/div/div/input').send_keys('ax20')
        logger.info('输入合作商账号')
        self.driver.find_element_by_xpath('//*[@id="pane-partner"]/form/div[2]/div/div/input').send_keys('hhr123456')
        logger.info('输入密码')
        self.driver.find_element_by_xpath('//*[@id="pane-partner"]/form/div[3]/div/div/input').send_keys('hhr123456')
        logger.info('输入验证码')
        self.driver.find_element_by_xpath('//*[@id="pane-partner"]/form/div[5]/button[1]/span').click()
        logger.info('点击登录按钮')
        sleep(1)
        actual = self.driver.find_element_by_class_name('line_vertical').text
        self.assertEqual('欢迎 信息科技有限公司 来到禾获仁！', actual)
        logger.info('断言')


# class KeFuLogin(unittest.TestCase):
#     def setUp(self) -> None:
#         self.driver = webdriver.Chrome()
#         self.driver.get('http://test.hhrchina.com/')
#         self.driver.maximize_window()
#         self.driver.find_element_by_class_name('close-img').click()
#         self.driver.implicitly_wait(10)
#
#     @unittest.skip('1')
#     def test_case01(self):
#         """
#         客服登录
#         :return:
#         """
#         self.driver.find_element_by_xpath('//a[text() = "合作商登录"]').click()
#         sleep(1)
#         self.driver.find_element_by_id('tab-service').click()
#         sleep(1)
#         self.driver.find_element_by_xpath('//*[@id="pane-service"]/form/div[1]/div/div/input').send_keys('ax20')
#         sleep(1)
#         self.driver.find_element_by_xpath('//*[@id="pane-service"]/form/div[2]/div/div/input').send_keys('a')
#         sleep(1)
#         self.driver.find_element_by_xpath('//*[@id="pane-service"]/form/div[3]/div/div/input').send_keys('123456')
#         sleep(2)
#         self.driver.find_element_by_id('customerClick').click()
#         sleep(2)
#         el = self.driver.find_element_by_xpath('//span[text() = "温馨提示"]')
#         if el.is_displayed() is True:
#             self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]').click()
#         sleep(2)
#         actual = self.driver.title
#         self.assertEqual('PC客服端', actual)
#
#     def tearDown(self) -> None:
#         sleep(3)
#         self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
