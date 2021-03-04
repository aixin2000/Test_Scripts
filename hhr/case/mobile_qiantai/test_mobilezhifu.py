# -*- coding:utf-8 -*-
from time import sleep
import unittest
from logs.logger import Logger
from public.hhr_mobileqiantai import ZhiKeLogin

logger = Logger(logger="MobileZhike Product").getlog()


class Test_MobileZhifu(ZhiKeLogin):
    @unittest.skip('1')
    def test_case01(self):
        """
        官网移动直客购买园区服务0元套餐
        :return:
        """
        self.mobile_parkplayment(2)
        actual = self.driver.title
        self.assertEqual('支付成功-上海注册公司_企业服务平台_代理记账_财税服务_税务筹划_工商变更_人事社保', actual)
        logger.info('断言')
        sleep(1)
        self.driver.find_element_by_xpath('//a[text() = "订单中心"]').click()
        sleep(1)

    @unittest.skip('1')
    def test_case02(self):
        """
        官网移动直客园区服务0元套餐加入购物车进行购买
        :return:
        """
        self.mobile_add_shopping()
        actual = self.driver.title
        self.assertEqual('支付成功-上海注册公司_企业服务平台_代理记账_财税服务_税务筹划_工商变更_人事社保', actual)
        logger.info('断言')
        sleep(2)
        self.driver.find_element_by_xpath('//a[text() = "订单中心"]').click()
        sleep(1)

    @unittest.skip('1')
    def test_case03(self):
        """
        官网移动直客购买企服商城0元套餐
        :return:
        """
        self.mobile_playment()
        actual = self.driver.title
        sleep(1)
        self.assertEqual('支付成功-上海注册公司_企业服务平台_代理记账_财税服务_税务筹划_工商变更_人事社保', actual)
        logger.info('断言')
        sleep(2)
        self.driver.find_element_by_xpath('//a[text() = "订单中心"]').click()
        sleep(1)

    @unittest.skip('1')
    def test_case04(self):
        """
        官网移动直客企服商城0元套餐加入购物车进行购买
        :return:
        """
        self.mobile_qifuadd_shopping()
        actual = self.driver.title
        self.assertEqual('支付成功-上海注册公司_企业服务平台_代理记账_财税服务_税务筹划_工商变更_人事社保', actual)
        logger.info('断言')
        sleep(2)
        self.driver.find_element_by_xpath('//a[text() = "订单中心"]').click()
        sleep(1)

    @unittest.skip('1')
    def test_case05(self):
        """
        官网移动直客购买企服商城非0元套餐
        :return:
        """
        self.mobile_playment()
        actual = self.driver.title
        self.assertEqual('支付宝', actual)
        logger.info('断言成功')
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/img').click()
        sleep(1)
        self.driver.find_element_by_class_name('to_orderCenter_btn').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]/section/section/button[1]').click()
        sleep(2)

    @unittest.skip('1')
    def test_case06(self):
        """
        官网移动直客购买园区服务非0元套餐
        :return:
        """
        self.mobile_parkplayment(2)
        actual = self.driver.title
        self.assertEqual('支付宝', actual)
        logger.info('断言成功')
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/img').click()
        sleep(1)
        self.driver.find_element_by_class_name('to_orderCenter_btn').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]/section/section/button[1]').click()
        sleep(1)


if __name__ == '__main__':
    unittest.main(verbosity=2)

