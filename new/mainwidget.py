import sys, io, tabbar, textedit, tabdata
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *

class MainWidget(QWidget):

    def __init__(self):
        super(MainWidget,self).__init__()

        self.tab_bar = tabbar.TabBar()
        self.tab_data = tabdata.TabData()

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.setSpacing(0)

        main_layout.addWidget(self.tab_bar)
        main_layout.addWidget(self.tab_data)

        #self.setLayout(main_layout)
        MainWidget.setLayout(self,main_layout)
        self.control_tabs()
        

    def New_Tab(self,file=None, filePath = None):
        
        if file == -1 or file == None: # -1 приходит от даблклика по tabbar or shortcut

            self.tab_bar.add_new_tab()
            self.tab_data.add_new_tabData()

        elif type(file) == io.TextIOWrapper:

            self.tab_bar.add_new_tab(filePath.split('/')[-1])
            self.tab_data.add_new_tabData(file= file, filePath= filePath)


    def control_tabs(self):

        self.tab_bar.tabBarDoubleClicked.connect(self.New_Tab)
        self.tab_bar.tabBarClicked.connect(self.Switch_tabs)
        self.tab_bar.tabCloseRequested.connect(self.Close_Tab)


    def Switch_tabs(self,index):
        
        if index == -1:
            return
        else:
            self.tab_data.visible_data(index)


    def Close_Tab(self,index):

        self.tab_bar.setCurrentIndex(index)
        self.Switch_tabs(index)
        if self.tab_data.getStatus(index) == True:
            
            code = self.Save_file()
            if code == -2 or code == -3 or code == -1:
                return
            else:
                self.tab_bar.del_tab(index)
                self.tab_data.del_tabData(index)

        else:
            self.tab_bar.del_tab(index)
            self.tab_data.del_tabData(index)


    def Open_file(self):
        
        fnames = QtWidgets.QFileDialog.getOpenFileNames()
        list_filePath = fnames[0]

        for i in range(len(list_filePath)):

            file = open(list_filePath[i],'r',encoding='utf8')
            self.New_Tab(file,list_filePath[i])
            file.close()


    def Save_as_file(self):
        
        fp = QtWidgets.QFileDialog.getSaveFileName()[0]
        
        if fp == '':
            # файл не выбран
            return - 2

        elif len(fp.rsplit('.')) > 1:
            f = open(fp, 'w',encoding= 'utf8')   #если задан тип файла

        else:
            fp += '.txt'                          #если не задан, по дефолту сохраняем в txt
            f = open(fp, 'w',encoding= 'utf8')

        try:
            self.tab_data.save_data(file= f, filePath= fp, i = self.tab_bar.getIndex())
            f.close()

        except Exception:

            return -3


    def Save_file(self):
    
        try:
            fp = self.tab_data.getFilePath()
            if fp == 'Start_tab' or fp == 'NewTab':

                return self.Save_as_file()
                
            else:

                f = open(fp,'w',encoding= 'utf8')
                self.tab_data.save_data(file = f, filePath= fp, i= self.tab_bar.getIndex())   
                f.close()
                
        except Exception:
            print(-1)
            return -1




if __name__ == '__main__':
    print('не то')
    sys.exit()