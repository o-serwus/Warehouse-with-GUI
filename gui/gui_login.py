from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(941, 862)
        MainWindow.setStyleSheet("background-color: rgb(59, 59, 59);\n"
                                 "border-color: rgb(103, 103, 103);\n"
                                 "color: rgb(212, 212, 212);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.navbar_frame = QtWidgets.QFrame(self.centralwidget)
        self.navbar_frame.setGeometry(QtCore.QRect(0, 0, 941, 80))
        self.navbar_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.navbar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.navbar_frame.setObjectName("navbar_frame")

        self.wh_label = QtWidgets.QLabel(self.navbar_frame)
        self.wh_label.setGeometry(QtCore.QRect(10, 10, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.wh_label.setFont(font)
        self.wh_label.setObjectName("wh_label")

        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(0, 80, 941, 741))
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        
        self.background_label = QtWidgets.QLabel(self.main_frame)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 941, 741))
        self.background_label.setPixmap(QtGui.QPixmap("/home/dci-student/Desktop/Ola/Database/08-23Database/Data08.31/Warehouse2/Warehouse2/warehouse.jpeg"))
        self.background_label.setScaledContents(True)
        self.background_label.setObjectName("background_label")
        
        
        

        self.label_3 = QtWidgets.QLabel(self.main_frame)
        self.label_3.setGeometry(QtCore.QRect(340, 100, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.sing_in_button = QtWidgets.QPushButton(self.main_frame)
        self.sing_in_button.setGeometry(QtCore.QRect(400, 360, 121, 31))
        self.sing_in_button.setObjectName("sing_in_button")

        self.user_input = QtWidgets.QLineEdit(self.main_frame)
        self.user_input.setGeometry(QtCore.QRect(360, 240, 201, 23))
        self.user_input.setAlignment(QtCore.Qt.AlignCenter)
        self.user_input.setObjectName("user_input")

        self.pass_input = QtWidgets.QLineEdit(self.main_frame)
        self.pass_input.setGeometry(QtCore.QRect(360, 310, 201, 23))
        self.pass_input.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_input.setObjectName("pass_input")
        self.pass_input.setEchoMode(QtWidgets.QLineEdit.Password)

        self.user_label = QtWidgets.QLabel(self.main_frame)
        self.user_label.setGeometry(QtCore.QRect(396, 210, 131, 20))
        self.user_label.setAlignment(QtCore.Qt.AlignCenter)
        self.user_label.setObjectName("user_label")

        self.pass_label = QtWidgets.QLabel(self.main_frame)
        self.pass_label.setGeometry(QtCore.QRect(400, 280, 131, 20))
        self.pass_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_label.setObjectName("pass_label_2")
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.wh_label.setText(_translate("MainWindow", "WareHouse"))
        self.label_3.setText(_translate("MainWindow", "Sign in"))
        self.sing_in_button.setText(_translate("MainWindow", "Sign In"))
        self.user_label.setText(_translate("MainWindow", "User"))
        self.pass_label.setText(_translate("MainWindow", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_Login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
