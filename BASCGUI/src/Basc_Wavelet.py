"""
============================================================
Authors: Helber Giovanny Sissa Becerra
         Tatiana Andrea Higuera Munevar
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The BASC algorithms are binarization techniques that aim
at determining a robust binarization by analyzing the data
at multiple scales
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Method: BASCHAAR1
============================================================
"""

import math
from sys import stdin

from pandas.io.sas.sas_constants import index


class Basc_Wavelet():


    def __init__(self, time_serie):
        self.time_serie = time_serie
        self._w0 = 0.5
        self._w1 = -0.5
        self._s0 = 0.5
        self._s1 = 0.5

    def bw_reconstruction(self):
        self.time_serie_increase_order = self.__increase_order__(self.time_serie)
        u = self.time_serie_increase_order[:]
        v = [None for i in range(len(self.time_serie_increase_order) - 1)]
        prind = []
        prindi=[]
        for i in range(len(self.time_serie_increase_order)-1):
            s, d , dmin, ind, indi = self.__wavelet_transform__(u)
            v[i] = ind
            u[indi] = s[indi]
            u[indi + 1] = s[indi]
            prind.append(ind)
            prindi.append(indi)
            pass

        vm = floorM = int(math.floor(median(v)))
        t = (self.time_serie_increase_order[floorM + 1] + self.time_serie_increase_order[floorM]) / 2
        uBinario = []
        strBinario = ""
        for i in self.time_serie:
            if i <= t:
                uBinario.append(0)
                strBinario += "0"
            else:
                strBinario += "1"
                uBinario.append(1)

        self.str_binario = strBinario
        self.t = t
        self.uBinario = uBinario

        pass

    def breakPoints(self):

        """
        This function compute the break points of all
        optimal step function

        Returns
        -------
        :return P : Array
                    The break points for optimal F function
        """
        P = [[-1 for i in range(len(self.time_serie ) >> 1)] for j in range(len(self.time_serie) >> 1)]
        for j in range(0, len(P)):
            z = j
            P[0][j] = self.Ind[0][z]
            if j > 0:
                z -= 1
                for i in range(1, j + 1):
                    P[i][j] = self.Ind[P[i - 1][j] + 1][z]
                    z -= 1
        return P
    def __increase_order__(self, time_serie):
        return  sorted(time_serie)

    def __wavelet_transform__(self, data):
        s = [None for i in range(len(data) - 1)]
        d = [None for i in range(len(data) - 1)]
        dmi = [float('inf') for i in range(len(data) - 1)]
        min_value = 0
        max_value = 0
        for i in range(len(s)-1):
            s[i] = (data[i] + data[i + 1]) * self._s1
            d[i] = (data[i] - data[i + 1]) * self._s1
            if d[i] != 0:
                dmi[i] = abs(d[i])

            if abs(d[i]) > abs(d[max_value]):
                max_value = i

            if abs(dmi[i]) < abs(dmi[min_value]):
                min_value = i

        return s, d, dmi, max_value, min_value


def median(V):
    """
    This function represents the value of the variable central
    position in a set of ordered data.

    Parameters
    ----------
    :param V: Array
              Vector that contain set of data

    Returns
    -------
    :return r : Integer
               Value that represent the median
    """
    V = sorted(V)
    x = int(len(V) / 2)
    x -= 1
    if len(V) % 2 == 0:
        r = (V[x] + V[x + 1]) / 2
    else:
        r = V[x + 1]
    return r
