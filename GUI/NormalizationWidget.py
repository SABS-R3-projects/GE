from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QSizePolicy, QSpacerItem, QVBoxLayout

class NormalizationWidget(QWidget):
    def __init__(self, minimum=0, maximum=1.5):
        _translate = QtCore.QCoreApplication.translate
        super(NormalizationWidget, self).__init__()
        self.layout = QtWidgets.QVBoxLayout(self)
        self.tabWidget = QtWidgets.QTabWidget()
        self.tabWidget.setObjectName("tabWidget")
        self.layout.addWidget(self.tabWidget)
        self.minimum = minimum
        self.maximum = maximum
        self.intensity = None
        self.verticalLayout = QVBoxLayout()
        spacerItem = QSpacerItem(30, 550, QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.layout.addItem(spacerItem)

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, 'Log Adjust')
        self.tab_layout = QtWidgets.QVBoxLayout(self.tab)

        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("Log")
        # self.label.setText(_translate("MainWindow", "Adjust Intensity"))
        self.tab_layout.addWidget(self.label)

        self.horizontalSlider_2 = QtWidgets.QSlider(self.tab)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_2.setMinimum(0)
        self.tab_layout.addWidget(self.horizontalSlider_2)
        self.horizontalSlider_2.valueChanged.connect(self.update_intensity)
        self.update_intensity(self.horizontalSlider_2.value())

    def update_intensity(self, value):
        self.intensity = (self.minimum + (
                    float(value) / (self.horizontalSlider_2.maximum() - self.horizontalSlider_2.minimum())) * (
                                  self.maximum - self.minimum))
        self.label.setText("Intensity Level: {0:.1f}".format(self.intensity))
        #BrainData.intensity = 5

