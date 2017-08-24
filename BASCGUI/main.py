"""
============================================================
Authors: Helber Giovanny Sissa Becerra
         Tatiana Andrea Higuera Munevar
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
============================================================
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from Widgets.window import Window
import sys

#app = QtGui.QGuiApplication(sys.argv)
app= QtWidgets.QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())