# -*- coding: utf-8 -*-
# @Time    : 2023/5/30 15:30
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 07.py
# @Software: PyCharm
import concurrent.futures
import time


def process(work):
    time.sleep(2)
    print('process {}'.format(work))


def process_works(works):
    # 这里我们创建了一个线程池，总共有4个线程可以分配使用。
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(process, works)


def main():
    works = [
        'work1',
        'work2',
        'work3',
        'work4'
    ]
    start_time = time.time()
    process_works(works)
    end_time = time.time()
    print('use {} seconds'.format(end_time - start_time))


if __name__ == '__main__':
    main()