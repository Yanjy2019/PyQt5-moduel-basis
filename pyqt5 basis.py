#PyQt5的具体使用方式与入门

import sys
from PyQt5.QtWidgets import QWidget,QApplication  #导入两个类来进行程序界面编程

if __name__=="__main__":
    #创建一个Application的类
    app=QApplication(sys.argv)
    #创建一个窗口
    w=QWidget()
    #设置窗口的尺寸大小
    w.resize(400,200)
    # 移动窗口
    w.move(300,300)

    #设置窗口的标题
    w.setWindowTitle("得一个基于PyQt5的桌面应用")
    #显示窗口
    w.show()
    #静进入程序的主循环，并且通过exit函数确保主循环的安全结束
    sys.exit(app.exec_())  #一一直在桌面上显示窗口形状

#QTdesigner在pycharm平台中的的安装和配置
#直接安装QT软件或者安装anaconda开发环境之后就会在电脑安装好QTdesigner.exe文件，之后pycharm里面配置扩展工具external tool文件，便可以方便在pycharm里面直接启动




