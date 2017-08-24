"""
============================================================
Authors: Helber Giovanny Sissa Becerra
         Tatiana Andrea Higuera Munevar
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Window is designed with the purpose of providing the user
with a pleasant interface and simple operation of the two
algorithms of BASC, offering the user different behaviors
with which to work and perform an analysis of the algorithms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Interface
"""

import matplotlib.pyplot as plt
import settings
import os
from UI.mainwindow import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from src import binarizacion
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class Window(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        settings.configuration(self)

        self.currentAlgorithm = ""
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.data = list()
        self.genes = list()
        self.ui.progressBar.hide()
        self.ui.cbseleccionarAlgoritmo.addItems(["BASCA", "BASCB"])
        self.ui.cbVisualizacion.addItems(["Step by step", "Final result", "Compare"])
        self.figure = plt.figure()
        self.ui.canvas = FigureCanvas(self.figure)
        self.ui.toolbar = NavigationToolbar(self.ui.canvas, self)
        self.ui.grafica.addWidget(self.ui.toolbar)
        self.ui.grafica.addWidget(self.ui.canvas)
        self.ui.cargarArchivo.clicked.connect(self.cargarArchivo)
        self.ax = self.figure.add_subplot(111)
        self.resultadoBinarizacion = binarizacion.Binarizacion(None, None)
        self.ui.procesar.clicked.connect(self.procesar)
        self.btn_save = QtWidgets.QPushButton("Save >>")
        self.ui.toolbar.addWidget(self.btn_save)
        self.btn_save.clicked.connect(self.save)
        pass

    def cargarArchivo(self):
        """
        This function is designed to be able to easily load
        the file that will contain the data of the gene that
        the user wants to process.
        """
        print("cargar Archivo")
        self.data = list()

        file = QFileDialog.getOpenFileName(self, 'Open file', '/', "Image files (*.in)")[0]

        self.ui.pathFile.clear()
        self.ui.pathFile.insertPlainText(file)
        genes = []
        self.genes = []
        if file != "":
            self.file = file
            ff = open(file)
            l = ff.readlines()
            genes = []
            nGen = 0
            for e in l:
                self.data.append(e.strip().split())
                nGen += 1
                genes.append("Gene " + str(nGen))

            ff.close()

            self.genes = [None for i in range(len(genes))]
            self.ui.cbGenes.clear()
            self.ui.cbGenes.addItems(genes)

    def procesar(self):
        """
        This function processes the file previously loaded,
        with the algorithm selected, the display mode and
        the gene that you want to be plotted.

        """
        print("procesar")
        opcionSelccionada = self.ui.cbseleccionarAlgoritmo.currentText()
        modoVisualizacion = self.ui.cbVisualizacion.currentText()
        genVisualizacion = int(self.ui.cbGenes.currentText().split()[1]) - 1

        try:
            gen = self.genes[genVisualizacion]

            # validar que no se ha procesado el gen o que el algoritmo a utilizar sea otro
            if gen == None or  opcionSelccionada != self.currentAlgorithm:
                self.currentAlgorithm = opcionSelccionada
                data = self.data[genVisualizacion]
                if len(data) == 0: raise Exception("Don't found file")
                if 1 <= len(data) < 3: raise Exception("The input vector must have at least 3 entries!")

                for i in range(len(data)):
                    # tmp Contains a set of Gene
                    tmp = [float(data[k]) for k in range(len(data))]
                    self.resultadoBinarizacion = binarizacion.Binarizacion(opcionSelccionada, tmp)
                self.genes.insert(genVisualizacion, self.resultadoBinarizacion)
            else:
                self.resultadoBinarizacion = self.genes[genVisualizacion]

            if modoVisualizacion == 'Step by step':
                graficasAmostrar = 0
                graficasAmostrarFinal = len(self.resultadoBinarizacion.puntos)
            elif modoVisualizacion == "Final result":
                graficasAmostrar = len(self.resultadoBinarizacion.puntos) - 1
                graficasAmostrarFinal = len(self.resultadoBinarizacion.puntos)
            elif modoVisualizacion == "comparacion":
                graficasAmostrar = 0
                graficasAmostrarFinal = 0

            self.ax.hold(False)

            if modoVisualizacion == "Compare":
                x = self.resultadoBinarizacion.puntos[0][0]
                y = self.data[genVisualizacion][:]
                y.insert(0, 0)
                self.ax.plot(x, y, drawstyle='steps')
                self.ui.canvas.draw()
                self.ax.hold(True)
                yTh = [self.resultadoBinarizacion.metodo.t, self.resultadoBinarizacion.metodo.t]
                xTh = [0, len(y) - 1]
                self.ax.plot(xTh, yTh)

                pass

            for i in range(graficasAmostrar, graficasAmostrarFinal):
                x = self.resultadoBinarizacion.puntos[i][0]
                y = self.resultadoBinarizacion.puntos[i][1]

                self.ax.plot(x, y, drawstyle='steps')
                if graficasAmostrar == len(self.resultadoBinarizacion.puntos) - 1:
                    self.ax.hold(False)
                else:
                    self.ax.hold(True)

            self.ui.canvas.draw()
            self.ui.thValue.setText(str(self.resultadoBinarizacion.metodo.t))
            self.ui.vectoBinarizado.setText(str(self.resultadoBinarizacion.metodo.uBinario))

        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error", e(0))
            pass

    def save(self):
        """
        This function will save the data in a pdf extension
        file which will contain the information of the processed
        gene, the respective current visualization being
        performed, the binarized vector and the Threshold
        """

        path = os.getcwd().replace('\\', '/')
        ruta = path + "//Formulario.pdf"

        genVisualizacion = int(self.ui.cbGenes.currentText().split()[1]) - 1
        data = self.data[genVisualizacion]
        nombreArchivo = 'datos.pdf'
        self.figure.savefig("output.png")
        logo = "./output.png"
        c = canvas.Canvas(ruta, pagesize=letter)
        width, height = letter
        encabezado = 'Escuela Colombian de Ingenería Julio Garavito'

        c.drawString(100, 700, encabezado)
        c.drawString(100, 650, 'Gene: ' + str(data))
        c.drawImage(logo, 40, 300, 600)  # Who needs consistency?

        c.drawString(100, 250, 'Binarized vector: ' + str(self.resultadoBinarizacion.metodo.uBinario))
        c.drawString(100, 200, 'Threshold: ' + str(self.resultadoBinarizacion.metodo.t))
        c.save()
        print("Path: "+ruta)
        os.system(ruta+" &")

