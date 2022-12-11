import sys, mainwidget
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QMainWindow,QApplication
from PyQt6.QtGui import QShortcut,QKeySequence,QAction,QCloseEvent



class Mainwindow(QMainWindow):
    
    def __init__(self, flag= None):
        super(QMainWindow, self).__init__()

        if flag == True:
            self.mw = mainwidget.MainWidget(flag)
        else:
            self.mw = mainwidget.MainWidget()

        self.setCentralWidget(self.mw)
        self.setMinimumSize(QSize(800,600))
        self.open_shortcut = QShortcut(QKeySequence(QKeySequence.StandardKey.Open),self)
        self.new_shortcut = QShortcut(QKeySequence(QKeySequence.StandardKey.New),self)
        self.save_shortcut = QShortcut(QKeySequence(QKeySequence.StandardKey.Save),self)
        self.find_shortcut = QShortcut(QKeySequence(QKeySequence.StandardKey.Find),self)

        self.open_shortcut.activated.connect(self.mw.Open_file)
        self.new_shortcut.activated.connect(self.mw.New_Tab)
        self.save_shortcut.activated.connect(self.mw.Save_file)
        #self.find_shortcut.activated.connect(self.mw.tab_data.findStr)

        self.menubar = self.menuBar()
        self.fileMenu = self.menubar.addMenu('Файл')
        #self.options_menu = self.menubar.addMenu('Параметры')
        #self.spravka_menu = self.menubar.addMenu('Справка')

        self.save = QAction('Save',self)
        self.save_as = QAction('Save As',self)
        self.open = QAction('Open',self)
        
        self.fileMenu.addAction(self.open)
        self.fileMenu.addAction(self.save)
        self.fileMenu.addAction(self.save_as)

        self.save.triggered.connect(self.mw.Save_file)
        self.save_as.triggered.connect(self.mw.Save_as_file)
        self.open.triggered.connect(self.mw.Open_file)

    def closeEvent(self, a0: QCloseEvent) -> None:

        for i in range(self.mw.tab_bar.get_number_of_tabs()-1,-1,-1):

           if self.mw.Close_Tab(i) == -4:
            a0.ignore()
            return
        


if __name__ == '__main__':
    
    if len(sys.argv) >1:
        app = QApplication(sys.argv)
        MainWindow = Mainwindow()
        fp = sys.argv[1]
        MainWindow.mw.argv_Open(fp)
    else:
        app = QApplication(sys.argv)
        MainWindow = Mainwindow(True)
        
    MainWindow.show()
    sys.exit(app.exec())
    
