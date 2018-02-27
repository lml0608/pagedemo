# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

import unittest
import os
import time

import HTMLTestRunner as ht


#用例路径
case_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"testcase")
print(case_path)
#日志存放路径
logs_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"logs")
print(logs_path)
#报告
report_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"test_report")

now = time.strftime("%Y_%m_%d %H_%M_%S")

report_abspath=os.path.join(report_path, now+"report.html")


#返回所有用例
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,pattern="test*.py",top_level_dir=None)
    print(discover)

    return discover
# suite = unittest.TestLoader().discover(case_path)
# print(suite)


if __name__ == '__main__':

    #all_case()

    #runner = unittest.TextTestRunner()

    #runner.run(all_case())

    #testunit = unittest.TestSuite()
    #testunit.addTest(TestSearchPage('testSearch'))


    #testunit.addTest(TestBuynowPage('testAddBuynow'))
    #定义报告输出路径
    #htmlPath = u"page_demo_Report.html"
    fp = open(report_abspath, "wb")
    runner = ht.HTMLTestRunner(
        stream=fp,
        title='这是我的自动化测试报告',
        description='用例执行情况：'
    )
    runner.run(all_case())
    #runner.run(testunit)
    fp.close()
