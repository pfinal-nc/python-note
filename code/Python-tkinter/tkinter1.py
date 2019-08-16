import tkinter as tk  # 导入tkinter模块
from tkinter import messagebox
from tkinter import simpledialog


class App:
    def __init__(self, master):
        fm1 = tk.Frame(master)
        tk.Button(fm1, text='打豆豆', command=self.CreatDialog, fg="#fff", bg="red").pack(side=tk.TOP, anchor=tk.W,
                                                                                       fill=tk.X,
                                                                                       expand=tk.YES)
        tk.Button(fm1, text='Center').pack(side=tk.TOP, anchor=tk.W, fill=tk.X, expand=tk.YES)
        tk.Button(fm1, text='bottom').pack(side=tk.TOP, anchor=tk.W, fill=tk.X, expand=tk.YES)
        fm1.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)

    def CreatDialog(self):
        world = simpledialog.askstring('告诉我', '你是不是猪', initialvalue='是')
        if world != "是":
            self.CreatDialog()


root = tk.Tk()  # 主窗口
root.title('吃饱喝足')  # 窗口标题
root.size(200, 200)
display = App(root)
root.mainloop()
