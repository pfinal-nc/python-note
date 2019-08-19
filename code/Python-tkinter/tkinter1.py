import tkinter as tk  # 导入tkinter模块
from tkinter import messagebox
from tkinter import simpledialog
import config


class App:
    def __init__(self, master):
        fm1 = tk.Frame(master)
        menu = tk.Menu(fm1)
        root.config(menu=menu)
        # 设置菜单选项
        # menu_one = self.get_menu(menu)
        # menu.add_cascade(label='首页', menu=menu_one)
        # self.get_menu(self, menu)
        # menu.add_command(label='关于', command=self.about_me)

    def get_menu(self):
        menu_list = config.MENU
        print(menu_list)

    def menu_func(self, params):
        print(params)

    def about_me(self):
        tk.messagebox.showinfo('欢迎', "欢迎使用!\nBy PFinal")


root = tk.Tk()  # 主窗口
root.title('吃饱喝足')  # 窗口标题
root.geometry("800x800+200+50")
display = App(root)
display.get_menu()
# root.mainloop()
