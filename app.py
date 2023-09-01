from gui.gui_app import Ui_MainWindow_App
from gui.gui_login import Ui_MainWindow_Login
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.main_window = Ui_MainWindow_Login()
        self.main_window.setupUi(MainWindow)
        self.main_window.sing_in_button.clicked.connect(self.login)

    def login(self):
        conn = sqlite3.connect("/home/dci-student/Desktop/Ola/Database/08-23Database/Data08.31/Warehouse2/Warehouse2/db/warehouse.db")
        cursor = conn.cursor()

        user = self.main_window.user_input.text()
        password = self.main_window.pass_input.text()

        query = "SELECT user, password FROM users WHERE user=? AND password=?;"
        cursor.execute(query, (user, password))
        result = cursor.fetchall()

        if result:
            self.main_window = Ui_MainWindow_App()
            self.main_window.setupUi(MainWindow)
            self.main_window.username_output.setText(user)
            self.main_window.pushButton.clicked.connect(self.logout)
        else:
            self.main_window.label_3.setText("Try again")

    def logout(self):
        self.main_window = Ui_MainWindow_Login()
        self.main_window.setupUi(MainWindow)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())