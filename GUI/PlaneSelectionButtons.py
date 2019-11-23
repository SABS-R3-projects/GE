from PyQt5.QtWidgets import QVBoxLayout, QWidget, QPushButton
from pyqtgraph.Qt import QtCore, QtGui


class PlaneSelectionButtons(QWidget):
    def __init__(self, button1, button2, button3, parent=None):
        super(PlaneSelectionButtons, self).__init__(parent=parent)

        self.layout = QVBoxLayout(self)
        self.btn1 = QPushButton()
        self.btn1.setIcon(QtGui.QIcon('one.png'))
        self.btn1.setIconSize(QtCore.QSize(100, 100))
        self.btn2 = QPushButton()
        self.btn2.setIcon(QtGui.QIcon('button2.png'))
        self.btn2.setIconSize(QtCore.QSize(100, 100))
        self.btn3 = QPushButton()
        self.btn3.setIcon(QtGui.QIcon('button3.png'))
        self.btn3.setIconSize(QtCore.QSize(100, 100))

        self.btn1.setFixedSize(120, 120)
        self.btn2.setFixedSize(120, 120)
        self.btn3.setFixedSize(120, 120)

        self.layout.addWidget(self.btn1)
        self.layout.addWidget(self.btn2)
        self.layout.addWidget(self.btn3)
        self.layout.setSpacing(20)

        self.btn1.clicked.connect(button1)
        self.btn2.clicked.connect(button2)
        self.btn3.clicked.connect(button3)