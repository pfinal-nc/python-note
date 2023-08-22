# -*- coding: utf-8 -*-
# @Time    : 2023/8/10 10:38
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : celery.py.py
# @Software: PyCharm
from celery import Celery


app = Celery('proj',
             backend='redis://localhost:6379/0',
             broker='redis://localhost:6379/0'
             include=['proj.tasks'])


app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()

    # 在这里创建了一个 Celery 实例（也称 app），如果需要使用 Celery，导入即可。
    # 该 broker 参数为指定的中间人（Broker）URL。
