# -*- coding:utf-8 -*-
from public.hhr_qiantai import *

from logs.logger import Logger

logger = Logger(logger="Submit information").getlog()


class HeRegister(HeLogin):
    # @unittest.skip('1')
    def test_case01(self):
        """合作商购买有限注册提交资料"""
        self.helimited_company_submitting_information()
        actual = self.driver.find_element_by_class_name('el-input__inner').is_enabled()
        self.assertTrue(actual)
        logger.info('断言')

    # @unittest.skip('1')
    def test_case02(self):
        """合作商购买有限合伙注册提交资料"""
        self.helimited_partnership_submission()
        actual = self.driver.find_element_by_class_name('el-input__inner').is_enabled()
        self.assertTrue(actual)
        logger.info('断言')

    # @unittest.skip('1')
    def test_case03(self):
        """合作商购买个人独资注册提交资料"""
        self.hesole_proprietorship_submission()
        actual = self.driver.find_element_by_class_name('el-input__inner').is_enabled()
        self.assertTrue(actual)
        logger.info('断言')


if __name__ == '__main__':
    unittest.main(verbosity=2)
