# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

def test(starttime):

    js1 = "document.getElementById('vstartTime').value=\"" + starttime + "\";"


    print(starttime)
    print(js1)



test("niho")

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