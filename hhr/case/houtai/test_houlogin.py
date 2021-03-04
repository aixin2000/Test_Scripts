# import unittest
# # from tools.test_tools import Test_Tools
# from public.hhr_houtai import Hou_Tai
# from logs.logger import Logger
# from time import sleep
# from selenium.common.exceptions import NoSuchElementException
#
# logger = Logger(logger="Test_Login").getlog()
#
#
# class Test_Login(Hou_Tai):
#     @unittest.skip('不执行')
#     def test_case4(self):
#         """后台登录"""
#         sleep(2)
#         self.driver.find_element_by_name('account').send_keys('刘美')
#         logger.info('输入用户名')
#         sleep(1)
#         self.driver.find_element_by_name('pwd').send_keys('hhr123456')
#         logger.info('输入密码')
#         sleep(1)
#         self.driver.find_element_by_class_name('loginButton').click()
#         logger.info('点击登录')
#         sleep(1)
#
#         try:
#             element = self.driver.find_element_by_class_name('layui-layer-btn0')
#         # 原文是except NoSuchElementException, e:
#         except NoSuchElementException as e:
#             # 打印异常信息
#             print(e)
#             # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
#             return False
#         else:
#             # 没有发生异常，表示在页面中找到了该元素，返回True
#             element.click()
#         sleep(5)
#         actual = self.driver.title
#         logger.info('获取标题')
#         self.assertEqual('公司注册', actual)
#         logger.info('断言')
#         js = "window.scrollTo(0,document.body.scrollHeight)"
#         logger.info('下拉网页')
#         self.driver.execute_script(js)
#         logger.info('执行js脚本')
#         sleep(5)
#
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)
