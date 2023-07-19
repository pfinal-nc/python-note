# -*- coding: utf-8 -*-
# @Time    : 2023/7/19 09:37
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : logging_handler.py
# @Software: PyCharm
import logging

# 使用 baseConfig 全局配置, 先声明了一个 Logger 对象, 然后指定了其对应的 Handker 为 FileHandler 对象, 然后 Handler 对象 还单独指定了 Formatter

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler('output.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info('This is a log info')
logger.debug('Debugging')
logger.warning('Warning exists')
logger.info('Finish')

# 没有在使用 baseConfig 全局配置, 而是先声明了一个 Logger 对象, 然后指定了其对应的 Handler 为 FileHandler 对象，然后 Handler 对象还单独指定了 Formatter 对象单独配置输出格式，最后给 Logger 对象添加对应的 Handler 即可

# logging 模块提供的 Handler:
#   streamHandler: logging.StreamHandler 日志输出地址, 可以是 sys.stderr, sys.stdout 或者文件
#   FileHandler:  logging.FileHandler 日志输出到文件
#   BaseRotatingHandler:  logging.handlers.BaseRotatingHandler  基本的 日志回滚方式
#
