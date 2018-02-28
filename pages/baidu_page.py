# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''


from .base import BasePage

from selenium.webdriver.common.by import By
from common.logger import Log


class BaiduPage(BasePage):

    log = Log()



    def __init__(self,driver):

        BasePage.__init__(self,driver)


    search_box = (By.ID,'kw')

    search_ok = (By.ID,'su')


    def open_url(self):
        self.open(self.url)


    def input_search(self,key_word):

        self.send_keys(self.search_box,key_word)
        self.log.info("输入内容：%s" % key_word)

    def click_search(self):

        self.click(self.search_ok)

        self.log.info("点击按钮：id=su")



