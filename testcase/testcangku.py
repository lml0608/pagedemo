# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

import unittest

import time

from selenium import webdriver


from pages.cangku_page import cangku_page
from pages.login_page import LoginPage
from common.screen import Screen
from common.logger import Log
from common.getlogger import get_logger



from libs.browser import browser


class Testcangku(unittest.TestCase):
    driver = browser('chrome')
    log = get_logger()

    def setUp(self):

        #option = webdriver.ChromeOptions()
        #option.add_argument('disable-infobars')
        #option.add_argument('headless')

        #self.driver = browser('chrome')
        self.base_url = 'http://192.168.2.119:8088/wgmfjz/shoppingmall/index.html'

    @Screen(driver)
    def test_add_buynow01(self):

        '''添加活动'''
        self.log.info("-----------测试开始----------------")

        cangku = cangku_page(self.driver)
        login_page = LoginPage(self.driver)


        login_page.get_url(self.base_url)


        #login_page.login()

        #login_page.open_yunyingshangc()

        cangku.open_cangku()

        #切换iframe
        cangku.switch_to_frame()

        cangku.click_add_btn()



        # time.sleep(10)
        #
        #
        # buynow.add_buynow('ceshi','2','54','100','1','2018-03-06 09:25:16','2018-03-09 09:25:16')
        #
        #
        # alert = buynow.is_alert_present()
        # self.assertEqual(alert.text,"产品id54已配置秒杀活动！")
        #
        #
        # self.assertEqual(self.driver.switch_to.alert.text,"产品id54已配置秒杀活动！")
        # buynow_page.accept_alert()
        #
        # alert.accept()


    def tearDown(self):

        self.driver.quit()
