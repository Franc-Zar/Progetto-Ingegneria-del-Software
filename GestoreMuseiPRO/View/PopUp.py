from PyQt5 import QtCore
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QDialog

# classe di base per la realizzazione di interfacce di tipo "pop-up"
class PopUp(QDialog):
  def __init__(self):
      super(PopUp, self).__init__()
      self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
      self.ui = None

  def setUi(self,ui):
      self.ui = ui

  def getUi(self):
      return self.ui

  def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

  def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()