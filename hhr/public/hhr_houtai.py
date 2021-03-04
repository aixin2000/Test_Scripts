from selenium import webdriver
import unittest
from time import sleep
from logs.logger import Logger

logger = Logger(logger="Test_Login").getlog()


class Hou_Tai(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        logger.info('打开谷歌浏览器')
        self.driver.get('http://test2.hhrchina.com/new/system/getCompanyManger.html')
        logger.info('打开官网后台')
        self.driver.maximize_window()
        logger.info('最大化浏览器窗口')
        self.driver.implicitly_wait(10)

    def tearDown(self) -> None:
        self.driver.find_element_by_xpath('//a[@href = "/user/system/exit.html"]').click()
        logger.info('退出登录')
        sleep(2)
        self.driver.quit()
