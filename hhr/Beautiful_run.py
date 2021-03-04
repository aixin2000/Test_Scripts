# -*- coding:utf-8 -*-
# author:aixin
# datetime:2021/2/19 15:44
# software: PyCharm
import unittest
from BeautifulReport import BeautifulReport
import time
# from tools.send_zmail import Email
from tools.send_mail_1 import Email
import os

test_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\hhr\\report'
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/hhr/case'
discover = unittest.defaultTestLoader.discover(start_dir=path, pattern='test_*.py')
all_suites = unittest.TestSuite()
all_suites.addTest(discover)

if __name__ == '__main__':
    now = time.strftime('%Y_%m_%d_%H_%M_%S')
    reprot_path = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))) + '/hhr/report/report_%s.html' % now
    file = open(reprot_path, 'wb')
    ruuner = BeautifulReport(all_suites)
    ruuner.report(filename='report_' + now, description='hhr测试用例', report_dir=test_path)
    file.close()

    # 发送测试报告
    email = Email()
    new_report = email.new_report(test_path)
    email.send_mail(new_report)
