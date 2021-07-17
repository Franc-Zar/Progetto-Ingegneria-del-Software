from PyQt5 import QtCore, QtGui, QtWidgets

from Login.ControllerLogin.GestioneLogin import GestioneLogin
from Ui import logo_rc


class UiModificaPasswd(object):
    def __init__(self):
        self.controller = GestioneLogin()

    def verificaCredenziali(self):
        oldPasswd = self.oldPasswdField.text()
        passwd = self.newPasswdField.text()
        if oldPasswd and passwd:
            return self.controller.verificaCredenziali(oldPasswd=oldPasswd, password=passwd)
        else:
            self.errorLabel.setStyleSheet("color: rgb(237, 28, 36)")
            self.errorLabel.setText("Inserire tutti i campi per favore!")


    # funzione per aggiornare la password dopo aver effettuato l'accesso
    def aggiornaPasswd(self):
        if self.verificaCredenziali():
            try:
                self.controller.changePasswd(self.confirmPasswdField.text(), self.newPasswdField.text())
                self.closeButton.click()
            except Exception as e:
                self.errorLabel.setStyleSheet("color: rgb(237, 28, 36)")
                self.errorLabel.setText(e.args[0])
        else:
            self.errorLabel.setStyleSheet("color: rgb(237, 28, 36)")
            self.errorLabel.setText("Ooops, password errata")


    # metodo per la visualizzazione della password inserita nelle label relative alle interfacce correlate
    # al controller del login
    def mostraPasswd(self):
        if self.mostraCheckBox.isChecked():
            self.oldPasswdField.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.newPasswdField.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.confirmPasswdField.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.oldPasswdField.setEchoMode(QtWidgets.QLineEdit.Password)
            self.newPasswdField.setEchoMode(QtWidgets.QLineEdit.Password)
            self.confirmPasswdField.setEchoMode(QtWidgets.QLineEdit.Password)

    def setupUi(self, loginUi):
        loginUi.setObjectName("Form")
        loginUi.resize(397, 336)

        self.frame = QtWidgets.QFrame(loginUi)
        self.frame.setGeometry(QtCore.QRect(-20, -10, 451, 371))
        self.frame.setStyleSheet("background-color: rgb(242, 233, 216);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.oldPasswdField = QtWidgets.QLineEdit(self.frame)
        self.oldPasswdField.setGeometry(QtCore.QRect(70, 120, 291, 31))
        self.oldPasswdField.setAutoFillBackground(False)
        self.oldPasswdField.setStyleSheet("font: 11pt \"Ubuntu\";\n"
                                          "background-color:rgba(0,0,0,0);\n"
                                          "border:2px solid rgba(0,0,0,0);\n"
                                          "color:rgb(3, 95, 144);\n"
                                          "border-bottom-color: rgb(3, 95, 144);\n"
                                          "padding-bottom:10px;")
        self.oldPasswdField.setText("")
        self.oldPasswdField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.oldPasswdField.setObjectName("oldPasswdField")

        self.newPasswdField = QtWidgets.QLineEdit(self.frame)
        self.newPasswdField.setGeometry(QtCore.QRect(70, 170, 291, 41))
        self.newPasswdField.setAutoFillBackground(False)
        self.newPasswdField.setStyleSheet("font: 11pt \"Ubuntu\";\n"
                                          "background-color:rgba(0,0,0,0);\n"
                                          "border:2px solid rgba(0,0,0,0);\n"
                                          "color:rgb(3, 95, 144);\n"
                                          "border-bottom-color: rgb(3, 95, 144);\n"
                                          "padding-bottom:10px;")
        self.newPasswdField.setText("")
        self.newPasswdField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newPasswdField.setObjectName("newPasswdField")

        self.confirmPasswdField = QtWidgets.QLineEdit(self.frame)
        self.confirmPasswdField.setGeometry(QtCore.QRect(70, 230, 291, 41))
        self.confirmPasswdField.setAutoFillBackground(False)
        self.confirmPasswdField.setStyleSheet("font: 11pt \"Ubuntu\";\n"
                                              "background-color:rgba(0,0,0,0);\n"
                                              "border:2px solid rgba(0,0,0,0);\n"
                                              "color:rgb(3, 95, 144);\n"
                                              "border-bottom-color: rgb(3, 95, 144);\n"
                                              "padding-bottom:10px;")
        self.confirmPasswdField.setText("")
        self.confirmPasswdField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmPasswdField.setObjectName("confirmPasswdField")

        self.titleLabel = QtWidgets.QLabel(self.frame)
        self.titleLabel.setGeometry(QtCore.QRect(40, 20, 191, 20))
        self.titleLabel.setStyleSheet("color:rgb(229, 82, 2);\n"
                                      "font: 11pt \"Ubuntu\";")
        self.titleLabel.setObjectName("titleLabel")

        self.closeButton = QtWidgets.QPushButton(self.frame)
        self.closeButton.setGeometry(QtCore.QRect(390, 20, 21, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.closeButton.setFont(font)
        self.closeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeButton.setStyleSheet("background-color: rgb(229, 82, 2); \n"
                                       "border-radius:10px;\n"
                                       "color:rgb(3, 95, 144);")
        self.closeButton.setFlat(True)
        self.closeButton.setObjectName("closeButton")

        self.minimizeButton = QtWidgets.QPushButton(self.frame)
        self.minimizeButton.setGeometry(QtCore.QRect(370, 20, 21, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.minimizeButton.setFont(font)
        self.minimizeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minimizeButton.setMouseTracking(True)
        self.minimizeButton.setStyleSheet("color:rgb(3, 95, 144);")
        self.minimizeButton.setFlat(True)
        self.minimizeButton.setObjectName("minimizeButton")

        self.modificaButton = QtWidgets.QPushButton(self.frame)
        self.modificaButton.setGeometry(QtCore.QRect(290, 290, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.modificaButton.setFont(font)
        self.modificaButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.modificaButton.setStyleSheet("background-color: rgb(3, 95, 144);\n"
                                          "border-radius:10px;\n"
                                          "color:rgb(242,233,216);")
        self.modificaButton.setObjectName("modificaButton")

        self.errorLabel = QtWidgets.QLabel(self.frame)
        self.errorLabel.setGeometry(QtCore.QRect(110, 80, 211, 20))
        self.errorLabel.setStyleSheet("color: rgb(247, 8, 8);")
        self.errorLabel.setText("")
        self.errorLabel.setObjectName("errorLabel")

        self.mostraCheckBox = QtWidgets.QCheckBox(self.frame)
        self.mostraCheckBox.setGeometry(QtCore.QRect(70, 290, 161, 20))
        self.mostraCheckBox.setMouseTracking(False)
        self.mostraCheckBox.setStyleSheet("color: rgb(72, 66, 66);")
        self.mostraCheckBox.setTristate(False)
        self.mostraCheckBox.setObjectName("mostraCheckBox")

        self.logoLabel = QtWidgets.QLabel(self.frame)
        self.logoLabel.setGeometry(QtCore.QRect(350, 50, 61, 61))
        self.logoLabel.setStyleSheet("image:url(:/newPrefix/LoginLogo.png)")
        self.logoLabel.setText("")
        # self.logoLabel.setPixmap(QtGui.QPixmap("../Porojecto/View/logo.png"))
        self.logoLabel.setScaledContents(True)
        self.logoLabel.setObjectName("logoLabel")

        self.retranslateUi(loginUi)
        QtCore.QMetaObject.connectSlotsByName(loginUi)
        loginUi.setTabOrder(self.oldPasswdField, self.newPasswdField)
        loginUi.setTabOrder(self.newPasswdField, self.confirmPasswdField)
        loginUi.setTabOrder(self.confirmPasswdField, self.modificaButton)
        loginUi.setTabOrder(self.modificaButton, self.mostraCheckBox)
        loginUi.setTabOrder(self.mostraCheckBox, self.minimizeButton)
        loginUi.setTabOrder(self.minimizeButton, self.closeButton)

    def retranslateUi(self, loginUi):
        _translate = QtCore.QCoreApplication.translate
        loginUi.setWindowTitle(_translate("Form", "Form"))
        self.oldPasswdField.setPlaceholderText(_translate("Form", "Attuale Password"))
        self.newPasswdField.setPlaceholderText(_translate("Form", "Nuova Password"))
        self.confirmPasswdField.setPlaceholderText(_translate("Form", "Conferma Nuova Password"))
        self.titleLabel.setWhatsThis(_translate("Form",
                                                "<html><head/><body><p align=\"center\"><span style=\" "
                                                "font-weight:600;\">Modifica Password</span></p></body></html>"))
        self.titleLabel.setText(_translate("Form",
                                           "<html><head/><body><p align=\"center\"><span style=\" "
                                           "font-weight:600;\">Modifica Password</span></p></body></html>"))
        self.closeButton.setText(_translate("Form", "X"))
        self.minimizeButton.setText(_translate("Form", "-"))
        self.modificaButton.setText(_translate("Form", "Salva "))
        self.mostraCheckBox.setText(_translate("Form", "Mostra password"))
