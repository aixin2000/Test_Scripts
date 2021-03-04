# coding:utf-8
import unittest
from data import HTMLTestRunner
import time
from tools.send_mail_1 import Email
import os
import sys

#把当前目录的父目录加到sys.path中
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/hhr/case'
discover = unittest.defaultTestLoader.discover(start_dir=path, pattern='test_*.py')

all_suites = unittest.TestSuite()
all_suites.addTest(discover)

now = time.strftime('%Y_%m_%d_%H_%M_%S')
reprot_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/hhr/report/report_%s.html' % now
file = open(reprot_path, 'wb')
test_runner = HTMLTestRunner.HTMLTestRunner(stream=file,
                                            title=u'hhr自动化测试用例',
                                            description=u'hhr测试组')

test_runner.run(all_suites)
file.close()

test_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+ '/hhr/report'
email = Email()
new_report = email.new_report(test_path)
email.send_mail(new_report)  # 发送测试报告

# send_zmail的实例化
# email = Email()
# email.send_mail()
