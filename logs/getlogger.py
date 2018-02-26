# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
import logging
import logging.config
import os
def get_logger():


    filepath = os.path.join(os.path.dirname(__file__), 'logging.conf')

    logging.config.fileConfig(filepath)
    return logging.getLogger()


def call_me():

    logger = get_logger()
    # filepath = os.path.join(os.path.dirname(__file__), 'logging.conf')
    # print(filepath)

    logger.info("hi")
# call_me()

#"D:/dev/pagedemo/testcase"


