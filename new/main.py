import sys, io, mainwidget
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QShortcut,QKeySequence



class Mainwindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(QtWidgets.QMainWindow, self).__init__()

        self.mw = mainwidget.MainWidget()
        self.setCentralWidget(self.mw)
        self.setMinimumSize(QtCore.QSize(800,600))
        self.open_shortcut = QShortcut(QKeySequence(QKeySequence.StandardKey.Open),self)
        self.new_shortcut = QShortcut(QKeySequence(QKeySequence.StandardKey.New),self)
        self.save_shortcut = QShortcut(QKeySequence(QKeySequence.StandardKey.Save),self)

        self.open_shortcut.activated.connect(self.mw.Open_file)
        self.new_shortcut.activated.connect(self.mw.New_Tab)
        self.save_shortcut.activated.connect(self.mw.Save_file)



if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Mainwindow()

    MainWindow.show()
    sys.exit(app.exec())
    
