# -*- coding: utf-8 -*-
# @Time    : 2023/7/27 16:26
# @Author  : PFinal南丞 <lampxiezi@163.com
# @File    : Pathlib_demo.py
# @Software: PyCharm
import os.path
from pathlib import Path

# pathlib 与 旧的 os.path 相比具有许多优点
# 虽然 os 模块以原始字符串格式表示路径，但 pathlib 使用面向对象的样式，这使得它更具可读性和编写自然

# 老方式
two_dirs_up = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(two_dirs_up)
# 新方式
two_dirs_up = Path(__file__).resolve().parent.parent
print(two_dirs_up)

# 路径被视为对象而不是字符串这一事实也使得 可以创建一次对象, 然后查找其属性或对其进行操作

readme = Path('README.md').resolve()
print(f"Absolute path: {readme.absolute()}")

print(f"File name: {readme.name}")

print(f"File root: {readme.root}")

print(f"File directory: {readme.parent}")

