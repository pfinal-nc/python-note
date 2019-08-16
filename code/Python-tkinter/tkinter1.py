import tkinter as tk  # 导入tkinter模块
from tkinter import messagebox
from tkinter import simpledialog


class App:
    def __init__(self, master):
        fm1 = tk.Frame(master)
        menu = tk.Menu(fm1)
        root.config(menu=menu)
        # 设置菜单选项
        menu_one = self.get_menu(menu)
        menu.add_cascade(label='语言', menu=menu_one)

    def get_menu(self, menu):
        menu1 = tk.Menu(menu, tearoff=False)
        for item in ['python', 'c', 'java', 'c++', 'c#', 'php', 'B', '退出']:
            if item == '退出':
                menu1.add_separator()
                menu1.add_command(label=item, command=root.quit)
            else:
                menu1.add_command(label=item, command=lambda: print(item))
        return menu1


root = tk.Tk()  # 主窗口
root.title('吃饱喝足')  # 窗口标题
root.geometry("800x800+200+50")
display = App(root)
root.mainloop()
