import sys
import formlayout   #导入相应的设计好的QTdesigner主窗口的类模块，然后即可直接进行展示
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__=="__main__":
    app=QApplication(sys.argv)

    mainwin=QMainWindow()                #创建一个窗口
    ui=formlayout.Ui_MainWindow()  #创建一个QTdesigner的类
    ui.setupUi(mainwin)                   #将对象直接进行运行设置函数，向主窗口上添加控件
    mainwin.show()                        #展示出来窗口的形式

    sys.exit(app.exec_())                #承接开头语句，用来实时的显示窗口
