# -*- coding: utf-8 -*-
# @Time    : 2023/8/25 10:06
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : app.py
# @Software: PyCharm

from aiohttp import web

# 路由装饰器
routes = web.RouteTableDef()


@routes.get('/')
async def index(request):
    """index """
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')


async def init():
    """ 初始化 HTTP应用 """
    app = web.Application()
    app.add_routes(routes)
    return app


web.run_app(init(), host='127.0.0.1', port=9000)
