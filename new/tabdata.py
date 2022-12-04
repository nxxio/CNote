from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
import sys, io

class TabData(QStackedWidget):
    def __init__(self):
        super(TabData, self).__init__()
        
        self.data_tabs = []
        self.InitTabData()

    
    def InitTabData(self):

        self.data_tabs.append({'TextEdit': textedit.PlainTextEdit(),'FilePath': 'Start_tab'})
        self.addWidget(self.data_tabs[0]['TextEdit'])


    def add_new_tabData(self,file = None ,filePath = None):
        
        if file == None:

            self.data_tabs.append({'TextEdit': textedit.PlainTextEdit(),'FilePath': 'NewTab'})
            i = len(self.data_tabs)-1
            self.addWidget(self.data_tabs[i]['TextEdit'])
            self.setCurrentIndex(i)

        else:

            self.data_tabs.append({'TextEdit': textedit.PlainTextEdit(),'FilePath': filePath})
            i = len(self.data_tabs)-1
            self.addWidget(self.data_tabs[i]['TextEdit'])
            self.setCurrentIndex(i)
            self.data_tabs[i]['TextEdit'].setPlainText(file.read())


    def save_data(self, i, file):

        if type(file) == io.TextIOWrapper:
             file.write(self.data_tabs[i]['TextEdit'].toPlainText())
        else:
            print('error')


    def visible_data(self, index):
        self.setCurrentIndex(index)


    def getFilePath(self):

        return self.data_tabs[self.currentIndex()]['FilePath']


    def getStatus(self,i):

        return self.data_tabs[i]['TextEdit'].document().isModified()


    def del_tabData(self, index):
        
        self.removeWidget(self.data_tabs[index]['TextEdit'])
        del self.data_tabs[index]


    

        

if __name__ == '__main__':
    print('не то')
    sys.exit()
        