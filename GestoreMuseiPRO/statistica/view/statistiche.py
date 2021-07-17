from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, FigureCanvasQTAgg, \
    NavigationToolbar2QT
from matplotlib.figure import Figure

from prenotazione.controller.ControllerPrenotazione import ControllerPrenotazione
from statistica.view.ViewStatistica import ViewStatistica


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(MplCanvas, self).__init__(self.fig)
        self.axes = self.fig.add_subplot(111)


class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        super().__init__(parent)
        self.canvas = MplCanvas(parent, width, height, dpi)
        self.setLayout(QtWidgets.QVBoxLayout())
        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        self.toolbar.setMinimumHeight(20)
        self.layout().addWidget(self.toolbar)
        self.layout().addWidget(self.canvas)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)


class UiStatistiche(object):
    def __init__(self):
        self.controller = ControllerPrenotazione()
        self.controller.verificaPrenotazioni()
        self.stats = ViewStatistica()

    def setupUi(self, UI_Statistiche):
        UI_Statistiche.setObjectName("UI_Statistiche")
        UI_Statistiche.resize(980, 830)
        UI_Statistiche.setStyleSheet("background-color: rgb(242,233,216)")

        self.centralWidget = QtWidgets.QWidget(UI_Statistiche)
        self.centralWidget.setObjectName("centralWidget")
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 951, 801))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.minimizeButton = QtWidgets.QPushButton(self.frame)
        self.minimizeButton.setGeometry(QtCore.QRect(900, 10, 21, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.minimizeButton.setFont(font)
        self.minimizeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minimizeButton.setMouseTracking(True)
        self.minimizeButton.setStyleSheet("color:rgb(3, 95, 144);")
        self.minimizeButton.setFlat(True)
        self.minimizeButton.setObjectName("minimizeButton")

        self.closeButton = QtWidgets.QPushButton(self.frame)
        self.closeButton.setGeometry(QtCore.QRect(920, 10, 21, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.closeButton.setFont(font)
        self.closeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeButton.setStyleSheet("background-color: rgb(229, 82, 2);\n"
                                       "border-radius:10px;\n"
                                       "color:rgb(3, 95, 144);")
        self.closeButton.setFlat(True)
        self.closeButton.setObjectName("closeButton")

        self.titleLabel = QtWidgets.QLabel(self.frame)
        self.titleLabel.setGeometry(QtCore.QRect(390, 10, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("color:rgb(229, 82, 2);")
        self.titleLabel.setObjectName("titleLabel")

        self.accountMenu = QtWidgets.QComboBox(self.frame)
        self.accountMenu.setGeometry(QtCore.QRect(10, 60, 141, 22))
        self.accountMenu.setStyleSheet("color: rgb(65, 65, 65);")
        self.accountMenu.setCurrentText("")
        self.accountMenu.setFrame(True)
        self.accountMenu.setObjectName("comboBox")
        self.accountMenu.addItem("")
        self.accountMenu.addItem("")

        self.userLabel = QtWidgets.QLabel(self.frame)
        self.userLabel.setGeometry(QtCore.QRect(20, 40, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.userLabel.setFont(font)
        self.userLabel.setStyleSheet("color:rgb(229, 82, 2);")
        self.userLabel.setObjectName("userLabel")

        self.logoLabel = QtWidgets.QLabel(self.frame)
        self.logoLabel.setGeometry(QtCore.QRect(880, 40, 61, 61))
        self.logoLabel.setStyleSheet("image:url(:/newPrefix/LoginLogo.png)")
        self.logoLabel.setText("")
        # self.logoLabel.setPixmap(QtGui.QPixmap("../Porojecto/View/logo.png"))
        self.logoLabel.setScaledContents(True)
        self.logoLabel.setObjectName("logoLabel")

        self.filtroComboBox = QtWidgets.QComboBox(self.frame)
        self.filtroComboBox.setGeometry(QtCore.QRect(130, 110, 81, 23))
        self.filtroComboBox.setStyleSheet("border:2px solid rgba(0,0,0,0);\n"
                                          "color:rgb(3, 95, 144);\n"
                                          "border-bottom-color: rgb(3, 95, 144);\n"
                                          "padding-bottom:1px;")
        self.filtroComboBox.setObjectName("filtroComboBox")
        self.filtroComboBox.addItem("")
        self.filtroComboBox.addItem("")

        self.textLabel = QtWidgets.QLabel(self.frame)
        self.textLabel.setGeometry(QtCore.QRect(50, 115, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.textLabel.setFont(font)
        self.textLabel.setStyleSheet("color:rgb(3, 95, 144);")
        self.textLabel.setObjectName("textLabel")

        self.imgFrame = QtWidgets.QFrame(self.frame)
        self.imgFrame.setGeometry(QtCore.QRect(10, 150, 950, 600))

        self.canvas_1 = MplWidget()
        self.canvas_2 = MplWidget()

        self.layout = QtWidgets.QVBoxLayout(self.imgFrame)
        self.layout.addWidget(self.canvas_1)
        self.layout.addWidget(self.canvas_2)
        self.imgFrame.setLayout(self.layout)

        self.dataButton = QtWidgets.QToolButton(self.frame)
        self.dataButton.setGeometry(QtCore.QRect(240, 105, 141, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataButton.sizePolicy().hasHeightForWidth())
        self.dataButton.setSizePolicy(sizePolicy)
        self.dataButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dataButton.setStyleSheet("background-color:rgb(229, 82, 2);\n"
                                      "border-radius:10px;\n"
                                      "color:rgb(242,233,216);")
        self.dataButton.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.dataButton.setMenu(QtWidgets.QMenu(self.dataButton))
        self.calendar = QtWidgets.QCalendarWidget(self.frame)
        self.calendar.setStyleSheet("background-color: rgb(242,233,216); color: rgb(3, 95, 144);")
        action = QtWidgets.QWidgetAction(self.dataButton)
        action.setDefaultWidget(self.calendar)
        self.dataButton.menu().addAction(action)
        self.dataButton.setObjectName("dataButton")
        self.calendar.selectionChanged.connect(self.display)


        self.backButton = QtWidgets.QPushButton(self.frame)
        self.backButton.setGeometry(QtCore.QRect(10, 10, 31, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.backButton.setFont(font)
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.setMouseTracking(True)
        self.backButton.setStyleSheet("border-image: url(:/newPrefix/back_button.png)")
        self.backButton.setText("")
        self.backButton.setFlat(True)
        self.backButton.setObjectName("backButton")

        UI_Statistiche.setCentralWidget(self.centralWidget)
        self.menubar = QtWidgets.QMenuBar(UI_Statistiche)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 25))
        self.menubar.setObjectName("menubar")
        UI_Statistiche.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(UI_Statistiche)
        self.statusbar.setObjectName("statusbar")
        UI_Statistiche.setStatusBar(self.statusbar)
        self.retranslateUi(UI_Statistiche)
        self.accountMenu.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(UI_Statistiche)

    def retranslateUi(self, UI_Statistiche):
        _translate = QtCore.QCoreApplication.translate
        UI_Statistiche.setWindowTitle(_translate("UI_Statistiche", "Statistiche"))
        self.minimizeButton.setText(_translate("UI_Statistiche", "-"))
        self.closeButton.setText(_translate("UI_Statistiche", "X"))
        self.titleLabel.setText(_translate("UI_Statistiche", "Statistiche"))
        self.accountMenu.setItemText(0, _translate("UI_Statistiche", "Home"))
        self.accountMenu.setItemText(1, _translate("UI_Statistiche", "Logout"))
        self.userLabel.setText(_translate("UI_Statistiche", "NOMEUTENTE"))
        self.filtroComboBox.setItemText(0, _translate("UI_Statistiche", "Giorno"))
        self.filtroComboBox.setItemText(1, _translate("UI_Statistiche", "Mese"))
        self.textLabel.setText(_translate("UI_Statistiche", "Filtra per:"))
        self.dataButton.setText(_translate("UI_Statistiche", "Calendario"))

    def display(self):
        data = self.calendar.selectedDate()
        if self.filtroComboBox.currentIndex():
            try:
                fig = self.stats.visiteMensili(data.toString('yyyy-MM-dd'))
                fig.set_figheight(2)
                fig.set_figwidth(9)
                self.canvas_1.canvas.figure.clear()
                self.canvas_1.canvas.figure = fig
                self.canvas_1.canvas.figure.tight_layout()
                self.canvas_1.canvas.draw()
                fig = self.stats.disdetteMensili(data.toString('yyyy-MM-dd'))
                fig.set_figheight(2)
                fig.set_figwidth(9)
                self.canvas_2.canvas.figure.clear()
                self.canvas_2.canvas.figure = fig
                self.canvas_2.canvas.figure.tight_layout()
                self.canvas_2.canvas.draw()
            except Exception as e:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("Errore")
                msg.setInformativeText('Caricamento statistiche fallito')
                print(e.args)
                msg.setWindowTitle("Error")
                msg.exec_()
        else:
            try:
                fig = self.stats.visiteGiornaliere(data.toString('yyyy-MM-dd'))
                fig.set_figheight(2)
                fig.set_figwidth(9)
                self.canvas_1.canvas.figure.clear()
                self.canvas_1.canvas.figure = fig
                self.canvas_1.canvas.figure.tight_layout()
                self.canvas_1.canvas.draw()
                fig = self.stats.disdetteGiornaliere(data.toString('yyyy-MM-dd'))
                fig.set_figheight(2)
                fig.set_figwidth(9)
                self.canvas_2.canvas.figure.clear()
                self.canvas_2.canvas.figure = fig
                self.canvas_2.canvas.figure.tight_layout()
                self.canvas_2.canvas.draw()
            except Exception as e:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("Errore")
                msg.setInformativeText('Caricamento statistiche fallito')
                print(e.args)
                msg.setWindowTitle("Error")
                msg.exec_()
