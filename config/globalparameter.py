import os,time

project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]), '.'))
# 测试用例代码存放路径（拥有构建suite）
test_case_path = project_path+"\\test_case"
# 测试报告的存放路径，并以当前时间作为报告的前缀
report_path = project_path+"\\report\\"
report_name = report_path+time.strftime('%Y-%m-%d_%H_%M_%S_',time.localtime())