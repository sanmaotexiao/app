from src.common.sendEmail import SendEmail
from HTMLTestRunner import HTMLTestRunner
import unittest
from config.globalparameter import report_name, test_case_path

# 执行测试
if __name__=="__main__":
    suite = unittest.defaultTestLoader.discover(start_dir=test_case_path, pattern= "test_setting.py")
    report = report_name+"Report.html"
    with open(report,'w',encoding='utf-8') as rf:
        runner = HTMLTestRunner.HTMLTestRunner(stream=rf,title='UI自动化测试',description='Android端测试用例执行结果')
        runner.run(suite)
    # SendEmail().send_email(report)