# -*- coding: utf-8 -*-
# @Time    : 2023/7/18 14:43
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : enum_demo.py
# @Software: PyCharm
import enum


# python  枚举

class BugCode(enum.Enum):
    """ BugCode """
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4


#
# 1. 枚举类不能用来实例化对象
# 2. 访问枚举类中的某一项, 直接使用类名访问加上要访问即可
# 3. 枚举类里面定义 key=value 在类外部不能修改 value 值
# 4. 枚举项可以用来比较，使用 ==，或者 is
# 5. 枚举类中的 Key 不能相同，Value 可以相同，但是 Value 相同的各项 Key 都会当做别名
# 6. 枚举类可以用 for 进行遍历, members.items() 可以遍历出含有别名的类
# 7. 如果要枚举类中的 value 也不能相同, 需要导入 unique 对枚举类进行装饰


if __name__ == '__main__':

    # 迭代枚举
    for code in BugCode:
        print(f'code_name:{code.name} , code_value:{code.value}')

    for bugcode in BugCode.__members__.items():
        print(f'枚举名:{bugcode[0]} 枚举值:{bugcode[1].value}')

    # 创建枚举
    BugCodeProcess = enum.Enum(
        value='BugCodeProcess',
        names=[
            ('new', 7),
            ('old', 6),
            ('invalid', 5),
            ('wrong', 4),
            ('incomplete', 3)
        ]
    )

    for code in BugCodeProcess:
        print(f'code_name:{code.name} , code_value:{code.value}')
