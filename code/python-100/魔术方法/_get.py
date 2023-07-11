# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 15:26
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : _get.py
# @Software: PyCharm
# __get__() 方法是python 中的一个特殊方法 用于定义一个描述符 描述符是一种 python 对象 它定义了另一个对象的访问方式, 可以控制对下那个的访问

class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def __get__(self, instance, owner):
        return instance.temperature

    def __set__(self, instance, value):
        if value < -273.15:
            raise ValueError("Temperature too low")
        instance.temperature = value


class Temperature:
    celsius = Celsius()


temp = Temperature()
temp.celsius = 25
print(temp.celsius)  # 输出 25
print(temp.celsius.to_fahrenheit())  # 输出 77.0