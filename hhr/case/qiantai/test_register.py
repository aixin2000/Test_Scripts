# -*- coding:utf-8 -*-
from public.hhr_qiantai import *
from tools.test_tools import Test_Tools
from logs.logger import Logger

logger = Logger(logger="Submit information").getlog()


a = Test_Tools()


class Register(ZhiKeLogin):
    # @unittest.skip('1')
    def test_case01(self):
        """直客购买有限注册提交资料"""
        self.limited_company_submitting_information()
        actual = self.driver.find_element_by_class_name('el-input__inner').is_enabled()
        self.assertTrue(actual)
        logger.info('断言')

    # @unittest.skip('1')
    def test_case02(self):
        """直客购买有限合伙注册提交资料"""
        self.limited_partnership_submission()
        actual = self.driver.find_element_by_class_name('el-input__inner').is_enabled()
        self.assertTrue(actual)
        logger.info('断言')

    # @unittest.skip('1')
    def test_case03(self):
        """直客购买个人独资注册提交资料"""
        self.sole_proprietorship_submission()
        actual = self.driver.find_element_by_class_name('el-input__inner').is_enabled()
        self.assertTrue(actual)
        logger.info('断言')


if __name__ == '__main__':
    unittest.main(verbosity=2)
