# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''


from selenium.webdriver.common.by import By
from .base import BasePage
import time
from common.logger import Log
from common.getlogger import get_logger

class BuynowPage(BasePage):

    log = get_logger()


    #秒杀按钮
    buynow_button = (By.LINK_TEXT, "秒杀活动")

    iframe_id = 'mallmanage_index'

    #添加按钮

    addbuynow_button = (By.XPATH, '//*[@class="button button-primary mr10"]')

    #x[0].click()

    # 添加秒杀

    vname_input = (By.ID, "vname")

    vquantity_input = (By.ID, "vquantity")

    productTitle_input = (By.ID, "productTitle")

    #productId_input = (By.NAME, "54")

    vupperLimit_input = (By.ID, "vupperLimit")

    vbuyNowPrice_input = (By.ID, "vbuyNowPrice")

    #提交

    submit_button = (By.XPATH, "html/body/div[3]/div/table/tbody/tr[3]/td/div[2]/button[2]")


    def __init__(self,driver):

        BasePage.__init__(self,driver)


    def open_buynowpage(self):
        '''点击打开秒杀页面'''
        self.click(self.buynow_button)
        self.log.info('打开秒杀界面')

    def switch_to_frame(self):
        '''切换到iframe'''
        self.switch_frame(self.iframe_id)
        self.log.info('切换到iframe')

    def click_add_btn(self):
        '''点击添加按钮'''
        self.click(self.addbuynow_button)
        self.log.info('点击添加秒杀')

        time.sleep(2)

    def add_buynow(self,vname,vquantity,proid,vupperLimit,vbuyNowPrice,starttime,endtime):
        '''添加秒杀'''

        # 输入活动名称

        self.send_keys(self.vname_input, vname)
        self.log.info('输入活动名')

        # 输入活动每人限购
        self.send_keys(self.vquantity_input, vquantity)
        self.log.info('输入每人限购')

        # 点击产品选择框按钮
        self.click(self.productTitle_input)

        # 点击添加按钮

        productId_input = (By.NAME, proid)
        self.click(productId_input)
        time.sleep(3)

        # 输入产品限购数量
        time.sleep(2)
        self.send_keys(self.vupperLimit_input, vupperLimit)
        time.sleep(3)

        # 输入秒杀价

        self.send_keys(self.vbuyNowPrice_input, vbuyNowPrice)

        # 输入活动开始结束时间

        js1 = "document.getElementById('vstartTime').value=\"" + starttime + "\";"
        js2 = "document.getElementById('vendTime').value=\"" + endtime + "\";"
        print(starttime)
        print(js1)

        self.js_execute(js1)
        self.js_execute(js2)

        time.sleep(3)

        # 活动提交

        self.click(self.submit_button)

        time.sleep(10)






        










