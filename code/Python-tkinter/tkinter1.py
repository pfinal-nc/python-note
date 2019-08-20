import tkinter as tk  # 导入tkinter模块
from tkinter import messagebox
from tkinter import simpledialog
import config
from func import Func
import hashlib


class App:
    def __init__(self, master):
        self.master = master
        self.party = tk.StringVar()
        self.init_menu()
        self.md5_str = tk.StringVar()

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
                                                {'label': k, 'variable': self.party, 'value': menu[k],
                                                 'command': self.set_content})
        Radiobutton_button.menu.add_separator()
        Radiobutton_button.menu.add_command(label="退出", command=lambda: root.quit());
        Radiobutton_button['menu'] = Radiobutton_button.menu

    def set_content(self):
        for widget in self.master.winfo_children()[1:]:
            widget.destroy()
        view_frame = tk.Frame(self.master, relief=tk.RAISED, borderwidth=1)
        eval('self.' + self.party.get())(view_frame)
        view_frame.pack(side=tk.TOP)

    def md52(self, view_frame):
        tk.Label(view_frame, text="MD5加密", bg="Azure", font=('Arial', 12), width=300, height=2, justify="center").pack()
        form = tk.Frame(view_frame)
        entry = tk.Entry(form, width=44, font=('Arial', 12), textvariable=self.md5_str, foreground='green',
                         justify=tk.LEFT)
        entry.grid(column=0, columnspan=3, row=0)
        btn = tk.Button(form, text="加密", font=('Arial', 10), justify=tk.RIGHT, command=self.md5_action)
        btn.grid(column=4, row=0)
        form.pack()
        text = tk.Frame(view_frame)
        tk.Label(text, text="加密结果:", font=('Arial', 8), justify="right").pack(side=tk.LEFT)
        self.textarea = tk.Text(text, width=400, height=4, font=('Arial', 10), foreground="green")
        self.textarea.configure(background=root.cget("background"))
        text.pack()

    def md5_action(self):
        if self.md5_str.get() == "":
            tk.messagebox.showinfo(title="错误了", message='大爷,请填写你要加密的东东')
        else:
            self.md5_str_list = [];
            self.md5_str_list.append(
                {'UTF-8': hashlib.md5(str(self.md5_str.get()).encode(encoding="UTF-8")).hexdigest()})
            self.md5_str_list.append({'GBK': hashlib.md5(str(self.md5_str.get()).encode(encoding="GBK")).hexdigest()})
            self.md5_str_list.append(
                {'GB2312': hashlib.md5(str(self.md5_str.get()).encode(encoding="GB2312")).hexdigest()})
            self.md5_str_list.append(
                {'GB18030': hashlib.md5(str(self.md5_str.get()).encode(encoding="GB18030")).hexdigest()})
        self.set_md5_content()

    def set_md5_content(self):
        self.textarea.pack()
        self.textarea.delete('1.0', tk.END)
        if len(self.md5_str_list) > 0:
            for item in self.md5_str_list:
                self.textarea.insert(tk.END, str(item) + "\n")


root = tk.Tk()
root.title("开发小工具")
root.geometry('600x400')
# 禁止改变窗口大小
# root.resizable(width=False, height=False)
App(root)
root.mainloop()
# root.mainloop()
