from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
import sys

class TabBar(QTabBar):

    def __init__(self):
        super(TabBar, self).__init__()

        self.setExpanding(False)
        self.setDocumentMode(True)
        self.setTabsClosable(True)
        self.setDrawBase(False)
        self.tabs = []
        self.Init_tabs()
        
    def add_new_tab(self,filename = None):

        if filename == None:
            self.addTab('New Tab')
            self.tabs.append({'TabName': 'NewTab'})
            self.setCurrentIndex(len(self.tabs)-1)
        else: 

            self.addTab(filename)
            self.tabs.append({'TabName': filename})
            self.setCurrentIndex(len(self.tabs)-1)
    

    def del_tab(self, index):

        self.removeTab(index)
        del self.tabs[index]


    def Init_tabs(self):

        self.addTab('hello')
        self.tabs.append({ 'TabName': 'hello'})


    def getIndex(self):

        return self.currentIndex()


    def change_tab_name(self, i, filepath):

        self.setTabText(i,filepath.split('/')[-1])

    def get_tab_name(self,i):
        return self.tabs[i]['TabName']

if __name__ == '__main__':
    print('не то')
    sys.exit()