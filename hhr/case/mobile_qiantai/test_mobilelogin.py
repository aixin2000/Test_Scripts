# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
import unittest
from logs.logger import Logger
from tools.test_tools import Test_Tools
from public.hhr_mobileqiantai import Login

logger = Logger(logger="MobileLogin information").getlog()

a = Test_Tools()
random = a.randomPhone()


class Test_MobileLogin(Login):
    # @unittest.skip('1')
    def test_case01(self):
        """
        官网移动直客登录
        :return:
        """
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
        actual = self.driver.find_element_by_class_name('registeringMy').text
        self.assertEqual('我要注册', actual)
        logger.info('断言成功')
        sleep(1)

    # @unittest.skip('1')
    def test_case02(self):
        """
        官网移动合作商登录
        :return:
        """
        self.driver.find_element_by_class_name('login').click()
        logger.info('点击登录按钮')
        sleep(1)
        self.driver.find_element_by_xpath('//a[text() = "合作商登录>>"]').click()
        logger.info('切换到合作商登录')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[2]/div[1]/input').send_keys('ax20')
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
        actual = self.driver.find_element_by_class_name('registeringMy').text
        self.assertEqual('我要注册', actual)
        logger.info('断言成功')
        sleep(1)

    # @unittest.skip('1')
    def test_case03(self):
        """
        官网移动直客注册
        :return:
        """
        self.driver.find_element_by_class_name('registered').click()
        logger.info('点击注册按钮')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[2]/div[1]/input').send_keys(random)
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
        sleep(3)
        # actual = self.driver.title
        # self.assertEqual('禾获仁首页', actual)
        actual = self.driver.find_element_by_class_name('registeringMy').text
        self.assertEqual('我要注册', actual)
        logger.info('断言成功')
        sleep(1)


# class MobileKeFu(unittest.TestCase):
#     def setUp(self) -> None:
#         mobileEmulation = {'deviceName': 'iPhone 5'}
#         options = webdriver.ChromeOptions()
#         options.add_experimental_option('mobileEmulation', mobileEmulation)
#         self.driver = webdriver.Chrome(chrome_options=options)
#         self.driver.get('http://test3.hhrchina.com/web/mobile.html#/index')
#         self.driver.find_element_by_class_name('close-img').click()
#         self.driver.implicitly_wait(10)
#         sleep(5)
#
#     # @unittest.skip('1')
#     def test_case01(self):
#         """
#         客服登录
#         :return:
#         """
#         self.driver.find_element_by_class_name('login').click()
#         logger.info('点击登录按钮')
#         sleep(1)
#         self.driver.find_element_by_xpath('//a[text() = "合作商登录>>"]').click()
#         logger.info('切换到合作商登录')
#         sleep(1)
#         self.driver.find_element_by_xpath('//span[text() = "客服登录"]').click()
#         logger.info('切换到客服登录')
#         sleep(1)
#         self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div[2]/div[2]/div[1]/input').send_keys('ax16')
#         logger.info('输入合作商账号')
#         sleep(1)
#         self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div[2]/div[2]/div[2]/input').send_keys('a')
#         logger.info('输入客服账号')
#         sleep(1)
#         self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div[2]/div[2]/div[3]/input').send_keys('123456')
#         logger.info('输入客服登录密码')
#         sleep(2)
#         self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div[2]/div[2]/div[5]/button').click()
#         logger.info('点击登录')
#         sleep(2)
#         # self.driver.switch_to.frame('dialog')
#         # list1 = self.driver.window_handles
#         # print(list1)
#         # self.driver.switch_to.window(list1[0])
#         el = self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/button[2]')
#         if el.is_displayed() is True:
#             el.click()
#         else:
#             pass
#         sleep(4)
#         # el = self.driver.find_element_by_xpath('//span[text() = "确认"]')
#         # el.click()
#         # if el.is_displayed() is True:
#         #     el.click()
#         # sleep(2)
#         actual = self.driver.title
#         self.assertEqual('移动客服端', actual)
#         sleep(2)
#
#     def tearDown(self) -> None:
#         self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)

