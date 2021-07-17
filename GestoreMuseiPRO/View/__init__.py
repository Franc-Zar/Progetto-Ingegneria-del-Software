import sys
from PyQt5.QtWidgets import QApplication
from View.GestoreMuseiPRO import GestoreMuseiPRO

# main del programma
if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = GestoreMuseiPRO()
    view.show()
    sys.exit(app.exec_())