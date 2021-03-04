# -*- coding:utf-8 -*-
from time import sleep
import unittest
from logs.logger import Logger
from public.hhr_mobileqiantai import WeiDian

logger = Logger(logger="Buy Product").getlog()


class Test_MobileZhifu(WeiDian):
    @unittest.skip('1')
    def test_case01(self):
        """
        官网移动在微店购买0元产品
        :return:
        """
        self.driver.find_element_by_xpath('//p[text() = "全部产品"]').click()
        logger.info('点击全部产品')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/ul/li[2]').click()
        logger.info('对价格进行升序排序')
        sleep(2)
        self.driver.find_element_by_class_name('shop-logo').click()
        logger.info('点击0元套餐')
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "立即购买"]').click()
        logger.info('点击立即购买')
        sleep(1)
        self.driver.find_element_by_xpath('//a[text() = "生成订单"]').click()
        logger.info('点击生成订单')
        sleep(1)
        self.driver.find_element_by_class_name('confirm_pay_btn').click()
        logger.info('点击立即支付')
        sleep(3)
        actual = self.driver.title
        self.assertEqual('支付成功-上海注册公司_企业服务平台_代理记账_财税服务_税务筹划_工商变更_人事社保', actual)
        logger.info('断言')
        sleep(2)

    @unittest.skip('1')
    def test_case02(self):
        """
        官网移动在微店加入购物车购买0元产品
        :return:
        """
        self.driver.find_element_by_xpath('//p[text() = "全部产品"]').click()
        logger.info('点击全部产品')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/ul/li[2]').click()
        logger.info('对价格进行升序排序')
        sleep(3)
        self.driver.find_element_by_class_name('shop-logo').click()
        logger.info('点击0元套餐')
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "加入购物车"]').click()
        logger.info('点击加入购物车')
        sleep(1)
        self.driver.find_element_by_id('check__0').click()
        logger.info('点击选择购物车产品')
        sleep(1)
        self.driver.find_element_by_xpath('//div[text() = "结算"]').click()
        logger.info('去结算')
        sleep(1)
        self.driver.find_element_by_xpath('//a[text() = "生成订单"]').click()
        logger.info('点击生成订单')
        sleep(1)
        self.driver.find_element_by_class_name('confirm_pay_btn').click()
        logger.info('点击立即支付')
        sleep(4)
        actual = self.driver.title
        self.assertEqual('支付成功-上海注册公司_企业服务平台_代理记账_财税服务_税务筹划_工商变更_人事社保', actual)
        logger.info('断言')
        sleep(2)


class WeiNotZero(WeiDian):
    @unittest.skip('1')
    def test_case01(self):
        """
        官网移动在微店使用支付宝购买非0元产品
        :return:
        """
        self.driver.find_element_by_xpath('//p[text() = "全部产品"]').click()
        logger.info('点击全部产品')
        sleep(1)
        self.driver.find_element_by_class_name('two-li').click()
        sleep(4)
        self.driver.find_element_by_class_name('two-li').click()
        sleep(2)
        logger.info('对价格进行升序排序')
        self.driver.find_element_by_class_name('shop-logo').click()
        logger.info('点击0元套餐')
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "立即购买"]').click()
        logger.info('点击立即购买')
        sleep(1)
        self.driver.find_element_by_xpath('//a[text() = "生成订单"]').click()
        logger.info('点击生成订单')
        sleep(1)
        self.driver.find_element_by_class_name('confirm_pay_btn').click()
        logger.info('点击立即支付')
        sleep(3)
        actual = self.driver.title
        self.assertEqual('支付宝', actual)
        logger.info('断言')
        sleep(2)

    def tearDown(self) -> None:
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/img').click()
        sleep(1)
        self.driver.find_element_by_class_name('to_orderCenter_btn').click()
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]/section/section/button[1]').click()
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="tabbar_4"]/p').click()
        sleep(1)
        self.driver.find_element_by_class_name('userSet').click()
        logger.info('退出登录')
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
