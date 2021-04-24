from pyqrangeslider import QRangeSlider
from pyqrangeslider.qtcompat.QtWidgets import QApplication

app = QApplication([])

slider = QRangeSlider()
slider.setMinimum(0)
slider.setMaximum(100)
slider.setValue((20, 80))
slider.show()

app.exec_()
