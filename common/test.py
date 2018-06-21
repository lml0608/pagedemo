# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

import os

print(os.getcwd())

# D:\app\pagedemo\common
#
# D:\app\pagedemo\screenshots

path = os.path.join(os.path.dirname(os.getcwd()),'screenshots')

print(path)

#D:\app\pagedemo