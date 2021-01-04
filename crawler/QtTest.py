import sys
from PyQt5 import QtWidgets, QtCore
app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(400, 400)
widget.setWindowTitle('Hello World')
widget.show()
sys.exit(app.exec__())
