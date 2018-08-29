# -*- coding:utf-8 -*-
from tkinter import *
import tkinter.messagebox as messagebox

class MyApp(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self,text="世界上最帅的人是谁?")
        self.helloLabel.pack()
        self.quitButton  = Button(self,text="谁呢?",command=self.who)
        self.quitButton.pack()
    def who(self):
        messagebox.showinfo("答案","当然是大爷我了")

myapp = MyApp()
myapp.master.title('骚逼')
myapp.mainloop()