# *** Import GUI library ***
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.sip import *
from PyQt5.uic import loadUiType
import sys
import os
from os import path



# *** Import package to download from Youtube ***
import pytube

import urllib.request


## Improt UI file

FORM_CLASS,_=loadUiType(path.join(path.dirname(__file__),"gui.ui"))



## Initiate UI file data
class MainApp(QMainWindow, FORM_CLASS):
    def __init__(self,parent=None):
        super(MainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.Handel_UI()
        self.Handel_Buttons()




    def Handel_UI(self):
        self.setWindowTitle("Youtube Downloader")
        self.setFixedSize(724,312)


    def Handel_Buttons(self):
        self.pushButton.clicked.connect(self.Handel_Download)

    def Handel_Browse(self):
        pass
    def Handel_progressBar(self, blocknum, blocksize, totolsize):
        pass


    def Handel_Download(self):
        url = self.lineEdit.text()
        location = self.lineEdit_2.text()
        try:
            youtube = pytube.YouTube(url)
            video = youtube.streams.get_lowest_resolution()
            video.download(location)
        except Exception:
            QMessageBox.warning(self, "Error", "Download faild")
            return

        QMessageBox.information(self, "Completed", "Download Finished")
        self.progressBar.setValue(0)
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()







if __name__ == '__main__':
    main()