import unittest
from time import sleep
from public.hhr_qiantai import WeiDian

from logs.logger import Logger

logger = Logger(logger="Buy Product").getlog()


class Wei(WeiDian):
    @unittest.skip('aa')
    def test_case01(self):
        """在微店购买0元产品"""
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="serviceAll"]/div/section[1]/div[2]/ul/li[7]/input').click()
        self.driver.find_element_by_xpath('//*[@id="serviceAll"]/div/section[1]/div[2]/ul/li[7]/input').send_keys(0)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="serviceAll"]/div/section[1]/div[2]/ul/li[8]/input').click()
        self.driver.find_element_by_xpath('//*[@id="serviceAll"]/div/section[1]/div[2]/ul/li[8]/input').send_keys(0)
        sleep(2)
        self.driver.find_element_by_class_name('certainBtn').click()
        sleep(2)
        # 选择一个产品进入产品详情页
        # self.driver.find_element_by_xpath('//p[text() = "个人独资企业注册"]').click()
        # logger.info('点击个人独资企业注册产品')
        self.driver.find_element_by_class_name('subtitle').click()
        sleep(2)
        # list2 = self.driver.window_handles
        # self.driver.switch_to.window(list2[1])
        # logger.info('切换窗口')
        # 点击立即购买
        self.driver.find_element_by_class_name('btn1').click()
        logger.info('点击立即购买')
        # 点击生成订单
        sleep(1)
        self.driver.find_element_by_xpath('//button[text()="生成订单"]').click()
        logger.info('点击生成订单')
        # 点击立即支付
        sleep(5)
        self.driver.find_element_by_class_name('indent-total-button').click()
        logger.info('点击立即支付')
        # 断言
        sleep(5)
        actual = self.driver.title
        self.assertEqual('购买成功', actual)
        sleep(3)
        logger.info('断言')

    @unittest.skip('11')
    def test_case02(self):
        """在微店使用微信购买非0元产品"""
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="serviceAll"]/div/section[1]/div[2]/ul/li[7]/input').click()
        self.driver.find_element_by_xpath('//*[@id="serviceAll"]/div/section[1]/div[2]/ul/li[7]/input').send_keys(1)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="serviceAll"]/div/section[1]/div[2]/ul/li[8]/input').click()
        self.driver.find_element_by_xpath('//*[@id="serviceAll"]/div/section[1]/div[2]/ul/li[8]/input').send_keys(10000)
        sleep(1)
        self.driver.find_element_by_class_name('certainBtn').click()
        sleep(4)
        self.driver.find_element_by_class_name('subtitle').click()
        # self.driver.find_element_by_xpath('//p[text() = "产品标题111"]').click()
        # logger.info('点击产品标题111产品')
        # sleep(1)
        # list2 = self.driver.window_handles
        # self.driver.switch_to.window(list2[1])
        # logger.info('切换窗口')
        # 点击立即购买
        sleep(4)
        self.driver.find_element_by_class_name('btn1').click()
        logger.info('点击立即购买')
        # 点击生成订单
        sleep(2)
        self.driver.find_element_by_xpath('//button[text()="生成订单"]').click()
        logger.info('点击生成订单')
        # 点击立即支付
        sleep(4)
        self.driver.find_element_by_class_name('indent-total-button').click()
        logger.info('点击立即支付')
        sleep(4)
        # 断言
        actual = self.driver.find_element_by_class_name('pay-way-title')
        self.assertTrue(actual)
        sleep(3)
        logger.info('断言')

    @unittest.skip('11')
    def test_case03(self):
        """在微店使用支付宝购买非0元产品"""
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="serviceAll"]/div/section[1]/div[2]/ul/li[7]/input').click()
        self.driver.find_element_by_xpath('//*[@id="serviceAll"]/div/section[1]/div[2]/ul/li[7]/input').send_keys(1)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="serviceAll"]/div/section[1]/div[2]/ul/li[8]/input').click()
        self.driver.find_element_by_xpath('//*[@id="serviceAll"]/div/section[1]/div[2]/ul/li[8]/input').send_keys(10000)
        sleep(2)
        self.driver.find_element_by_class_name('certainBtn').click()
        sleep(4)
        self.driver.find_element_by_class_name('subtitle').click()
        # self.driver.find_element_by_xpath('//p[text() = "产品标题111"]').click()
        # logger.info('点击产品标题111产品')
        # sleep(1)
        # list2 = self.driver.window_handles
        # self.driver.switch_to.window(list2[1])
        # logger.info('切换窗口')
        # 点击立即购买
        sleep(4)
        self.driver.find_element_by_class_name('btn1').click()
        logger.info('点击立即购买')
        # 点击生成订单
        sleep(2)
        self.driver.find_element_by_xpath('//button[text()="生成订单"]').click()
        logger.info('点击生成订单')
        # 点击立即支付
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="indent"]/div/div/ul/li[2]').click()
        logger.info('使用支付宝支付')
        sleep(1)
        self.driver.find_element_by_class_name('indent-total-button').click()
        logger.info('点击支付')
        sleep(3)
        actual = self.driver.find_element_by_class_name('ft-center').text
        self.assertEqual('扫一扫付款（元）', actual)
        sleep(3)
        logger.info('断言')
        sleep(1)
        self.driver.back()
        logger.info('回退')

    @unittest.skip('1')
    def test_case04(self):
        """微店产品加入购物车去结算"""
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="serviceAll"]/div/section[1]/div[2]/ul/li[7]/input').click()
        self.driver.find_element_by_xpath('//*[@id="serviceAll"]/div/section[1]/div[2]/ul/li[7]/input').send_keys(0)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="serviceAll"]/div/section[1]/div[2]/ul/li[8]/input').click()
        self.driver.find_element_by_xpath('//*[@id="serviceAll"]/div/section[1]/div[2]/ul/li[8]/input').send_keys(0)
        sleep(1)
        self.driver.find_element_by_class_name('certainBtn').click()
        sleep(2)
        # 选择一个产品进入产品详情页
        # self.driver.find_element_by_xpath('//p[text() = "个人独资企业注册"]').click()
        # logger.info('点击个人独资企业注册产品')
        self.driver.find_element_by_class_name('subtitle').click()
        # 选择一个产品进入产品详情页
        # self.driver.find_element_by_xpath('//p[text() = "个人独资企业注册"]').click()
        # logger.info('点击个人独资企业注册产品')
        # sleep(1)
        # list2 = self.driver.window_handles
        # self.driver.switch_to.window(list2[1])
        # logger.info('切换窗口')
        sleep(2)
        self.driver.find_element_by_class_name('btn2').click()
        logger.info('加入购物车')
        sleep(1)
        self.driver.find_element_by_xpath('//a[@href = "/shoppingcart.html"]').click()
        logger.info('去购物车结算')
        sleep(1)
        self.driver.find_element_by_name('goodRadio').click()
        logger.info('选中一个产品')
        sleep(1)
        self.driver.find_element_by_id('sub').click()
        logger.info('去结算')
        sleep(1)
        self.driver.find_element_by_xpath('//button[text()="生成订单"]').click()
        logger.info('点击生成订单')
        # 点击立即支付
        sleep(4)
        self.driver.find_element_by_class_name('indent-total-button').click()
        logger.info('点击立即支付')
        # 断言
        sleep(4)
        actual = self.driver.title
        self.assertEqual('购买成功', actual)
        sleep(1)
        logger.info('断言')
        sleep(2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
