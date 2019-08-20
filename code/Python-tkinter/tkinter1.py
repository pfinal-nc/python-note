import tkinter as tk  # 导入tkinter模块
from tkinter import messagebox
from tkinter import simpledialog
import config
from func import Func


class App:
    def __init__(self, master):
        self.master = master
        self.party = tk.StringVar()
        self.init_menu()

    def init_menu(self):
        mBar = tk.Frame(self.master, relief=tk.RAISED, borderwidth=2)
        mBar.pack(fill=tk.X)
        self.rad_button(mBar)

    def rad_button(self, mBar):
        Radiobutton_button = tk.Menubutton(mBar, text='工具', underline=0)
        Radiobutton_button.pack(side=tk.LEFT)
        Radiobutton_button.menu = tk.Menu(Radiobutton_button)
        for item in config.MENU:
            for menu in item['工具']:
                for k in menu:
                    Radiobutton_button.menu.add('radiobutton',
                                                {'label': k, 'variable': self.party, 'value': menu[k],'command':self.set_content})

        Radiobutton_button['menu'] = Radiobutton_button.menu

    def set_content(self):
        print(self.party.get())




root = tk.Tk()
root.title("开发小工具")
root.geometry('600x400')
# 禁止改变窗口大小
# root.resizable(width=False, height=False)
App(root)
root.mainloop()
# root.mainloop()
