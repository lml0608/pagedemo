# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

from selenium import webdriver

def browser(browser='firefox'):
    ''''打开浏览器函数，"firefox"、"chrome"、"ie"、"phantomjs"'''

    try:

        if browser == "firefox":

            driver = webdriver.Firefox()
            return driver

        elif browser == "chrome":
            # driver = webdriver.Chrome(
            #     executable_path='/Users/liubin/PycharmProjects/pagedemo/tools/chromedriver')

            # driver = webdriver.Chrome(
            #     executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
            driver = webdriver.Chrome(
                executable_path='D:\\app\\pagedemo\\tools\\chromedriver.exe')




            return driver
        elif browser == "ie":
            driver = webdriver.Ie()
            return driver

        elif browser == "phantomjs":

            driver = webdriver.PhantomJS()
            return driver

        else:

            print("Not found this browser, You can enter 'firefox', 'chrome', 'ie' or 'phantomjs'")
    except Exception as msg:

        print("%s" % msg)