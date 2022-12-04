import sys, mainwidget
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

        self.menubar = self.menuBar()
        self.fileMenu = self.menubar.addMenu('Файл')
        self.options_menu = self.menubar.addMenu('Параметры')
        #self.spravka_menu = self.menubar.addMenu('Справка')

        self.save = QtGui.QAction('Save',self)
        self.save_as = QtGui.QAction('Save As',self)
        self.open = QtGui.QAction('Open',self)
        
        self.fileMenu.addAction(self.open)
        self.fileMenu.addAction(self.save)
        self.fileMenu.addAction(self.save_as)

        self.save.triggered.connect(self.mw.Save_file)
        self.save_as.triggered.connect(self.mw.Save_as_file)
        self.open.triggered.connect(self.mw.Open_file)



if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Mainwindow()

    MainWindow.show()
    sys.exit(app.exec())
    
