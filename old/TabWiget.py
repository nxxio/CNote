import sys,io, SaveDialog
from tkinter import dialog
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QTextDocument


# Ошибки при сохранения файла
# save_file() возвращает '-1' когда у документа нет файла, в который надо сохранять, при написании текста в открытой вкладке в программе
# save_as_file() возвращает '-2' когда после открытия file dialog файл не выбран, file dialog закрывается пользователем

# сделай диалоговые окна и резервное копирование запи.lug,jj,fchmgn dkuthjgnсь в txt

class Tabwiget():


    def __init__(self):

        self.tab_data = [] # [{'Tab': Qwidget(), 'TextEdit': QPlainTextEdit(tab) ,'FileName': Путь к файлу или Empy_file }]
        
        self.noname_count =0
        self.tabwidget = QtWidgets.QTabWidget()
        self.tabwidget.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,QtWidgets.QSizePolicy.Policy.Expanding)
        
    

    def Init_tabs(self):

        self.tabwidget.setGeometry(QtCore.QRect(0, 0, 800, 570))
        self.tabwidget.setDocumentMode(True)

        tab = QtWidgets.QWidget()
        start_note = QtWidgets.QPlainTextEdit(tab)
        #start_note.setGeometry(QtCore.QRect(0, 0, 800, 550))
        
        self.tab_data.append({'Tab': tab, 'TextEdit': start_note,'FileName': 'Start_tab'})

        self.tabwidget.addTab(tab,"start_tab")
        #self.Tabwidget.setMovable(True)
        self.tabwidget.setTabsClosable(True)  


    def control_tab(self):

        self.tabwidget.tabBarDoubleClicked.connect(self.add_new_tab)
        self.tabwidget.tabCloseRequested.connect(self.close_tab)


    def close_tab(self,i):

        if self.tab_data[i]['TextEdit'].document().isModified() == True:

            if self.save_file(self.tab_data[i]) ==-1:
                self.save_as_file(self.tab_data[i])
                
            self.tabwidget.removeTab(i)
            del self.tab_data[i]
            self.noname_count -=1
            
        else: 
            self.tabwidget.removeTab(i)
            del self.tab_data[i]
            self.noname_count -= 1




    def add_new_tab(self,file=None, file_name = None):

        if file == -1 or file == None: # -1 приходит от даблклика по tabbar or shortcut
            
            tab = QtWidgets.QWidget()

            new_note = QtWidgets.QPlainTextEdit(tab)
            new_note.setGeometry(QtCore.QRect(0, 0, 800, 550))

            self.tab_data.append({'Tab': tab, 'TextEdit': new_note,'FileName': 'Empy_file' })
            
            #for i in range(len(self.tab_data)):

             #   if self.tab_data[i]['FileName'] == 'Empy_file':
              #      temp +=1

            self.tabwidget.addTab(tab,f'noname-{self.noname_count+1}')
            self.noname_count +=1
            self.tabwidget.setCurrentIndex(len(self.tab_data)-1)


        elif type(file) == io.TextIOWrapper:
            
            tab = QtWidgets.QWidget()
            new_note = QtWidgets.QPlainTextEdit(tab)
            new_note.setGeometry(QtCore.QRect(0, 0, 800, 550))

            self.tab_data.append({'Tab': tab, 'TextEdit': new_note,'FileName': file_name})
            self.tabwidget.addTab(tab,file_name.split('/')[-1])
            self.tabwidget.setCurrentIndex(len(self.tab_data)-1)
        
            new_note.setPlainText(file.read())


    def save_file(self,tab):
    
        try:
        
            #if self.tab_data[self.tabwidget.currentIndex()]['FileName'] == 'Start_tab' or self.tab_data[self.tabwidget.currentIndex()]['FileName'] == 'Empy_file':
            if tab['FileName'] == 'Start_tab' or tab['FileName'] == 'Empy_file':   
                # диалоговое окно 'хотите сохранить?' при условии что флаг тру
                # флаг будет тру если запрос придет от меню
                return -1

            else:
                #f = open(self.tab_data[self.tabwidget.currentIndex()]['FileName'], 'w', encoding='utf8')
                #f.write(self.tab_data[self.tabwidget.currentIndex()]['TextEdit'].toPlainText())   
                f = open(tab['FileName'], 'w', encoding='utf8')
                f.write(tab['TextEdit'].toPlainText())
                f.close()

        except Exception:

            return -1

    
    def save_as_file(self,tab):
        
        fname = QtWidgets.QFileDialog.getSaveFileName()[0]
        
        if fname == '':
            # файл не выбран
            return -2

        elif len(fname.rsplit('.')) > 1:
            f = open(fname, 'w',encoding= 'utf8')

        else:
            fname += '.txt' 
            f = open(fname, 'w',encoding= 'utf8')

        try:
            #f.write(self.tab_data[self.tabwidget.currentIndex()]['TextEdit'].toPlainText())
            f.write(tab['TextEdit'].toPlainText())
            tab['FileName'] = fname
            f.close()

        except Exception:

            return -2


    def open_file(self):
        
        fnames = QtWidgets.QFileDialog.getOpenFileNames()
        list_name = fnames[0]

        for i in range(len(list_name)):

            f = open(list_name[i],'r',encoding='utf8')
            self.add_new_tab(f,list_name[i])
            f.close()

    def menu_save_file(self):
    
        try:
        
            if self.tab_data[self.tabwidget.currentIndex()]['FileName'] == 'Start_tab' or self.tab_data[self.tabwidget.currentIndex()]['FileName'] == 'Empy_file':
            
                self.save_as_file(self.tab_data[self.tabwidget.currentIndex()])
            else:
                f = open(self.tab_data[self.tabwidget.currentIndex()]['FileName'], 'w', encoding='utf8')
                f.write(self.tab_data[self.tabwidget.currentIndex()]['TextEdit'].toPlainText())   
                f.close()

        except Exception:

            return

if __name__ == '__main__':

    print(' Не то ')
    sys.exit()


