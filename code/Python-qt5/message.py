# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'pfinal'
__mtime__ = '2019/9/24'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QLabel, QLineEdit, QTextEdit, QPushButton, QComboBox, \
    QStyleFactory, QGridLayout
from PyQt5.QtGui import QIcon, QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口的位置和大小
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message box')
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '消息',
                                     "确定要关闭吗?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    # 每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
