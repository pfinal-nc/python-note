# -*- coding: utf-8 -*-
# @Time    : 2023/10/7 16:16
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : 别名.py
# @Software: PyCharm
from typing import Union, TypeVar, Tuple

if __name__ == '__main__':
    #  在项目中 经常会有一些变量类型非常复杂, 且在多出地方都会使用到,那么利用别名 是最方便的 声明一个DEMO_TYPE的别名, 别名不需要写TypeHInts.
    #
    # DEMO_TYPE = Dict[str, List[int]]
    #
    # demo_container: DEMO_TYPE = {"bar": [1, 2, 3, 4]}
    # print(demo_container)
    # print(demo_container)

    # TypeVar跟Union的使用很像,区别是Union返回值的类型与输入的值是可以不一样的,而TypeVar返回值类型与输入的值类型必须一样的.当前Generic也是跟TypeVar一样要求返回值的类型与输入的值类型必须是一样的

    DEMO_TYPE = Union[int, str]


    def demo(a: DEMO_TYPE, b: DEMO_TYPE) -> DEMO_TYPE:
        """

        @param a:
        @param b:
        """
        pass


    demo(1, "1")
    demo(1, 1)
    demo("1", "1")

    DEMO1_TYPE = TypeVar('DEMO1_TYPE', int, str)


    def demo1(a: DEMO1_TYPE, b: DEMO1_TYPE) -> DEMO1_TYPE:
        """

        @param a:
        @param b:
        """
        return 1,1

    demo1(1, "1")
    demo1(1, 1)
    demo1('1', '1')