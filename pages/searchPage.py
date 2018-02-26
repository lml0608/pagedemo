# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''


from selenium import webdriver


from selenium.webdriver.common.by import By

from .basePage import Page

class SearchPage(Page):



    search_input = (By.ID, "kw")


    search_button = (By.ID, "su")

    def __init__(self, driver, base_url="http://www.baidu.com"):

        Page.__init__(self,driver,base_url)


    #打开浏览器
    def gotoBaiduHomePage(self):

        self.driver.get(self.base_url)

    #输入搜索内容

    def input_search_text(self, text="liubin"):

        self.input_text(self.search_input, text)

    #点击搜索按钮
    def click_search_btn(self):

        self.click(self.search_button)










