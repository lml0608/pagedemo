# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

import unittest

import time

from selenium import webdriver


from pagedemo.pages.buynowPage import BuynowPage


class TestBuynowPage(unittest.TestCase):



    def setUp(self):

        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        #option.add_argument('headless')
        self.driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',chrome_options=option)

        self.base_url = 'http://portaltest.wgmf.com/index.html'


    def test_add_buynow(self):

        '''添加活动成功'''
        driver = self.driver
        url = self.base_url
        staff_id = '449'
        password = '449'
        buynow_page = BuynowPage(driver,url)
        buynow_page.goto_home_page()
        buynow_page.goto_loginpage()
        buynow_page.input_staff_id_text(staff_id)
        buynow_page.input_password_text(password)
        buynow_page.click_login_btn()

        time.sleep(3)
        buynow_page.open_yunyingshangc()
        time.sleep(3)

        buynow_page.open_buynowpage()

        time.sleep(3)

        buynow_page.switch_to_frame("mallmanage_index")

        buynow_page.click_add_btn()

        buynow_page.input_vname_text("ceshi")

        buynow_page.input_vquantity_text("2")


        buynow_page.click_productTitle_btn()

        buynow_page.click_productId_btn("36")


        buynow_page.input_vupperLimit_text("100")

        buynow_page.input_vbuyNowPrice_text("1")


        buynow_page.input_actvity_time('2018-02-06 09:25:16','2018-02-09 09:25:16')

        buynow_page.click_submit_btn()


        self.assertEqual(self.driver.switch_to.alert.text,"保存成功！")
        buynow_page.accept_alert()




    def test_add_buynow1(self):
        '''产品已经创建了秒杀'''


        driver = self.driver


        url = self.base_url

        staff_id = '449'
        password = '449'


        buynow_page = BuynowPage(driver,url)

        buynow_page.goto_home_page()
        #截图测试
        buynow_page.get_screenshort()

        buynow_page.goto_loginpage()
        buynow_page.input_staff_id_text(staff_id)
        buynow_page.input_password_text(password)
        buynow_page.click_login_btn()

        #截图测试
        buynow_page.get_screenshort()

        time.sleep(3)

        buynow_page.open_yunyingshangc()
        time.sleep(3)

        buynow_page.open_buynowpage()
        time.sleep(3)


        buynow_page.switch_to_frame("mallmanage_index")

        buynow_page.click_add_btn()
        #截图测试
        buynow_page.get_screenshort()

        buynow_page.input_vname_text("ceshi")
        buynow_page.input_vquantity_text("2")

        buynow_page.click_productTitle_btn()
        buynow_page.click_productId_btn("54")

        buynow_page.input_vupperLimit_text("100")

        buynow_page.input_vbuyNowPrice_text("1")

        buynow_page.input_actvity_time('2018-02-06 09:25:16','2018-02-09 09:25:16')

        buynow_page.click_submit_btn()

        self.assertEqual(self.driver.switch_to.alert.text,"产品id54已配置秒杀活动！")

        buynow_page.accept_alert()


    def tearDownClass(self):
        self.driver.quit()








