import configparser
import random
import os
import time


class Test_Tools:
    def randomPhone(self):
        headList = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
                    "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
                    "186", "187", "188", "189"]
        return random.choice(headList) + "".join(random.choice("0123456789") for i in range(8))

    def read_config(self):
        file = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/config/config.ini'
        # 创建配置文件对象
        con = configparser.ConfigParser()
        # 读取文件
        con.read(file, encoding='utf-8')
        # 获取所有section
        sections = con.sections()
        # ['url', 'email']

        # 获取特定section
        items = con.items('testServer')  # 返回结果为元组
        # [('baidu','http://www.baidu.com'),('port', '80')] 	# 数字也默认读取为字符串

        # 可以通过dict方法转换为字典
        items1 = dict(items)
        return items1



    # def savescreenshot(self, driver, file_name):
    #     if not os.path.exists('./image'):
    #         os.makedirs('./image')
    #     now = time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
    #     # 截图保存
    #     driver.get_screenshot_as_file('./image/' + now + '-' + file_name)
    #     # time.sleep(1)




