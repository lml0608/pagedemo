# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

import os

print(os.path.dirname(__file__))


driver = webdriver.Chrome(
            executable_path='/Users/liubin/PycharmProjects/pagedemo/tools/chromedriver')




driver.get("http://www.baidu.com")

#driver.get("https://home.cnblogs.com/u/liumeile/")

# print(driver.title)
#
# title = EC.title_is('用户登录 - 博客园')
#
# r2 = EC.title_contains('用户登录')
#
# print(title(driver))
#
# print(r2)


#等待时长10秒，默认0.5秒杀询问一次
#unitil()元素出现
#WebDriverWait(driver,10).until(lambda x: x.find_element("id","kw")).send_keys("selenium")


#元素消失

#is_disappeared = WebDriverWait(driver,10,1).until_not(lambda x: x.find_element_by_id("kw").is_displayed())



#print(is_disappeared)

driver.quit()

