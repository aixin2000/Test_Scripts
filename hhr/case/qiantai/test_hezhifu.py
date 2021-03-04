# -*- coding:utf-8 -*-
import unittest
from time import sleep
from public.hhr_qiantai import ZhiKeLogin, HeLogin, WeiDian

from logs.logger import Logger

logger = Logger(logger="hezuoshang Product").getlog()


class HeZuoShanPlay(HeLogin):
    # @unittest.skip('1')
    def test_case01(self):
        """合作商注册大厅购买0元产品"""
        self.select_park_service()
        self.driver.find_element_by_class_name('indent-total-button').click()
        logger.info('点击支付')
        sleep(2)
        actual = self.driver.title
        sleep(2)
        self.assertEqual('购买成功', actual)
        logger.info('断言')

    # @unittest.skip('11')
    def test_case02(self):
        """合作商注册大厅使用微信购买非0元产品"""
        self.select_park_service(1, 1000)
        self.driver.find_element_by_class_name('indent-total-button').click()
        logger.info('点击立即支付')
        sleep(3)
        actual = self.driver.find_element_by_class_name('pay-way-title')
        self.assertTrue(actual)
        logger.info('断言')

    # @unittest.skip('11')
    def test_case03(self):
        """合作商注册大厅使用支付宝购买非0元产品"""
        self.select_park_service(1, 10000)
        self.driver.find_element_by_xpath('//*[@id="indent"]/div/div/ul/li[2]').click()
        logger.info('使用支付宝支付')
        sleep(2)
        self.driver.find_element_by_class_name('indent-total-button').click()
        logger.info('点击支付')
        sleep(2)
        actual = self.driver.find_element_by_class_name('ft-center').text
        sleep(1)
        self.assertEqual('扫一扫付款（元）', actual)
        logger.info('断言')
         
        self.driver.back()
        logger.info('回退')

    @unittest.skip('a')
    def test_case04(self):
        """合作商注册大厅使用余额支付购买非0元产品"""
        self.select_park_service(1, 10000)
        self.driver.find_element_by_xpath('//*[@id="indent"]/div/div/ul/li[3]').click()
        logger.info('使用余额支付')
        sleep(1)
        self.driver.find_element_by_class_name('indent-total-button').click()
        logger.info('点击支付')
        self.driver.find_element_by_id('getPhoneCodeBtn').click()
        logger.info('点击发送验证码')
        self.driver.find_element_by_xpath('//*[@id="mainCon"]/section/div/div/input').send_keys('hhrChina20151022')
        self.driver.find_element_by_class_name('pay-confirm').click()
        logger.info('点击支付')

    # @unittest.skip('1')
    def test_case05(self):
        """合作商企服商城购买0元产品"""
        self.select_enterprise_service()
        self.driver.find_element_by_class_name('indent-total-button').click()
        logger.info('点击立即支付')
        sleep(3)
        actual = self.driver.title
        self.assertEqual('购买成功', actual)

    # @unittest.skip('1')
    def test_case06(self):
        """合作商企服商城使用微信购买非0元产品"""
        self.select_enterprise_service(1, 10000)
        self.driver.find_element_by_class_name('indent-total-button').click()
        logger.info('点击立即支付')
        sleep(3)
        actual = self.driver.find_element_by_class_name('pay-way-title')
        self.assertTrue(actual)
        logger.info('断言')

    # @unittest.skip('1')
    def test_case07(self):
        """合作商企服商城使用支付宝购买非0元产品"""
        self.select_enterprise_service(1, 10000)
        self.driver.find_element_by_xpath('//*[@id="indent"]/div/div/ul/li[2]').click()
        logger.info('使用支付宝支付')
        self.driver.find_element_by_class_name('indent-total-button').click()
        logger.info('点击立即支付')
        actual = self.driver.find_element_by_class_name('ft-center').text
        self.assertEqual('扫一扫付款（元）', actual)
        logger.info('断言')
        self.driver.back()
        logger.info('回退')

    @unittest.skip('1')
    def test_case08(self):
        """合作商企服商城使用余额支付购买非0元产品"""
        self.select_enterprise_service(1, 10000)
        self.driver.find_element_by_xpath('//*[@id="indent"]/div/div/ul/li[3]').click()
        logger.info('使用余额支付')
        self.driver.find_element_by_class_name('indent-total-button').click()
        logger.info('点击支付')
        self.driver.find_element_by_id('getPhoneCodeBtn').click()
        logger.info('点击发送验证码')
        self.driver.find_element_by_xpath('//*[@id="mainCon"]/section/div/div/input').send_keys('hhrChina20151022')
        sleep(1)
        self.driver.find_element_by_class_name('pay-confirm').click()
        logger.info('点击支付')

    @unittest.skip('1')
    def test_case09(self):
        """合作商注册大厅加入购物车去结算"""
        self.driver.find_element_by_class_name('registrationWords').click()
        logger.info('点击注册类型')
        list1 = self.driver.window_handles
        self.driver.switch_to.window(list1[1])
        logger.info('切换窗口')
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[8]/div[2]/div[8]/div[1]/input').send_keys(0)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[4]/div[8]/div[2]/div[8]/div[2]/input').send_keys(0)
        logger.info('输入价格范围')
        self.driver.find_element_by_class_name('price_btn').click()
        logger.info('点击确定')
        self.driver.find_element_by_class_name('card-tit1').click()
        # self.driver.find_element_by_xpath('//li[text()="直客产品新增lala "]').click()
        logger.info('点击一个直客产品')
        list1 = self.driver.window_handles
        self.driver.switch_to.window(list1[2])
        logger.info('切换窗口')
        self.driver.find_element_by_xpath('//a[text() = "加入购物车"]').click()
        logger.info('加入购物车')
        self.driver.find_element_by_xpath('//a[text() = "去购物车结算"]').click()
        logger.info('去购物车结算')
        self.driver.find_element_by_name('goodRadio').click()
        logger.info('点击选择产品')
        self.driver.find_element_by_id('sub').click()
        logger.info('去结算')
        self.driver.find_element_by_id('dealTxt').click()
        logger.info('已阅读并同意《用户服务协议》')
        self.driver.find_element_by_class_name('indent-total-button').click()
        logger.info('点击生成订单')
        sleep(1)
        self.driver.find_element_by_class_name('indent-total-button').click()
        logger.info('点击立即支付')
        sleep(3)
        actual = self.driver.title
        self.assertEqual('购买成功', actual)
        logger.info('断言')

    @unittest.skip('1')
    def test_case10(self):
        """合作商企服商城加入购物车去结算"""
        self.driver.find_element_by_id('nav_item_serviceMall').click()
        logger.info('点击企服商城')
         
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)
        sleep(2)
        self.driver.find_element_by_xpath('//a[text() = "更多 >"]').click()
        logger.info('点击更多')
         
        list1 = self.driver.window_handles
        self.driver.switch_to.window(list1[1])
        logger.info('切换窗口')
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[2]/section[1]/div[2]/ul/li[7]/input').send_keys(0)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[2]/section[1]/div[2]/ul/li[8]/input').send_keys(0)
        logger.info('输入价格范围')
         
        self.driver.find_element_by_class_name('certainBtn').click()
        logger.info('点击确定')
         
        self.driver.find_element_by_class_name('headline').click()
        logger.info('点击一个企服商城产品')
        sleep(2)
        list2 = self.driver.window_handles
        self.driver.switch_to.window(list2[2])
        logger.info('切换窗口')
        sleep(2)
        self.driver.find_element_by_class_name('btn2').click()
        logger.info('加入购物车')
         
        self.driver.find_element_by_xpath('//span[text() = "去购物车结算"]').click()
        logger.info('去购物车结算')
        list3 = self.driver.window_handles
        self.driver.switch_to.window(list3[3])
        logger.info('切换窗口')
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/div/div/div[3]/div[1]/div[2]/div/div[1]/div/div[1]/label/span/span').click()
        logger.info('选中一个产品')
        self.driver.find_element_by_class_name('settlement-btn').click()
        logger.info('去结算')
         
        self.driver.find_element_by_xpath('//button[text()="生成订单"]').click()
        logger.info('点击生成订单')
        # 点击立即支付
        sleep(2)
        self.driver.find_element_by_class_name('indent-total-button').click()
        logger.info('点击立即支付')
        # 断言
        sleep(3)
        actual = self.driver.title
        self.assertEqual('购买成功', actual)
         
        logger.info('断言')


    @unittest.skip('11')
    def test_case11(self):
        """在微店购买产品"""
        # 点击我的后台
        self.driver.find_element_by_xpath('//a[@href = "/customer/monthIndex.html"]').click()
         
        # 点击微商城定制
        self.driver.find_element_by_xpath('//a[@href = "/monthUserCenter/toBrandCustomization.html"]').click()
         
        # 点击预览微商城
        self.driver.find_element_by_class_name('previewBtn').click()
         
        # 切换句柄
        list1 = self.driver.window_handles
        self.driver.switch_to.window(list1[1])
        # 登录账号
         
        self.driver.find_element_by_class_name('loginBtn').click()
         
        self.driver.find_element_by_name('mobilePhone').send_keys('18273675403')
         
        self.driver.find_element_by_name('password').send_keys('aixin96177520000')
         
        self.driver.find_element_by_name('code').send_keys('hhrChina20151022')
         
        self.driver.find_element_by_class_name('passwordLogin').click()

        # 选择一个产品进入产品详情页
        self.driver.find_element_by_xpath('//p[text() = "个人独资企业注册"]').click()
         
        list2 = self.driver.window_handles
        self.driver.switch_to.window(list2[2])
        # 点击立即购买
        self.driver.find_element_by_class_name('btn1').click()

        # 点击生成订单
         
        self.driver.find_element_by_xpath('//button[text()="生成订单"]').click()
        # 点击立即支付
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div[1]/ul/button').click()
        # 断言
        sleep(2)
        actual = self.driver.title
        self.assertEqual('购买成功', actual)


if __name__ == '__main__':
    unittest.main(verbosity=2)

