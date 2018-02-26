# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
from selenium import webdriver
import unittest

class Blog(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
        self.driver.get("")

