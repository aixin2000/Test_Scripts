# -*- coding:utf-8 -*-
from time import sleep
import unittest
from logs.logger import Logger
from public.hhr_mobileqiantai import MobileReg
from selenium.webdriver.common.touch_actions import TouchActions

logger = Logger(logger="Buy Product").getlog()


class Test_MobileZhifu(MobileReg):
    @unittest.skip('1')
    def test_case01(self):
        """
        官网移动直客购买园区服务0元套餐
        :return:
        """
        # self.driver.find_element_by_xpath('//p[text() = "园区服务"]').click()
        # logger.info('点击园区服务')
        # sleep(3)
        # self.driver.find_element_by_class_name('serviceMall_top_menu').click()
        # logger.info('点击筛选按钮')
        # sleep(1)
        # self.driver.find_element_by_xpath('//a[text() = "有限公司注册"]').click()
        # logger.info('点击有限公司注册')
        # sleep(1)
        # self.driver.find_element_by_class_name('filter_item_inpo').send_keys(0)
        # sleep(1)
        # self.driver.find_element_by_class_name('filter_item_inpt').send_keys(0)
        # logger.info('进行0-0条件筛选')
        # self.driver.find_element_by_xpath('//button[text() = "确定"]').click()
        # logger.info('点击确定')
        # sleep(1)
        # self.driver.find_element_by_class_name('service_period').click()
        # logger.info('点击0元套餐')
        # sleep(1)
        # self.driver.find_element_by_class_name('start_zc').click()
        # logger.info('点击立即购买')
        # sleep(1)
        # self.driver.find_element_by_id('payDeal').click()
        # logger.info('点击已阅读并同意《用户服务协议》')
        # sleep(1)
        # self.driver.find_element_by_xpath('//a[text() = "生成订单"]').click()
        # logger.info('点击生成订单')
        # sleep(1)
        # self.driver.find_element_by_class_name('confirm_pay_btn').click()
        # logger.info('点击立即支付')
        # sleep(3)
        # self.driver.find_element_by_xpath('//a[@href = "/mobile/myCompany.html"]').click()
        # logger.info('进入企业管理')
        # sleep(1)
        # self.driver.find_element_by_class_name('blue_btn').click()
        # logger.info('点击填写注册资料')
        # sleep(1)
        self.driver.find_element_by_xpath('//*[@id="tabbar_4"]/p').click()
        logger.info('点击我的')
        sleep(1)
        self.driver.find_element_by_xpath('//p[text() = "我的服务"]').click()
        logger.info('点击我的服务')
        sleep(1)
        self.driver.find_element_by_class_name('blue_btn').click()
        logger.info('点击填写注册资料')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/div[2]/div/div/div/input').send_keys(100)
        logger.info('填写注册资金')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[3]').click()
        logger.info('选择公司名称')
        sleep(10)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div/div').click()
        logger.info('+选择行业名称')
        sleep(1)
        self.driver.find_element_by_class_name('sort').click()
        logger.info('选择信息科技')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div/input').send_keys('发我')
        logger.info('选择第一个公司名称')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[2]/div[2]/div[1]/div[1]/div[2]/div/input').send_keys('安静')
        logger.info('选择第二个公司名称')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[2]/div[3]/div[1]/div[1]/div[2]/div/input').send_keys('谷歌')
        logger.info('选择第三个公司名称')
        sleep(1)
        self.driver.find_element_by_class_name('van-button__text').click()
        logger.info('点击保存')
        sleep(1)

        # 添加股东信息
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]').click()
        logger.info('点击股东详情')
        sleep(5)
        self.driver.find_element_by_class_name('shareholder_btn').click()
        logger.info('添加股东消息')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[4]/div/div/div/div[1]/div/div/div/input').send_keys(r'D:\python_workspace\PROJECT\hhr\image\1.jpg')
        logger.info('上传股东身份证人像面')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[4]/div/div/div/div[2]/div/div/div/input').send_keys(r'D:\python_workspace\PROJECT\hhr\image\1.jpg')
        logger.info('上传股东身份证国徽面')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[5]/div[1]/div[2]/div/input').send_keys('贺剑')
        logger.info('输入股东姓名')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[5]/div[2]/div[2]/div/input').send_keys('15623254787')
        logger.info('输入联系电话')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[5]/div[3]/div[2]/div/input').send_keys(100)
        logger.info('输入出资比例')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[5]/div[4]/div[2]/div/input').send_keys(430407199810082819)
        logger.info('输入身份证号码')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div[5]/div[5]/div/div/div[1]/div/div/input').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/button[2]').click()
        logger.info('输入开始日期')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[5]/div[5]/div/div/div[2]/div/div/input').click()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/button[2]').click()
        logger.info('输入结束日期')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[5]/div[6]/div[2]/div/textarea').send_keys('上海市锦辉大厦')
        logger.info('输入身份证号码')
        sleep(1)
        self.driver.find_element_by_xpath('//div[text() = "保存"]').click()
        sleep(1)


if __name__ == '__main__':
    unittest.main(verbosity=2)








