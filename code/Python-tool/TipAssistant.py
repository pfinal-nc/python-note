# 系统相关
import datetime
import os
import random
import threading
import time
import tkinter

# 语音相关
from aip import AipSpeech
from playsound import playsound


# 功能对象
class Function(object):

    # 初始化类
    def __init__(self):
        super(Function, self).__init__()

    # 语音提醒
    def speak(self, text):
        APP_ID = "16578116"
        API_KEY = "binHhPdxelN6mjuAOMGkBkCu"
        SECRET_KEY = "pcwS2WGXDYGqxSSsu7yM79WhOQi2IxgS"

        filename = "speak" + str(int(random.uniform(1, 20))) + ".mp3"

        # 识别声音
        client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
        result = client.synthesis(text, "zh", 1, {"per": 4, "spd": 5, "pit": 3, "vol": 5, })

        mp3File = open(filename, "wb")
        mp3File.write(result)
        mp3File.close()

        # 播放音频
        playsound(filename)
        os.remove(filename)

    # 提示线程
    def noticeThread(self, text, timeIndex):
        spk = threading.Thread(target=self.speak, args=(text,))
        spk.start()

        nitFace = Interface(600, 50)
        x, y = nitFace.getCenterPos()
        nitFace.preConfig(x, y)
        nitFace.drawTest(text)
        nitFace.autoClose(timeIndex)
        nitFace.endConfig()

    # 提示窗口
    def notice(self, text, timeIndex):
        spk = threading.Thread(target=self.noticeThread, args=(text, timeIndex,))
        spk.start()

    # 计算线程
    def openPlanThread(self, text, timeIndex):
        while self.rtime(timeIndex) != 0:
            time.sleep(0.1)

        self.notice(text, 10)

    # 开启计算
    def openPlan(self, text, timeIndex):
        plan = threading.Thread(target=self.openPlanThread, args=(text, timeIndex))
        plan.start()

    # 计算时间
    def rtime(self, timeIndex):
        # 计算时间
        yearNow = datetime.datetime.now().strftime('%Y-%m-%d')
        timeNow = datetime.datetime.now().strftime('%H:%M:%S')
        ta = time.strptime(yearNow + " " + timeIndex, "%Y-%m-%d %H:%M:%S")
        tb = time.strptime(yearNow + " " + timeNow, "%Y-%m-%d %H:%M:%S")
        y, m, d, H, M, S = ta[0:6]
        dataTimea = datetime.datetime(y, m, d, H, M, S)
        y, m, d, H, M, S = tb[0:6]
        dataTimeb = datetime.datetime(y, m, d, H, M, S)
        return (dataTimea - dataTimeb).seconds


