# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

from selenium import webdriver

class Screen(object):

    def __init__(self,driver):
        self.driver = driver



    def __call__(self, f):

        def inner(*args):

            try:

                return f(*args)

            except:

                import time

                nowTime = time.strftime("%Y_%m_%d_%H_%M_%S")

                self.driver.get_screenshot_as_file('%s.jpg' % nowTime)

                raise

        return inner


#import unittest


# class Test(unittest.TestCase):
#
#     driver = webdriver.Firefox()
#
#     def setUp(self):
#         #driver = webdriver.Firefox()
#         self.driver.get("http://www.baidu.com")
#
#
#     @Screen(driver)
#     def test01(self):
#
#         self.driver.find_element_by_id("11kw").send_keys("python")
#         self.driver.find_element_by_id("su").click()

