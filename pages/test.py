# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''



def outer():

    def inner():

        print("hello")

    return inner

foo = outer()

foo()