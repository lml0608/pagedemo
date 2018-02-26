# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
import os,time

from selenium.webdriver.support.ui import WebDriverWait


class Page(object):


    '''
    Page基类
    '''



    def __init__(self, driver, base_url="http://www.baidu.com"):

        self.driver = driver
        self.base_url = base_url

        self.timeout = 30


    def find_element(self, *loc,timeout=10):

        '''元素定位'''

        element = WebDriverWait(self.driver, timeout,1).until(lambda x:x.find_element(*loc))

        #return self.driver.find_element(*loc)

        return element

    def find_elements(self, *loc):
        '''一组元素定位'''

        return self.driver.find_elements(*loc)

    def input_text(self,loc, text):
        '''控件输入'''

        self.find_element(*loc).send_keys(text)

    def click(self, loc):
        '''按钮点击'''
        print(self.find_element(*loc))
        self.find_element(*loc).click()

    # def click_elemements(self, loc, num):
    #     '''按钮点击'''
    #
    #     #print(self.find_elements(*loc))
    #     self.find_elements(*loc)[num].click()


    def get_title(self):
        '''获取网页标题'''

        return self.driver.title

    def clear(self,loc):
        '''清除输入框'''

        return self.find_element(*loc).clear()




    def get_screenshort(self):

        '''截图保存'''
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        screen_name = file_path + rq + '.png'

        try:
            self.driver.get_screenshot_as_file(screen_name)

        except NameError as e:
            print("截图失败")

            self.get_screenshort()












