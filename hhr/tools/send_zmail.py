import zmail
import os


class Email():
    def new_report(self, test_report):
        lists = os.listdir(test_report)  # 列出目录的下所有文件和文件夹保存到lists
        lists.sort(key=lambda fn: os.path.getmtime(test_report + "\\" + fn))  # 按时间排序
        file_new = os.path.join(test_report, lists[-1])  # 获取最新的文件保存到file_new
        print(file_new)
        return file_new

    def send_mail(self):
        test_path = "D:\\python_workspace\\PROJECT\\hhr\\report\\"
        new_report1 = self.new_report(test_path)
        with open(new_report1, 'r', encoding='utf-8') as fp:
            content_html = fp.read()
        # 准备邮件内容
        mail_content = {
            'subject': '自动化测试报告',
            # 'content_text': '自动化测试报告内容',
            'content_html': content_html,
            'attachments': new_report1
        }
        # 发件人邮箱何授权码
        sever = zmail.server('aixin02@163.com', 'LRNWTQVGNKHDQEIV')
        # 发件人 - （收件人，邮箱内容）
        list1 = ['aixin02@163.com', '1454622738@qq.com']
        sever.send_mail(list1, mail_content)
        print('邮件发送成功')
