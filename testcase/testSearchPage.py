# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

import unittest

import time

from selenium import webdriver


from pagedemo.pages.searchPage import SearchPage


class TestSearchPage(unittest.TestCase):



    def setUp(self):

        self.driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

        self.base_url = 'http://www.baidu.com'

    def testSearch(self):


        driver = self.driver


        url = self.base_url


        text = "selenium"


        assert_title = "百度一下，你就知道"


        #获取SearchPage对象，并初始化driver，url
        search_Page = SearchPage(driver, url)

        #调用方法打开浏览器
        search_Page.gotoBaiduHomePage()


        #调用方法输入搜索关键字
        search_Page.input_search_text(text)

        # 调用方法点击搜索
        search_Page.click_search_btn()
        #断言判断打开页面是否正常

        self.assertEqual(search_Page.get_title(), assert_title)


    def tearDown(self):

        self.driver.quit()








