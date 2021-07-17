from PyQt5 import QtCore, QtGui, QtWidgets

from Login.ControllerLogin.GestioneLogin import GestioneLogin
from Ui import logo_rc

class UiLogin(object):
    def __init__(self):
        self.controller = GestioneLogin()

    def verificaCredenziali(self):
        username = self.userField.text()
        passwd = self.passwdField.text()
        if username and passwd:
            return self.controller.verificaCredenziali(username=username, password=passwd)
        else:
            raise Exception("Inserire tutti i campi")

    #metodo per la visualizzazione della password inserita nelle label relative
    #alle interfacce correlate al controller del login
    def mostraPasswd(self):
        if self.mostraCheckBox.isChecked():
                self.passwdField.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
                self.passwdField.setEchoMode(QtWidgets.QLineEdit.Password)

    def setupUi(self, loginUi):
            loginUi.setObjectName("Login")
            loginUi.resize(480, 640)
            loginUi.setStyleSheet("background-color: rgb(242,233,216)")

            self.centralWidget = QtWidgets.QWidget(loginUi)
            self.centralWidget.setObjectName("centralWidget")
            self.frame = QtWidgets.QFrame(self.centralWidget)
            self.frame.setGeometry(QtCore.QRect(10, 10, 451, 571))
            self.frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
            self.frame.setStyleSheet("")
            self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
            self.frame.setObjectName("frame")

            self.exitButton = QtWidgets.QPushButton(self.frame)
            self.exitButton.setGeometry(QtCore.QRect(430, 10, 21, 21))
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            self.exitButton.setFont(font)
            self.exitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.exitButton.setMouseTracking(True)
            self.exitButton.setStyleSheet("color:rgb(3, 95, 144);\n"
                                          "border-radius:10px;\n"
                                          "background-color: rgb(229, 82, 2);")
            self.exitButton.setCheckable(False)
            self.exitButton.setAutoDefault(False)
            self.exitButton.setDefault(True)
            self.exitButton.setFlat(True)
            self.exitButton.setObjectName("exitButton")

            self.minimizeButton = QtWidgets.QPushButton(self.frame)
            self.minimizeButton.setGeometry(QtCore.QRect(410, 10, 21, 21))
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            self.minimizeButton.setFont(font)
            self.minimizeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.minimizeButton.setMouseTracking(True)
            self.minimizeButton.setStyleSheet("color: rgb(3, 95, 144);")
            self.minimizeButton.setDefault(True)
            self.minimizeButton.setFlat(True)
            self.minimizeButton.setObjectName("minimizeButton")

            self.logoLabel = QtWidgets.QLabel(self.frame)
            self.logoLabel.setGeometry(QtCore.QRect(150, 70, 151, 161))
            self.logoLabel.setStyleSheet("image:url(:/newPrefix/LoginLogo.png)")
            self.logoLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.logoLabel.setFrameShadow(QtWidgets.QFrame.Plain)
            self.logoLabel.setText("")
            # self.logoLabel.setPixmap(QtGui.QPixmap("../Porojecto/View/logo.png"))
            self.logoLabel.setScaledContents(True)
            self.logoLabel.setObjectName("logoLabel")

            self.loginField = QtWidgets.QPushButton(self.frame)
            self.loginField.setGeometry(QtCore.QRect(290, 430, 111, 31))
            font = QtGui.QFont()
            font.setBold(True)
            font.setWeight(75)
            self.loginField.setFont(font)
            self.loginField.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.loginField.setStyleSheet("background-color: rgb(3, 95, 144);\n"
                                          "border-radius:10px;\n"
                                          "color:rgb(242,233,216);")
            self.loginField.setObjectName("loginField")

            self.passwdField = QtWidgets.QLineEdit(self.frame)
            self.passwdField.setGeometry(QtCore.QRect(50, 360, 291, 41))
            self.passwdField.setAutoFillBackground(False)
            self.passwdField.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                           "border:2px solid rgba(0,0,0,0);\n"
                                           "color:rgb(3, 95, 144);\n"
                                           "font: 13pt \"Ubuntu\";\n"
                                           "border-bottom-color: rgb(3, 95, 144);\n"
                                           "padding-bottom:10px;")
            self.passwdField.setEchoMode(QtWidgets.QLineEdit.Password)
            self.passwdField.setObjectName("passwdField")

            self.userField = QtWidgets.QLineEdit(self.frame)
            self.userField.setGeometry(QtCore.QRect(50, 300, 291, 41))
            self.userField.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.userField.setAutoFillBackground(False)
            self.userField.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                         "border:2px solid rgba(0,0,0,0);\n"
                                         "color:rgb(3, 95, 144);\n"
                                         "font: 13pt \"Ubuntu\";\n"
                                         "border-bottom-color: rgb(3, 95, 144);\n"
                                         "padding-bottom:10px;")
            self.userField.setInputMask("")
            self.userField.setFrame(True)
            self.userField.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.userField.setDragEnabled(False)
            self.userField.setReadOnly(False)
            self.userField.setClearButtonEnabled(False)
            self.userField.setObjectName("userField")

            self.mostraCheckBox = QtWidgets.QCheckBox(self.frame)
            self.mostraCheckBox.setGeometry(QtCore.QRect(50, 420, 161, 20))
            self.mostraCheckBox.setMouseTracking(False)
            self.mostraCheckBox.setStyleSheet("color: rgb(72, 66, 66);")
            self.mostraCheckBox.setTristate(False)
            self.mostraCheckBox.setObjectName("mostraCheckBox")

            self.errorLabel = QtWidgets.QLabel(self.frame)
            self.errorLabel.setGeometry(QtCore.QRect(130, 260, 171, 20))
            self.errorLabel.setStyleSheet("color: rgb(247, 8, 8);")
            self.errorLabel.setText("")
            self.errorLabel.setObjectName("errorLabel")

            self.exitButton.raise_()
            self.minimizeButton.raise_()
            self.logoLabel.raise_()
            self.loginField.raise_()
            self.passwdField.raise_()
            self.mostraCheckBox.raise_()
            self.errorLabel.raise_()
            self.userField.raise_()
            loginUi.setCentralWidget(self.centralWidget)
            self.menubar = QtWidgets.QMenuBar(loginUi)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 25))
            self.menubar.setObjectName("menubar")
            loginUi.setMenuBar(self.menubar)
            self.statusbar = QtWidgets.QStatusBar(loginUi)
            self.statusbar.setObjectName("statusbar")
            loginUi.setStatusBar(self.statusbar)

            self.retranslateUi(loginUi)
            QtCore.QMetaObject.connectSlotsByName(loginUi)
            loginUi.setTabOrder(self.userField, self.passwdField)
            loginUi.setTabOrder(self.passwdField, self.loginField)
            loginUi.setTabOrder(self.loginField, self.mostraCheckBox)
            loginUi.setTabOrder(self.mostraCheckBox, self.minimizeButton)
            loginUi.setTabOrder(self.minimizeButton, self.exitButton)

    def retranslateUi(self, Login):
            _translate = QtCore.QCoreApplication.translate
            Login.setWindowTitle(_translate("Login", "Login"))
            self.exitButton.setText(_translate("Login", "X"))
            self.minimizeButton.setText(_translate("Login", "-"))
            self.loginField.setText(_translate("Login", "Log In"))
            self.passwdField.setPlaceholderText(_translate("Login", "Password"))
            self.userField.setPlaceholderText(_translate("Login", "Username"))
            self.mostraCheckBox.setText(_translate("Login", "Mostra password"))