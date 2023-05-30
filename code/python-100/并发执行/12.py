# -*- coding: utf-8 -*-
# @Time    : 2023/5/30 17:31
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 12.py
# @Software: PyCharm
import asyncio


# @asyncio.coroutine
# def hello():
#     print("hello world! (%s)" % threading.currentThread())
#     yield from asyncio.sleep(1)
#     print("hello world! (%s)" % threading.currentThread())
#
#
# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# @asyncio.coroutine
async def wget(host):
    print("wget %s..." % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()


loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
