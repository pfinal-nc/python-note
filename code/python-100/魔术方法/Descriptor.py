# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 15:20
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : Descriptor.py
# @Software: PyCharm
# 描述魔术方法  __get___()  ___set___ __delete___

class Temperature:
    """Temperature"""

    def __init__(self, celsius=0):
        self._celsius = celsius

    def to_fahrenheit(self):
        return (self._celsius * 1.8) + 32

    def __get__(self, instance, owner):
        print("Getting celsius value...")
        return self._celsius

    def __set__(self, instance, value):
        print("Setting celsius value...")
        if value < -273.15:
            raise ValueError("Temperature too low")
        self._celsius = value

    def __delete__(self, instance):
        print("Deleting celsius value...")
        del self._celsius


temp = Temperature()
temp.celsius = 25
print(temp.celsius)

