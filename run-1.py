import sys
import minwinhorizontal
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__=="__main__":
    app=QApplication(sys.argv)

    mainwin=QMainWindow()                #创建一个窗口
    ui=minwinhorizontal.Ui_MainWindow()  #创建一个QTdesigner的类
    ui.setupUi(mainwin)                   #将对象直接进行运行设置函数，向主窗口上添加控件
    mainwin.show()                        #展示出来窗口的形式

    sys.exit(app.exec_())


