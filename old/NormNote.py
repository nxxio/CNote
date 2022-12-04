import sys, io
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QShortcut,QKeySequence
from TabWiget import Tabwiget


class MainWindow(QtWidgets.QMainWindow):
    

    def __init__(self):
        super(MainWindow, self).__init__()
        
        MainWindow.resize(self,800, 600)
        #MainWindow.setFixedSize(self,QtCore.QSize(800,600))
        MainWindow.setSizePolicy(self,QtWidgets.QSizePolicy.Policy.Expanding,QtWidgets.QSizePolicy.Policy.Expanding)
        self.setWindowTitle('CNote')

        self.tabs = Tabwiget()
        
     #------------start UI-----------------------------------------#
        self.initUI()
        self.tabs.control_tab()
        #bttn = QtWidgets.QPushButton('asr;fkvjas')
        #self.setCentralWidget(bttn)

        self.setCentralWidget(self.tabs.tabwidget)



   
    def initUI(self):

        #self.statusBar()
    #------------настройка Menubar---------------------------------------------#

        self.menubar = self.menuBar()
        self.fileMenu = self.menubar.addMenu('Файл')
        self.options_menu = self.menubar.addMenu('Параметры')
        self.spravka_menu = self.menubar.addMenu('Справка')

        self.save = QtGui.QAction('Save',self)
        self.save_as = QtGui.QAction('Save As',self)
        self.open = QtGui.QAction('Open',self)
        
        self.fileMenu.addAction(self.open)
        self.fileMenu.addAction(self.save)
        self.fileMenu.addAction(self.save_as)

        self.save.triggered.connect(self.tabs.menu_save_file)
        self.save_as.triggered.connect(self.tabs.save_as_file)
        self.open.triggered.connect(self.tabs.open_file)

     #------------Дефолт настройка TabWidget---------------------------------------------#
        self.tabs.Init_tabs()

        self.open_shortcut = QShortcut(QKeySequence(QKeySequence.StandardKey.Open),self)
        self.new_shortcut = QShortcut(QKeySequence(QKeySequence.StandardKey.New),self)
        self.save_shortcut = QShortcut(QKeySequence(QKeySequence.StandardKey.Save),self)
        #'Ctrl + F'
        
        self.open_shortcut.activated.connect(self.tabs.open_file)
        self.new_shortcut.activated.connect(self.tabs.add_new_tab)
        self.save_shortcut.activated.connect(self.tabs.menu_save_file)


    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:

        for i in range(len(self.tabs.tab_data)-1,-1,-1):

            self.tabs.close_tab(i)
        
        
        



####################################################################################
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    

    MainWindow.show()
    sys.exit(app.exec())
    