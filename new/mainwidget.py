import sys, io, tabbar, tabdata
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QMessageBox, QFileDialog
from PyQt6.QtWidgets import QMessageBox as QM


class MainWidget(QWidget):

    def __init__(self, flag = None):
        super(MainWidget,self).__init__()

        if flag == True:

            self.tab_bar = tabbar.TabBar(flag)
            self.tab_data = tabdata.TabData(flag)
        else:
            self.tab_bar = tabbar.TabBar()
            self.tab_data = tabdata.TabData()

        main_layout = QVBoxLayout()
        main_layout.setSpacing(0)

        main_layout.addWidget(self.tab_bar)
        main_layout.addWidget(self.tab_data)

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

        if self.tab_data.getStatus(index) == True:          # если в блокноте что то писали спрашиваем надо ли сохранить
           
            reply = QM.question(self,'Warning','Save ' + self.tab_bar.get_tab_name(index) + '?', QM.StandardButton.Yes| QM.StandardButton.No | QM.StandardButton.Cancel, QM.StandardButton.Yes)

            if reply == QM.StandardButton.Yes:              # если ответили что сохранить надо
                code = self.Save_file()                     # сохраняем
                if code == -3 or code == -1:  
                    
                    QMessageBox.information(self,'Error', 'Ошибка сохранения',QM.StandardButton.Ok) # если есть ошибки
                    return -4

                elif code == -2:
                    return -4                               # если не выбран файл куда сохранять ничего не делаем
                else:                                       
                    self.tab_bar.del_tab(index)             # если ошибок нет, мы все сохранили, удаляем вкладку
                    self.tab_data.del_tabData(index)

            elif reply == QM.StandardButton.Cancel:
                return - 4
            else:
                self.tab_bar.del_tab(index)                 # если ответили что сохранять не нало, просто удаляем
                self.tab_data.del_tabData(index)

        else:
            self.tab_bar.del_tab(index)                     # если документ не  изменялся, удаляем вкладку
            self.tab_data.del_tabData(index)


    def Open_file(self):
        
        fnames = QFileDialog.getOpenFileNames()
        list_filePath = fnames[0]

        for i in range(len(list_filePath)):

            file = open(list_filePath[i],'r',encoding='utf8')
            self.New_Tab(file,list_filePath[i])
            file.close()

    def argv_Open(self,filePath):

        file = open(filePath,'r',encoding='utf8')
        self.tab_bar.add_new_tab(filePath.split('\\')[-1])
        self.tab_data.add_new_tabData(file,filePath)
        file.close()

    def Save_as_file(self):
        
        code = self.tab_data.save_data(save_as= True)
        if type(code) == list:
            self.tab_bar.change_tab_name(code[0],code[1])
            return None
        else:
            if code == -1 or code == -3:
                QMessageBox.information(self,'Error', 'Ошибка сохранения',QM.StandardButton.Ok)
            return code


    def Save_file(self):

        code = self.tab_data.save_data(save_as= False)
        if type(code) == list:
            self.tab_bar.change_tab_name(code[0],code[1])
            return None
        else:
            if code == -1 or code == -3:
                QMessageBox.information(self,'Error', 'Ошибка сохранения',QM.StandardButton.Ok)
            return code




if __name__ == '__main__':
    print('не то')
    sys.exit()