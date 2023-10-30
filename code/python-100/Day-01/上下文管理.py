# -*- coding: utf-8 -*-
# @Time    : 2023/10/30 10:30
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 上下文管理.py
# @Software: PyCharm
import asyncio
import ssl

import aiohttp
import certifi


# 自定义上下文管理器
# 通过定义 __enter__ 和 __exit__ 方法，就可以创建一个上下文管理器

class MyContextManager:
    def __enter__(self):
        print("ente 进入上下文")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit 退出上下文")


with MyContextManager() as m:
    print("with 在上下文中执行操作")


# 获取一个锁, 执行相应的操作, 完成后再释放锁,伪代码
#
# some_lock = threading.Lock()
# with some_lock:
#     .....


# 常用使用上下文管理的场景

# 1. 打开-关闭
#  如果想自动打开和关闭资源 可以使用上下文管理器 例如, 可以使用上下文管理器打开一个套接字并关闭它

# 2. 锁定-释放
# 上下文管理器可以帮助更有效地管理对象的锁, 允许获取锁并自动释放锁

# 3. 启动-停止
# 上下文管理器还能帮助处理需要启动和停止阶段的场景, 可以使用上下文管理启动器并自动停止

# 4. 更改-重置
# 上下文管理器可以处理更改和重置场景
# 例如, 应用程序需要链接多个数据源, 有一个默认链接,需要链接到另一个数据源:
#  首先， 使用上下文管理器将默认链接更改为新链接
#  第二, 使用新链接
#  第三, 完成新链接的操作后, 将其重置回默认链接

# 5. 进入-退出
# 上下文管理器可以处理进入和退出的场景

#  常见的上下文管理器和with 语句使用

# 1. 文件操作
# with open('demo.txt') as file:
#     content = file.read()
#     print(content)
#

# 2. 数据库链接 在数据库操作中, 使用with 语句可以确保在使用完数据库连接后正确地关闭连接, 防止资源泄露
# with sqlite3.connect('mydatabase.db') as conn:
#     cursor = conn.cursor()
#     cursor.execute('select * from users')

# 3. 网络连接, 类似于数据库链接, 确保在网络连接使用完毕后关闭连接是良好的实践

# url = "http://dev.local.crm.cn/index.php?m=user&a=department"
# # 使用sesssion对象作为上下文管理器
# with requests.Session() as session:
#     # 发起request请求
#     resp = session.get(url)
#     # 在此处处理相应
#     print(resp.status_code)
#     print(resp.text)

# 4. 线程锁, threading 模块 Lock 对象可以作为上下文管理器,确保在使用完锁之后正确释放.
#
# lock = threading.Lock()
# with lock:
#     ....

# 5. 文件锁 在多进程环境下,可以使用文件锁确保多个进程对同一文件的互斥锁访问.
#
# with open("demo.txt") as file:
#     fcntl.flock(file, fcntl.LOCK_EX)
#     # 执行需要文件锁的代码
#     fcntl.flock(file, fcntl.LOCK_UN)

# 6. 时间测量 使用上下文管理器来测量代码块的执行时间

# class TimerContextManager:
#     """TimerContextManager"""
#
#     def __enter__(self):
#         self.start_time = time.time()
#         return self
#
#     def __exit__(self, exc_type, exc_value, trace):
#         self.end_time = time.time()
#         elapsed_time = time.time() - self.start_time
#         print(f"Code executed in {elapsed_time} seconds")
#
#
# with TimerContextManager():
#     print("测试测试")

# 7. 测试资源管理 在测试中, 可以使用上下文管理器确保在测试开始喝结束时正确滴分配和释放资源
# class TestContextManager:
#     """TestContextManager"""
#     def __enter__(self):
#         # 在测试开始时分配资源
#         print("测试开始")
#         return self
#
#     def __exit__(self, exc_type, exc_value, trace):
#         # 在测试结束时释放资源
#         print("测试结束")
#
#
# with TestContextManager():
#     print("测试测试")

# 异步上下文管理器
# 要创建异步上下文管理器, 需要定义__aenter__和__aexit__方法.

class AsyncSession:
    """ AsyncSession """

    def __init__(self, url):
        self.url = url

    async def __aenter__(self):
        sslcontext = ssl.create_default_context(cafile=certifi.where())
        self.session = aiohttp.ClientSession()
        response = await self.session.get(self.url, ssl=sslcontext)
        return response

    async def __aexit__(self, exc_type, exc_value, exc_tb):
        await self.session.close()


async def check(url):
    async with AsyncSession(url) as response:
        print(f"{url}: status: {response.status}")
        html = await response.text()
        print(f"{url}: type -> {html[:17].strip()}")


async def main():
    """main"""
    await asyncio.gather(
        check("https://realpython.com"),
        check("https://pycoders.com"),
    )


asyncio.run(main())
