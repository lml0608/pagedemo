# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

import unittest

import time

from selenium import webdriver


from pages.buynow_page import BuynowPage
from pages.login_page import LoginPage
from common.screen import Screen
from common.logger import Log



from libs.browser import browser


class TestBuynowPage(unittest.TestCase):
    driver = browser('chrome')
    log = Log()

    def setUp(self):

        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        #option.add_argument('headless')
        #self.driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',chrome_options=option)
        #self.driver = browser('chrome')
        self.base_url = 'http://portaltest.wgmf.com/index.html'

    @Screen(driver)
    def test_add_buynow(self):

        '''添加活动'''
        self.log.info("-----------测试开始----------------")

        buynow = BuynowPage(self.driver)
        login_page = LoginPage(self.driver)


        login_page.open(self.base_url)


        login_page.login()

        login_page.open_yunyingshangc()

        buynow.open_buynowpage()

        #切换iframe
        buynow.switch_to_frame()

        buynow.click_add_btn()



        time.sleep(10)


        buynow.add_buynow('ceshi','2','54','100','1','2018-03-06 09:25:16','2018-03-09 09:25:16')


        alert = buynow.is_alert_present()
        self.assertEqual(alert.text,"产品id54已配置秒杀活动！")
        #
        #
        # self.assertEqual(self.driver.switch_to.alert.text,"产品id54已配置秒杀活动！")
        # buynow_page.accept_alert()

        alert.accept()







    def tearDown(self):
        self.driver.quit()
        self.log.info("-----------测试结束----------------")








