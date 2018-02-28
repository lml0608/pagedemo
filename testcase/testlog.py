
import time
import unittest

from selenium import webdriver

from common.logger import Log

from common.getlogger import get_logger

from libs.browser import browser

#log = Log()
log = get_logger()

class Test(unittest.TestCase):
    driver = browser('chrome')

    def setUp(self):



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




