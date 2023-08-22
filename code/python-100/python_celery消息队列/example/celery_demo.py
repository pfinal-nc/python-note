# -*- coding: utf-8 -*-
# @Time    : 2023/8/10 10:21
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : celery_demo.py
# @Software: PyCharm
from task import add

if __name__ == '__main__':
    result = add.delay(4, 4)
    print(result.ready())  # 检测是否处理完毕
    print(result.get(timeout=1))  # 整个任务执行过程为异步的，如果一直等待任务完成，会将异步调用转换为同步调用
    # 如果任务出现异常，get() 会再次引发异常，可以通过 propagate 参数进行覆盖：
    print(result.get(propagate=False))
    # 如果任务出现异常，可以通过 traceback 命令进行回溯
    print(result.traceback)

