from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QSizePolicy, QSpacerItem, QVBoxLayout


class NormalizationWidget(QWidget):
    """
    A class that creates the Intensity Normalization widget that appears when Adjust Intensity option
    under the Tools menu bar is clicked
    """
    def __init__(self, viewer, minimum=0.5, maximum=1.6):
        self.win = viewer
        self.brain = viewer.brain

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
        self.label.setText(_translate("MainWindow", "Adjust Intensity"))
        self.tab_layout.addWidget(self.label)

        self.log_intensity_slider = QtWidgets.QSlider(self.tab)
        self.log_intensity_slider.setOrientation(QtCore.Qt.Horizontal)
        self.log_intensity_slider.setObjectName("log_intensity_slider")
        self.log_intensity_slider.setMinimum(0)
        self.log_intensity_slider.setValue(1)
        self.tab_layout.addWidget(self.log_intensity_slider)
        self.log_intensity_slider.valueChanged.connect(self.update_intensity)

    def update_intensity(self):
        """
        A Method that keeps track of the intensity values displayed on the Logarithmic Intensity Widget
        It updates the appearance of the brain on the viewer as intensity is changed
        """
        # Take input from controller
        value = self.log_intensity_slider.value()
        self.brain.intensity = (self.minimum + (
                float(value) / (self.log_intensity_slider.maximum() - self.log_intensity_slider.minimum())) * (
                                        self.maximum - self.minimum))
        # Edit the Brain Data Using function defined in BrainData class
        self.brain.log_normalization()
        # Update what you are displaying
        self.label.setText("Intensity Level: {0:.1f}".format(self.brain.intensity))
        self.win.refresh_image()