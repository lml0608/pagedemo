
import unittest

from common.logger import Log

from selenium import webdriver

from pages.base import browser,Liubin

import time


log = Log()

class Test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path='/Users/liubin/PycharmProjects/pagedemo/tools/chromedriver')


        self.driver.get("http://www.baidu.com")

        self.driver.implicitly_wait(20)

    def test_01(self):

        log.info("---测试用例开始----")

        self.driver.find_element_by_id("kw").send_keys("selemiu")

        log.info("输入内容：selenium")

        self.driver.find_element_by_id("su").click()

        log.info("点击按钮：id=su")

        time.sleep(2)

        t = self.driver.title

        log.info("获取title内容：%s" % t)

        self.assertIn("百度搜索",t)

    def tearDown(self):

        self.driver.quit()

        log.info("-----用例测试结束--------")


if __name__ == "__main__":

    unittest.main()




