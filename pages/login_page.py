# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''




from selenium.webdriver.common.by import By
from .base import BasePage
import time

from common.logger import Log

from common.getlogger import get_logger

class LoginPage(BasePage):
    ''''登录'''



    #登陆元素
    login_button = (By.ID, "loginShow")

    staff_input = (By.ID, "staff_id")

    password_input = (By.ID, "password")

    sub_button = (By.CLASS_NAME, "sub")

    #进入商城管理
    manager_button = (By.XPATH, "html/body/div[2]/div/ul/li[4]/a")



    #打开浏览器
    def get_url(self,url):

        self.open(url)
        time.sleep(5)



    def login(self,staff_id='449',password='449'):
        '''
        登陆并切换到运营商城
        :param staff_id: 
        :param password: 
        :return: 
        '''
        # 弹出登陆框


        self.click(self.login_button)
        #self.log.info("-----------点击登陆商城----------------")



        # 输入工号
        self.send_keys(self.staff_input, staff_id)
        #self.log.info("-----------输入员工工号----------------")


        # 输入密码
        self.send_keys(self.password_input, password)
        #self.log.info("-----------输入登陆密码----------------")


        # 点击登陆按钮

        self.click(self.sub_button)
        #self.log.info("-----------点击登陆按钮----------------")

        #打开运营管理中心
        self.click(self.manager_button)
        #self.log.info("------------切换到运营商城---------------")



