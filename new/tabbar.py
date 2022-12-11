from PyQt6.QtWidgets import QTabBar
import sys

class TabBar(QTabBar):

    def __init__(self, flag = None):
        super(TabBar, self).__init__()

        self.setExpanding(False)
        self.setDocumentMode(True)
        self.setTabsClosable(True)
        self.setDrawBase(False)
        self.tabs = [] #{'TabName': 'NewTab'}
        self.noname_count=[]
        if flag == True:
            self.Init_tabs()
        
        
    def add_new_tab(self,filename = None):

        if filename == None:

            self.addTab(f'Noname-{self.Slot()}')
            self.tabs.append({'TabName': 'NewTab'})
            self.setCurrentIndex(len(self.tabs)-1)
        else: 

            self.addTab(filename)
            self.tabs.append({'TabName': filename})
            self.setCurrentIndex(len(self.tabs)-1)
    

    def del_tab(self, index):

        self.removeTab(index)
        if self.tabs[index]['TabName'] == 'NewTab':
            self.clearSlot(index)
        del self.tabs[index]


    def Init_tabs(self):

        self.addTab(f'Noname-{self.Slot()}')
        self.tabs.append({ 'TabName': 'NewTab'})


    def getIndex(self):

        return self.currentIndex()


    def change_tab_name(self, i, filepath):

        self.setTabText(i,filepath.split('/')[-1])
        self.clearSlot(i)

    def get_tab_name(self,i):
        return self.tabs[i]['TabName']

    def get_number_of_tabs(self):
        return len(self.tabs)


    def Slot(self):

        if len(self.noname_count) == 0:
            self.noname_count.append(True)
            return 1
        else:
            for i in range(len(self.noname_count)):

                if self.noname_count[i] == False:
                    self.noname_count[i] = True
                    return i+1

            self.noname_count.append(True)
            return len(self.noname_count)

    def clearSlot(self, i):

        self.noname_count[i] = False
        temp = False
        for j in range(len(self.noname_count)):
            if self.noname_count[j] == True:
                temp =  True
        
        if temp == False:
            self.noname_count.clear()



if __name__ == '__main__':
    print('не то')
    sys.exit()