import sys
import minwinhorizomtal
from PyQt5.QtWidgets import QApplicatio,QMainWindow

if __name__=="__main__":
    app=QApplication(sys.argv)
    mainwin=QMainWindow()
    ui=minwinhorizomtal.Ui_MainWindow()
    ui.setupUi(mainwin)
    mainwin.show()
    sys.exit(app.exec_())
