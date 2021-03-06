# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statistiche.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UI_Catalogo(object):
    def setupUi(self, UI_Catalogo):
        UI_Catalogo.setObjectName("UI_Catalogo")
        UI_Catalogo.resize(480, 530)
        UI_Catalogo.setStyleSheet("background-color: rgb(242,233,216)")
        self.centralwidget = QtWidgets.QWidget(UI_Catalogo)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 451, 451))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Minimize = QtWidgets.QPushButton(self.frame)
        self.Minimize.setGeometry(QtCore.QRect(400, 10, 21, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Minimize.setFont(font)
        self.Minimize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Minimize.setMouseTracking(True)
        self.Minimize.setStyleSheet("color:rgb(3, 95, 144);")
        self.Minimize.setFlat(True)
        self.Minimize.setObjectName("Minimize")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Exit = QtWidgets.QPushButton(self.frame)
        self.Exit.setGeometry(QtCore.QRect(420, 10, 21, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Exit.setFont(font)
        self.Exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Exit.setStyleSheet("background-color: rgb(229, 82, 2);\n"
"border-radius:10px;\n"
"color:rgb(3, 95, 144);")
        self.Exit.setFlat(True)
        self.Exit.setObjectName("Exit")
        self.Title = QtWidgets.QLabel(self.frame)
        self.Title.setGeometry(QtCore.QRect(190, 10, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setStyleSheet("color:rgb(229, 82, 2);")
        self.Title.setObjectName("Title")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(10, 60, 141, 22))
        self.comboBox.setStyleSheet("color: rgb(65, 65, 65);")
        self.comboBox.setCurrentText("")
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.User = QtWidgets.QLabel(self.frame)
        self.User.setGeometry(QtCore.QRect(20, 40, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.User.setFont(font)
        self.User.setStyleSheet("color:rgb(229, 82, 2);\n"
"")
        self.User.setObjectName("User")
        self.logo_label = QtWidgets.QLabel(self.frame)
        self.logo_label.setGeometry(QtCore.QRect(380, 40, 61, 61))
        self.logo_label.setStyleSheet("image:url(:/newPrefix/LoginLogo.png)")
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap("../Porojecto/View/logo.png"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setObjectName("logo_label")
        self.salaComboBox_1 = QtWidgets.QComboBox(self.frame)
        self.salaComboBox_1.setGeometry(QtCore.QRect(130, 110, 81, 23))
        self.salaComboBox_1.setStyleSheet("border:2px solid rgba(0,0,0,0);\n"
"color:rgb(3, 95, 144);\n"
"border-bottom-color: rgb(3, 95, 144);\n"
"padding-bottom:1px;")
        self.salaComboBox_1.setObjectName("salaComboBox_1")
        self.salaComboBox_1.addItem("")
        self.salaComboBox_1.addItem("")
        self.nome_utente_2 = QtWidgets.QLabel(self.frame)
        self.nome_utente_2.setGeometry(QtCore.QRect(50, 110, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nome_utente_2.setFont(font)
        self.nome_utente_2.setStyleSheet("color:rgb(3, 95, 144);")
        self.nome_utente_2.setObjectName("nome_utente_2")
        self.graficoStatistiche = QtWidgets.QLabel(self.frame)
        self.graficoStatistiche.setGeometry(QtCore.QRect(30, 180, 171, 181))
        self.graficoStatistiche.setStyleSheet("")
        self.graficoStatistiche.setText("")
        self.graficoStatistiche.setPixmap(QtGui.QPixmap("../Porojecto/View/logo.png"))
        self.graficoStatistiche.setScaledContents(True)
        self.graficoStatistiche.setObjectName("graficoStatistiche")
        self.graficoStatistiche_2 = QtWidgets.QLabel(self.frame)
        self.graficoStatistiche_2.setGeometry(QtCore.QRect(250, 180, 171, 181))
        self.graficoStatistiche_2.setStyleSheet("")
        self.graficoStatistiche_2.setText("")
        self.graficoStatistiche_2.setPixmap(QtGui.QPixmap("../Porojecto/View/logo.png"))
        self.graficoStatistiche_2.setScaledContents(True)
        self.graficoStatistiche_2.setObjectName("graficoStatistiche_2")
        self.dataFineButton_2 = QtWidgets.QToolButton(self.frame)
        self.dataFineButton_2.setGeometry(QtCore.QRect(240, 110, 141, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataFineButton_2.sizePolicy().hasHeightForWidth())
        self.dataFineButton_2.setSizePolicy(sizePolicy)
        self.dataFineButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dataFineButton_2.setStyleSheet("background-color:rgb(229, 82, 2);\n"
"border-radius:10px;\n"
"color:rgb(242,233,216);")
        self.dataFineButton_2.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.dataFineButton_2.setObjectName("dataFineButton_2")
        self.inserisci_button = QtWidgets.QPushButton(self.frame)
        self.inserisci_button.setGeometry(QtCore.QRect(310, 400, 111, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(242, 233, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(3, 95, 144))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 233, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 233, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(3, 95, 144))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(3, 95, 144))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 233, 216, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 233, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(3, 95, 144))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 233, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 233, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(3, 95, 144))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(3, 95, 144))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 233, 216, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 233, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(3, 95, 144))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 233, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 233, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(3, 95, 144))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(3, 95, 144))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 233, 216, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.inserisci_button.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.inserisci_button.setFont(font)
        self.inserisci_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.inserisci_button.setStyleSheet("background-color: rgb(3, 95, 144);\n"
"border-radius:10px;\n"
"color:rgb(242,233,216);")
        self.inserisci_button.setObjectName("inserisci_button")
        self.back_button = QtWidgets.QPushButton(self.frame)
        self.back_button.setGeometry(QtCore.QRect(10, 10, 31, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.back_button.setFont(font)
        self.back_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_button.setMouseTracking(True)
        self.back_button.setStyleSheet("border-image: url(:/newPrefix/back_button.png)")
        self.back_button.setText("")
        self.back_button.setFlat(True)
        self.back_button.setObjectName("Back")
        UI_Catalogo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(UI_Catalogo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 25))
        self.menubar.setObjectName("menubar")
        UI_Catalogo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(UI_Catalogo)
        self.statusbar.setObjectName("statusbar")
        UI_Catalogo.setStatusBar(self.statusbar)

        self.retranslateUi(UI_Catalogo)
        self.comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(UI_Catalogo)

    def retranslateUi(self, UI_Catalogo):
        _translate = QtCore.QCoreApplication.translate
        UI_Catalogo.setWindowTitle(_translate("UI_Catalogo", "MainWindow"))
        self.Minimize.setText(_translate("UI_Catalogo", "-"))
        self.Exit.setText(_translate("UI_Catalogo", "X"))
        self.Title.setText(_translate("UI_Catalogo", "Statistiche"))
        self.comboBox.setItemText(0, _translate("UI_Catalogo", "Home"))
        self.comboBox.setItemText(1, _translate("UI_Catalogo", "Logout"))
        self.User.setText(_translate("UI_Catalogo", "NOMEUTENTE"))
        self.salaComboBox_1.setItemText(0, _translate("UI_Catalogo", "Giorno"))
        self.salaComboBox_1.setItemText(1, _translate("UI_Catalogo", "Mese"))
        self.nome_utente_2.setText(_translate("UI_Catalogo", "Filtra per:"))
        self.dataFineButton_2.setText(_translate("UI_Catalogo", "Calendario"))
        self.inserisci_button.setText(_translate("UI_Catalogo", "Salva Grafici"))
import back_rc
import logo_rc
