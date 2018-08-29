# -*- coding:utf-8 -*-
# 导入 Tkinter 模块
from tkinter import *
import tkinter.messagebox as messagebox
# button
root = Tk()
# def helloCallBack():
#     messagebox.showinfo( "大爷的", "这个是啥骚逼逼")
# B = Button(top,text="点我", command = helloCallBack)
#
# B.pack()
# top.mainloop()
coord = 10, 50, 240, 210
cv = Canvas(root,bg = 'black',height="800")
cv.pack()
root.mainloop()
