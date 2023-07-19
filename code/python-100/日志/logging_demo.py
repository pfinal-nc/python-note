# -*- coding: utf-8 -*-
# @Time    : 2023/7/18 19:12
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : logging_demo.py
# @Software: PyCharm
import logging

# Logger：即 Logger Main Class，是我们进行日志记录时创建的对象，我们可以调用它的方法传入日志模板和信息，来生成一条条日志记录，称作 Log Record。
# Log Record：就代指生成的一条条日志记录。
# Handler：即用来处理日志记录的类，它可以将 Log Record 输出到我们指定的日志位置和存储形式等，如我们可以指定将日志通过 FTP 协议记录到远程的服务器上，Handler 就会帮我们完成这些事情。
# Formatter：实际上生成的 Log Record 也是一个个对象，那么我们想要把它们保存成一条条我们想要的日志文本的话，就需要有一个格式化的过程，那么这个过程就由 Formatter 来完成，返回的就是日志字符串，然后传回给 Handler 来处理。
# Filter：另外保存日志的时候我们可能不需要全部保存，我们可能只需要保存我们想要的部分就可以了，所以保存前还需要进行一下过滤，留下我们想要的日志，如只保存某个级别的日志，或只保存包含某个关键字的日志等，那么这个过滤过程就交给 Filter 来完成。
# Parent Handler：Handler 之间可以存在分层关系，以使得不同 Handler 之间共享相同功能的代码。


# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(filename)s - %(funcName)s - %(lineno)s')

logging.basicConfig(level=logging.DEBUG,
                    filename='output.log',
                    datefmt='%Y/%m/%d %H:%M:%S',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(module)s - %(message)s')
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info('This is a log info')
    logger.debug('Debugging')
    logger.warning('Warning exists')
    logger.info('Finish')

# basicConfig 参数
# filename: 即日志输出的文件名, 如果指定了这个信息之后 实际上会启用 FileHandler，而不再是 StreamHandler，这样日志信息便会输出到文件中了。
# filemode: 这个是指定日志文件的写入方式, 有两种形式, 一种是 w 一种是 a 分别代表清楚后写入和追加写入
# format: 指定日志信息的输出格式, 即上文实例所示的参数
#   %(levelno) s：打印日志级别的数值
#   %(levelname) s：打印日志级别的名称
#   %(filename) s：打印当前执行程序名
#   %(funcName) s：打印日志的当前函数
#   %(lineno) d：打印日志的当前行号。
#   %(asctime) s：打印日志的时间。
#   %(thread) d：打印线程 ID。
#   %(threadName) s：打印线程名称.
#   %(process) d：打印进程 ID。
#   %(processName) s：打印线程名称。
#   %(module) s：打印模块名称。
#   %(message) s：打印日志信息。
#
# datefmt: 指定时间的输出格式
# style:  如果 format 参数指定了, 这个额参数就可以指定格式化时的占位符 如 %, {, $
# level: 指定日志输出的类别, 程序会输出大于等于此级别的信息
# stream: 在没有指定 filename 的时候会默认使用 streamhandler
# handlers: 可以指定日志处理时所使用的 Handlers，必须是可迭代的。
