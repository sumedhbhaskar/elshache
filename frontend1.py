# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frontend.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from demobackend import *
from scripting import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(402, 309)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")


        self.general_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.general_label.setFont(font)
        self.general_label.setObjectName("general_label")
        self.gridLayout.addWidget(self.general_label, 0, 1, 1, 1)

        #total share label 
        self.total_shares_label = QtWidgets.QLabel(self.centralwidget)
        self.total_shares_label.setObjectName("total_shares_label")
        self.gridLayout.addWidget(self.total_shares_label, 1, 0, 1, 3)

        #total shares input
        self.total_shares_input = QtWidgets.QLineEdit(self.centralwidget)
        self.total_shares_input.setObjectName("total_shares_input")
        self.gridLayout.addWidget(self.total_shares_input, 1, 3, 1, 2)

        #minimum share label
        self.min_shares_label = QtWidgets.QLabel(self.centralwidget)
        self.min_shares_label.setObjectName("min_shares_label")
        self.gridLayout.addWidget(self.min_shares_label, 2, 0, 1, 3)

        #min share input
        self.min_shares_input = QtWidgets.QLineEdit(self.centralwidget)
        self.min_shares_input.setObjectName("min_shares_input")
        self.gridLayout.addWidget(self.min_shares_input, 2, 3, 1, 2)

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 6)


        self.generateshares_head = QtWidgets.QLabel(self.centralwidget)
        self.generateshares_head.setObjectName("generateshares_head")
        self.gridLayout.addWidget(self.generateshares_head, 4, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 4, 1, 3, 1)

        
        self.generatesecret_key_head = QtWidgets.QLabel(self.centralwidget)
        self.generatesecret_key_head.setObjectName("generatesecret_key_head")
        self.gridLayout.addWidget(self.generatesecret_key_head, 4, 2, 1, 3)


        self.Secret_key_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Secret_key_label.setFont(font)
        self.Secret_key_label.setObjectName("Secret_key_label")
        self.gridLayout.addWidget(self.Secret_key_label, 5, 0, 1, 1)


        self.shareverifier_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.shareverifier_label.setFont(font)
        self.shareverifier_label.setObjectName("shareverifier_label")
        self.gridLayout.addWidget(self.shareverifier_label, 5, 2, 1, 4)

        #secret key input
        self.secret_key_input = QtWidgets.QLineEdit(self.centralwidget)
        self.secret_key_input.setObjectName("secret_key_input")
        self.gridLayout.addWidget(self.secret_key_input, 6, 0, 2, 1)


        #share verifier input
        self.share_verifier_input = QtWidgets.QLineEdit(self.centralwidget)
        self.share_verifier_input.setObjectName("share_verifier_input")
        self.gridLayout.addWidget(self.share_verifier_input, 6, 2, 2, 4)


        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 7, 1, 1, 1)

        #generate share buttom
        self.generate_share_button = QtWidgets.QPushButton(self.centralwidget)
        self.generate_share_button.setObjectName("generate_share_button")
        self.gridLayout.addWidget(self.generate_share_button, 8, 0, 1, 1)
        
        #generate share signal
        self.generate_share_button.clicked.connect(self.generateshares)



        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 8, 1, 2, 1)


        self.share_file_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.share_file_label.setFont(font)
        self.share_file_label.setObjectName("share_file_label")
        self.gridLayout.addWidget(self.share_file_label, 8, 2, 1, 2)

        #browse button
        self.browse_input  = QtWidgets.QLineEdit(self.centralwidget)
        self.browse_input.setObjectName("Browser_input")
        self.gridLayout.addWidget(self.browse_input, 8, 4, 1, 1)

        #self.browse_button = QtWidgets.QPushButton(self.centralwidget)
        #self.browse_button.setObjectName("browse_button")
        #self.gridLayout.addWidget(self.browse_button, 8, 4, 1, 1)


        #generate key button
        self.generate_key_button = QtWidgets.QPushButton(self.centralwidget)
        self.generate_key_button.setObjectName("generate_key_button")
        self.gridLayout.addWidget(self.generate_key_button, 9, 2, 1, 3)
        
        #generate key signal
        self.generate_key_button.clicked.connect(self.generatekey)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 402, 25))
        self.menubar.setObjectName("menubar")
        self.menuFiles = QtWidgets.QMenu(self.menubar)
        self.menuFiles.setObjectName("menuFiles")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFiles.addAction(self.actionExit)
        self.menubar.addAction(self.menuFiles.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.general_label.setText(_translate("MainWindow", "General"))
        self.total_shares_label.setText(_translate("MainWindow", "Total Shares"))
        self.min_shares_label.setText(_translate("MainWindow", "Minimum needed shares"))
        self.generateshares_head.setText(_translate("MainWindow", "Generate Shares"))
        self.generatesecret_key_head.setText(_translate("MainWindow", "Generate Secret key "))
        self.Secret_key_label.setText(_translate("MainWindow", "Secret Key"))
        self.shareverifier_label.setText(_translate("MainWindow", "Share verifier"))
        self.label_2.setText(_translate("MainWindow", "or"))
        self.generate_share_button.setText(_translate("MainWindow", "Generate shares"))
        self.share_file_label.setText(_translate("MainWindow", "Share File"))
    
        self.generate_key_button.setText(_translate("MainWindow", "Generate key"))
        self.menuFiles.setTitle(_translate("MainWindow", "Files"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    def generateshares(self):
        """
        collect data from 
        total_share_input 
        &
        minium_share_input
        &
        secret key input
        and calling the function from backend
        """
        totalshares = int(self.total_shares_input.text())
        minshares   = int(self.min_shares_input.text())
        secretkey   = int(self.secret_key_input.text())

        generateShares(secretkey,totalshares,minshares)

      



    def generatekey(self):
        totalshares = int(self.total_shares_input.text())
        minshares   = int(self.min_shares_input.text())
        shareVerifier = int(self.share_verifier_input.text())

        filename = str(self.browse_input.text())

        generateKey(filename,minshares,shareVerifier)


     

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

