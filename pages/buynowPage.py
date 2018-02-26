# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''


from selenium import webdriver
from pagedemo.logs import getlogger


from selenium.webdriver.common.by import By

from .basePage import Page
import time

class BuynowPage(Page):

    logger = getlogger.get_logger()

    #登陆元素
    login_button = (By.ID, "loginShow")

    staff_input = (By.ID, "staff_id")

    password_input = (By.ID, "password")

    sub_button = (By.CLASS_NAME, "sub")



    #进入商城管理
    manager_button = (By.XPATH, "html/body/div[2]/div/ul/li[4]/a")

    #秒杀按钮
    buynow_button = (By.LINK_TEXT, "秒杀活动")



    #driver.switch_to.frame('mallmanage_index')
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



    def __init__(self, driver, base_url="http://www.baidu.com"):

        Page.__init__(self,driver,base_url)


    #打开浏览器
    def goto_home_page(self):

        self.driver.get(self.base_url)
        self.logger.info("Open url : %s" % self.base_url)

    #弹出登陆框
    def goto_loginpage(self):
        self.click(self.login_button)
        time.sleep(3)

    #输入工号
    def input_staff_id_text(self,staff_id):
        self.input_text(self.staff_input,staff_id)

    #输入密码
    def input_password_text(self,password):
        self.input_text(self.password_input, password)
    #点击登陆按钮
    def click_login_btn(self):
        self.click(self.sub_button)

    #打开运营商城

    def open_yunyingshangc(self):

        self.click(self.manager_button)


    #点击打开秒杀页面

    def open_buynowpage(self):
        self.click(self.buynow_button)


    #切换到iframe
    def switch_to_frame(self, iframe_name):
        self.driver.switch_to.frame(iframe_name)

    #点击添加按钮
    def click_add_btn(self):
        self.click(self.addbuynow_button)

        time.sleep(2)
    #输入活动名称
    def input_vname_text(self, vname):
        self.input_text(self.vname_input, vname)

    #输入活动每人限购
    def input_vquantity_text(self, vquantity):
        self.input_text(self.vquantity_input, vquantity)
        time.sleep(2)

    #点击产品选择框按钮
    def click_productTitle_btn(self):
        self.click(self.productTitle_input)

    #点击添加按钮
    def click_productId_btn(self,text):
        productId_input = (By.NAME, text)
        self.click(productId_input)
        time.sleep(3)



    #输入产品限购名称
    def input_vupperLimit_text(self, vupperLimit):

        self.clear(self.vupperLimit_input)
        time.sleep(2)
        self.input_text(self.vupperLimit_input, vupperLimit)
        time.sleep(3)

    #输入秒杀价

    def input_vbuyNowPrice_text(self, vbuyNowPrice):

        self.input_text(self.vbuyNowPrice_input, vbuyNowPrice)

    #输入活动开始结束时间
    def input_actvity_time(self,starttime,endtime):

        js1 = "document.getElementById('vstartTime').value=\"" + starttime + "\";"
        js2 = "document.getElementById('vendTime').value=\"" + endtime + "\";"
        print(starttime)
        print(js1)

        self.driver.execute_script(js1)
        self.driver.execute_script(js2)

        time.sleep(3)

    #活动提交

    def click_submit_btn(self):

        self.click(self.submit_button)

        time.sleep(3)


    def accept_alert(self):

        self.driver.switch_to.alert.accept()






        

    #点击添加

    #输入搜索内容

    # def input_search_text(self, text="liubin"):
    #
    #     self.input_text(self.search_input, text)
    #
    # #点击搜索按钮
    # def click_search_btn(self):
    #
    #     self.click(self.search_button)










