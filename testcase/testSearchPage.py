# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

import unittest

import time

from selenium import webdriver


from pages.baidu_page import BaiduPage
from libs import browser

class TestSearchPage(unittest.TestCase):


    def setUp(self):

        self.driver = browser.browser('chrome')

        self.base_url = 'http://www.baidu.com'

    def testSearch(self):


        driver = self.driver


        url = self.base_url


        text = "selenium"


        assert_title = "百度一下，你就知道"


        #获取SearchPage对象，并初始化driver，url
        baidu_page = BaiduPage(driver)

        #调用方法打开浏览器
        baidu_page.open(url,t=assert_title)

        baidu_page.input_search(text)

        baidu_page.click_search()


        #调用方法输入搜索关键字
        #search_Page.input_search_text(text)

        # 调用方法点击搜索
        #search_Page.click_search_btn()
        #断言判断打开页面是否正常

        self.assertEqual(baidu_page.get_title(), assert_title)


    def tearDown(self):

        self.driver.quit()








