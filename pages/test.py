# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''


from selenium import webdriver
import time

driver = webdriver.PhantomJS()
driver.get("https://www.baidu.com")

print(driver.title)

time.sleep(10)
driver.find_element_by_id("kw").send_keys("selenium")

driver.find_element_by_id("su").click()








driver.quit()


# def outer():
#
#     def inner():
#
#         print("hello")
#
#     return inner
#
# foo = outer()
#
# foo()