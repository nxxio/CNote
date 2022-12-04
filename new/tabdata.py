from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
import sys, io, textedit

class TabData(QStackedWidget):
    def __init__(self):
        super(TabData, self).__init__()
        
        self.data_tabs = []     #{'TextEdit': ' ','FilePath': ' '})
        self.InitTabData()
        

    #def control_text_change(self):
     #   self.data_tabs[self.currentIndex()]['TextEdit'].textChanged.connect(self.text_changed)

    #def text_changed(self):
     #   self.data_tabs[self.currentIndex()]['TxtCh'] = True
      #  print(True)
    
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


    def save_data(self, save_as):

        index = self.currentIndex()
        fp = self.data_tabs[index]['FilePath']

        if save_as == False:

            if fp == 'Start_tab' or fp == 'NewTab':
                return self.save_data(save_as= True)
            else:
                try:
                    file = open(fp, 'w',encoding= 'utf8')
                    file.write(self.data_tabs[index]['TextEdit'].toPlainText())
                    file.close()
                except Exception:
                    return -1

        elif save_as == True:

            fp = QtWidgets.QFileDialog.getSaveFileName()[0]
        
            if fp == '':
                return -2
            # файл не выбран

            elif len(fp.rsplit('.')) >= 1:
                pass   #если задан тип файла

            else:
                fp += '.txt'                         #если не задан, по дефолту сохраняем в txt
            
            try:
                self.data_tabs[index]['FilePath'] = fp
                f = open(fp, 'w',encoding= 'utf8')
                f.write(self.data_tabs[index]['TextEdit'].toPlainText())
                f.close()
                return [index,fp]
                

            except Exception:
                return -3



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
        