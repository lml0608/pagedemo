

import logging,time,os


log_path = '/Users/liubin/PycharmProjects/pagedemo/logs'



class Log(object):

    def __init__(self):

        #日志的命名

        self.logname = os.path.join(log_path,'%s.log' % time.strftime('%Y_%m_%d'))


        self.logger = logging.getLogger()


        self.logger.setLevel(logging.DEBUG)


        #日志输出格式

        self.formatter = logging.Formatter('[%(asctime)s]- [%(filename)s][line:%(lineno)d]-%(levelname)s: %(message)s')


    def __console(self,level,message):

        #写到文件
        fh = logging.FileHandler(self.logname,'a',encoding='utf-8')

        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)

        self.logger.addHandler(fh)


        #输出到控制台
        ch = logging.StreamHandler()

        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)

        self.logger.addHandler(ch)


        if level == 'info':
            self.logger.info(message)

        elif level == 'debug':
            self.logger.debug(message)

        elif level == 'warning':
            self.logger.warning(message)

        elif level == 'error':
            self.logger.error(message)



        #避免日志输入重复
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)

        #关闭打开的文件

        fh.close()




    def debug(self,message):

        self.__console('debug', message)

    def info(self,message):

        self.__console('info', message)

    def warning(self,message):

        self.__console('warning', message)

    def error(self,message):

        self.__console('error', message)


# if __name__ == '__main__':
#
#     log = Log()
#
#
#     log.info("----测试开始----")
#
#     log.info("----输入密码----")
#
#     log.warning("----测试结果----")






