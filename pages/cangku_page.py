# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
from selenium.webdriver.common.by import By
from .base import BasePage
import time


class cangku_page(BasePage):

    #切换到仓库管理
    cangku_btn = (By.LINK_TEXT, "仓库管理")

    #添加仓库按钮
    add_btn = (By.ID,"warehouse_addBtn")
    #仓库代码
    ck_code = (By.ID,"warehouse_code")
    #仓库名称
    ck_name = (By.ID, "warehouse_name")
    #提交按钮
    sumbit_btn = (By.XPATH, "//div[@class='bui-stdmod-footer']/button[1]")
    #取消按钮
    cancle_btn = (By.XPATH, "//div[@class='bui-stdmod-footer']/button[2]")

    iframe_id = 'mainFrame'



    def __init__(self,driver):

        BasePage.__init__(self,driver)


    def open_cangku(self):
        '''点击打开秒杀页面'''
        self.click(self.cangku_btn)
        #self.log.info('打开仓库界面')

    def switch_to_frame(self):
        '''切换到iframe'''
        self.switch_frame(self.iframe_id)
        #self.log.info('切换到iframe')

    def click_add_btn(self):
        '''点击添加按钮'''
        self.click(self.add_btn)
        #self.log.info('点击添加秒杀')

        time.sleep(2)




