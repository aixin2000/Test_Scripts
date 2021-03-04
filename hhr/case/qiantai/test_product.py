import unittest
from time import sleep
from public.hhr_qiantai import HeLogin
from logs.logger import Logger

logger = Logger(logger="product release").getlog()


class Product(HeLogin):
    @unittest.skip('1')
    def test_case01(self):
        """合作商新增企业服务类产品"""
        # 点击我的后台
        self.driver.find_element_by_xpath('//a[@href = "/customer/monthIndex.html"]').click()
        logger.info('点击我的后台')
        sleep(1)
        # 点击产品管理
        self.driver.find_element_by_xpath('//a[text()= "产品管理"]').click()
        logger.info('点击产品管理')
        sleep(1)
        # 点击新增产品
        self.driver.find_element_by_xpath('//span[text() = "+ 新增产品"]').click()
        logger.info('点击新增产品')
        sleep(1)
        # 输入产品名称
        self.driver.find_elements_by_class_name('el-input__inner')[0].send_keys('产品标题111')
        logger.info('输入产品名称')
        sleep(1)
        # 输入产品副标题
        self.driver.find_elements_by_class_name('el-input__inner')[1].send_keys('产品副标题')
        logger.info('输入产品副标题')
        sleep(1)
        # 选择一级类型
        self.driver.find_elements_by_class_name('el-input__inner')[2].click()
        # self.driver.find_element_by_xpath('//span[text() = "财税服务"]').click()
        self.driver.find_element_by_class_name('el-select-dropdown__item').click()
        logger.info('选择一级类型')
        sleep(1)
        # 选择二级类型
        self.driver.find_elements_by_class_name('el-input__inner')[3].click()
        self.driver.find_element_by_xpath('//span[text() = "代理记账"]').click()
        logger.info('选择二级类型')
        sleep(1)
        # 选择三级类型
        self.driver.find_elements_by_class_name('el-input__inner')[4].click()
        self.driver.find_element_by_xpath('//span[text() = "小规模纳税人代理记账"]').click()
        logger.info('选择三级类型')
        sleep(1)
        # 添加优势
        self.driver.find_element_by_xpath('//span[text() = "+ 添加优势"]').click()
        self.driver.find_elements_by_class_name('el-input__inner')[5].send_keys('4545')
        logger.info('添加优势')
        sleep(1)
        # 添加产品标签
        self.driver.find_elements_by_class_name('el-input__inner')[6].send_keys('wdadd')
        logger.info('添加产品标签')
        # 点击编辑服务详情
        self.driver.find_element_by_id('tab-second').click()
        logger.info('点击编辑服务详情')
        # 输入服务名称
        self.driver.find_elements_by_class_name('el-input__inner')[0].send_keys('服务名称')
        logger.info('输入服务名称')
        sleep(1)
        # 输入服务类型
        self.driver.find_elements_by_class_name('el-input__inner')[1].send_keys('服务类型')
        logger.info('输入服务类型')
        # 点击添加服务明细
        self.driver.find_element_by_xpath('//*[@id="app"]/section/section/section[3]/section/section/section/section[2]/section[1]/section[2]/button').click()
        self.driver.find_elements_by_class_name('el-input__inner')[2].send_keys('aa')
        logger.info('点击添加服务明细')
        sleep(1)
        # 输入原价
        self.driver.find_elements_by_class_name('el-input__inner')[3].send_keys(2)
        logger.info('输入原价')
        # 输入销售价
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/section/section[3]/section/section/section/section[2]/section[2]/div/div/div[2]/div[1]/div/input').send_keys(1)
        logger.info('输入销售价')
        # 价格包含
        sleep(2)
        self.driver.find_elements_by_class_name('el-input__inner')[4].send_keys('价格包含')
        logger.info('价格包含')
        # 点击填充
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/section/section[3]/section/section/section/section[2]/section[2]/div/div/button/span').click()
        logger.info('点击填充')
        # 点击编辑图文详情
        sleep(5)
        self.driver.find_element_by_id('tab-pc').click()
        logger.info('点击编辑图文详情')
        sleep(1)
        # 上传图片
        self.driver.find_element_by_xpath('//span[text() = "点击上传"]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/div[2]/div/div[2]/section[2]/ul/li[1]').click()
        logger.info('上传图片')
        # 下移
        js = "var q=document.documentElement.scrollTop=500"
        self.driver.execute_script(js)
        # 点击删除服务详情模块
        self.driver.find_element_by_xpath('//*[@id="app"]/section/section/section[3]/section/form/div[2]/div/div/div[3]/div[2]/div[2]/button/span').click()
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div[3]/button[2]/span').click()
        logger.info('点击删除服务详情模块')
        sleep(1)
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        sleep(3)
        # 删除常见问答模块
        self.driver.find_element_by_xpath('/html/body/section/section/section/section[3]/section/form/div[2]/div/div/div[5]/div[2]/div[2]/button/span').click()
        self.driver.find_element_by_xpath('/html/body/div[5]/div/div[3]/button[2]/span').click()
        logger.info('删除常见问答模块')
        # 点击下一步
        self.driver.find_element_by_xpath('//span[text() = "下一步"]').click()
        # 使用一键使用PC模板详情
        self.driver.find_element_by_xpath('//span[text() = "一键使用PC模板详情"]').click()
        sleep(2)
        logger.info('使用一键使用PC模板详情')
        # 下移
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        sleep(1)
        # 点击上架并提交审核
        self.driver.find_element_by_xpath('/html/body/section/section/section/section[3]/div/div/button[2]/span').click()
        logger.info('点击上架并提交审核')
        sleep(3)
        # 断言
        actual = self.driver.title
        self.assertEqual('产品管理', actual)
        logger.info('断言')

if __name__ == '__main__':
    unittest.main(verbosity=2)