# 皮肤界面
class Interface(object):

    # 初始化类
    def __init__(self, winWidth, winHight):
        super(Interface, self).__init__()

        # 窗口主体
        self.root = tkinter.Tk()

        # 右键菜单
        self.menu = 0

        # 鼠标位置
        self.mouseX = 0
        self.mouseY = 0

        # 输入数据
        self.timeText = ""
        self.inputText = ""

        # 窗口位置
        self.winXPos = 0
        self.winYPos = 0

        # 功能函数
        self.func = Function()

        # 窗口宽高
        self.winWidth = winWidth
        self.winHight = winHight

        # 屏幕宽高
        self.realWinXMaxPos = self.root.winfo_screenwidth()
        self.realWinYMaxPos = self.root.winfo_screenheight()

    # 获取居中
    def getCenterPos(self):
        centerXPos = int((self.realWinXMaxPos - self.winWidth) / 2)
        centerYPos = int((self.realWinYMaxPos - self.winHight) / 2)
        return centerXPos, centerYPos

    # 窗口拖动
    def move(self, event):
        new_x = (event.x - self.mouseX) + self.root.winfo_x()
        new_y = (event.y - self.mouseY) + self.root.winfo_y()
        s = str(self.winWidth) + "x" + str(self.winHight) + "+" + str(new_x) + "+" + str(new_y)
        self.root.geometry(s)

    # 最新坐标
    def newpos(self, event):
        self.mouseX, self.mouseY = event.x, event.y

    # 右键菜单
    def rmenu(self, event):
        self.menu.post(event.x_root, event.y_root)

    # 设置线程
    def confirm(self):
        self.func.notice("任务部署完成！", 3)
        self.func.openPlan(self.inputText.get(), self.timeText.get())

    # 预先配置
    def preConfig(self, winXPos, winYPos):
        # 窗口位置
        self.winXPos = winXPos
        self.winYPos = winYPos

        # 窗口置顶
        self.root.overrideredirect(True)
        self.root.resizable(width=False, height=False)

        # 窗口透明
        self.root.attributes("-alpha", 0.6)
        self.root.configure(bg="grey")

        # 窗口位置
        self.root.geometry(
            str(self.winWidth) + "x" + str(self.winHight) + "+" + str(self.winXPos) + "+" + str(self.winYPos))

    # 标题刷新
    def refresh(self, leftTime):
        self.root.wm_attributes('-topmost', 1)
        self.root.overrideredirect(False)

        while leftTime > 0:
            leftTime -= 1
            self.root.title(str(leftTime) + "秒后自动关闭!")
            time.sleep(1)

        self.root.wm_attributes('-topmost', 0)
        self.root.destroy()

    # 自动关闭
    def autoClose(self, leftTime):
        ref = threading.Thread(target=self.refresh, args=(leftTime,))
        ref.start()

    # 右键配置
    def rightKey(self):
        # 菜单配置
        self.menu = tkinter.Menu(self.root, tearoff=0)
        self.menu.add_command(label="退出", command=self.root.quit)
        self.root.bind("<Button-3>", self.rmenu)

    # 后来配置
    def endConfig(self):
        # 事件绑定
        self.root.bind("<B1-Motion>", self.move)
        self.root.bind("<Button-1>", self.newpos)

        # 窗口置顶
        self.root.mainloop()

    # 绘制输入
    def drawInput(self):
        # 背景颜色
        bgColor = "#111111"

        # 边框绘制
        canvas = tkinter.Canvas(self.root, width=self.winWidth - 2, height=self.winHight - 2, bg=bgColor,
                                highlightthickness=0)
        canvas.place(x=1, y=1)

        # 输入时间
        eTime = tkinter.StringVar()
        nowTime = datetime.datetime.now().strftime('%H:%M:%S')
        eTime.set(nowTime)
        self.timeText = tkinter.Entry(self.root, font=("微软雅黑", 10), textvariable=eTime)
        self.timeText.place(x=10, y=10, anchor='nw', width=self.winWidth - 60, height=20)

        timeLabel = tkinter.Label(self.root, text="时间", bg=bgColor, fg="white", font=("微软雅黑", 12))
        timeLabel.place(x=self.winWidth - 40, y=10 - 1, anchor='nw', width=30, height=20)

        # 输入提示
        self.inputText = tkinter.Entry(self.root, font=("微软雅黑", 10))
        self.inputText.place(x=10, y=40, anchor='nw', width=self.winWidth - 60, height=20)

        inputLabel = tkinter.Label(self.root, text="文本", bg=bgColor, fg="white", font=("微软雅黑", 12))
        inputLabel.place(x=self.winWidth - 40, y=40 - 1, anchor='nw', width=30, height=20)

        # 确定按钮
        confirmBtn = tkinter.Button(self.root, text="开启线程", bg=bgColor, fg="white", font=("微软雅黑", 11),
                                    command=self.confirm)
        confirmBtn.place(x=10, y=70 - 1, anchor='nw', width=self.winWidth - 20, height=25)

    # 绘制文本
    def drawTest(self, text):
        # 提示信息
        label = tkinter.Label(self.root, text=text, fg="white", font=("宋体", 24))
        label.configure(bg="black")
        label.place(anchor='nw', width=self.winWidth, height=self.winHight)


# 启动程序
if __name__ == '__main__':
    rootWin = Interface(200, 100)
    rootWin.preConfig(rootWin.realWinXMaxPos - rootWin.winWidth, rootWin.realWinYMaxPos - rootWin.winHight - 40)
    rootWin.drawInput()
    rootWin.rightKey()
    rootWin.endConfig()