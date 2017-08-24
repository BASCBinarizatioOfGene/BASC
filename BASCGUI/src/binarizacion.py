"""
============================================================
Authors: Helber Giovanny Sissa Becerra
         Tatiana Andrea Higuera Munevar
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The basc algorithms share the binarization in which a search
of the points is made which will be necessary to make the
graph
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
============================================================
"""

from src import BASCA, BASCB
import matplotlib.pyplot as plt


class Binarizacion():
    def __init__(self, tipo, datos):
        if tipo != None and datos != None:
            self.algoritmo = tipo
            if tipo == "BASCA":
                self.metodo = BASCA.BASCA(datos)
                self.size = len(datos) - 1
            elif tipo == "BASCB":
                self.metodo = BASCB.BASCB(datos)
                self.size = len(self.metodo.xPuntos) #- 1
            self.puntos = list()
            self.plot()

    def plot(self):

        H = [[0 for i in range(len(self.metodo.uSort) - 1)] for j in range(self.size)]
        s = 0
        for i in range(len(self.metodo.uSort) - 1):
            s += (self.metodo.uSort[i + 1] - self.metodo.uSort[i])

        maxY = 0
        for i in range(self.size - 2, -1, -1):
            for j in range(self.size - 2, -1, -1):
                if self.algoritmo == "BASCA":
                    H[i][j] = self.metodo.h[j][i] / self.metodo.hTotal[i]

                elif self.algoritmo == "BASCB":
                    H[i][j] = self.metodo.h[i][j] / self.metodo.hTotal[i - 1]
                maxY += H[i][j]

        for i in range(len(H[0]) - 1, -1, -1):
            H[-1][i] = (self.metodo.uSort[i + 1] - self.metodo.uSort[i]) / s
            # Calculate the H (weight) for the ordered input values
            # Calculate the intervals

        k = 0
        yActual = 0.5
        for i in range(len(H) - 1, -1, -1):
            if i < len(H) - 1:
                yActual += 1.9
                # Current steps and costs
            cActual = H[i]
            yPuntos = list()
            if self.algoritmo == "BASCA":

                x = self.metodo.xPuntos[i]

            elif self.algoritmo == "BASCB":
                x = self.metodo.xPuntos[k]

            for j in range(len(x) - 1):
                if j == 0:
                    yPuntos.append(yActual)
                    yPuntos.append(yActual)
                else:
                    yPuntos.append(yActual + sum(cActual[:j]))

            self.puntos.append((x, yPuntos))
            k += 1
        pass

        def getPuntos(self):
            return self.puntos
