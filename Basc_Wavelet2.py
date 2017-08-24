"""
============================================================
Authors: Helber Giovanny Sissa Becerra
         Tatiana Andrea Higuera Munevar
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The BASC algorithms are binarization techniques that aim
at determining a robust binarization by analyzing the data
at multiple scales
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Method: BASCHAAR2
============================================================
"""

import math
from sys import stdin

class Basc_Wavelet2():


    def __init__(self, time_serie):
        self.time_serie = time_serie
        self._w0 = 0.5
        self._w1 = -0.5
        self._s0 = 0.5
        self._s1 = 0.5

    def bw_reconstruction(self):
        self.time_serie_increase_order = self.__increase_order__(self.time_serie)
        P = [i for i in range(len(self.time_serie))]
        u = self.time_serie_increase_order[:]
        v = []
        while len(P) > 3:
            s, join = self.__wavelet_transform__(u)
            aux1 = self.__find_pos__(u, join)
            for i in range(len(aux1)):
                u[aux1[i]] = s[join]
            break_point = self.__find_break_point__(P, join)
            if len(P) > break_point:
                P = P[:break_point]+P[break_point+1:]
            else:
                break
            #Compute score breakpoints
            q = [None for i in range(len(self.time_serie))]
            h = self.__mean__(self.time_serie_increase_order[P[0]+1:P[1]+1]) - self.__mean__(self.time_serie_increase_order[0:P[1]+1])
            z = (self.time_serie_increase_order[P[0]] + self.time_serie_increase_order[P[1]])/ 2
            e = self.__norm__(self.time_serie_increase_order,z)
            q[0] = h/e
            ind = 0
            for i in range(1, len(P) - 1):
                h = self.__mean__(self.time_serie_increase_order[P[i] + 1:P[i+1]+1 ]) - self.__mean__(
                    self.time_serie_increase_order[P[i-1]+1:P[i]+1])
                z = (self.time_serie_increase_order[P[i]] + self.time_serie_increase_order[P[i]+1]) / 2
                e = self.__norm__(self.time_serie_increase_order, z)
                q[i] = h / e
                #find index of strongest discontinuity
                if q[i] > q[ind]:
                    ind = i
            v.append(P[ind])

        #last jump
        s, join = self.__wavelet_transform__(u)
        aux1 = self.__find_pos__(u, join)
        floorM = int(math.floor(median(v)))
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

    def __norm__(self, f, z):
        e = 0
        for i in range(len(f)):
            e += math.pow(f[i] - z ,2)
        return e

    def __mean__(self, f):
        r = 0
        tmp_sum = 0
        for i in range(len(f)):
            tmp_sum += f[i]
        r = tmp_sum/len(f)
        return r
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
        return sorted(time_serie)

    def __find_pos__(self, time_serie, value):
        tmp = []
        for i in range(len(time_serie)):
            if time_serie[i] == time_serie[value] or time_serie[i] == time_serie[value + 1]:
                tmp.append(i)

        return tmp

    def __find_break_point__(sefl, p_values, index):
        min_ind = float('inf')
        for i in range(len(p_values)):
            if p_values[i] == index and i < min_ind:
                min_ind = i
        return min_ind

    def __wavelet_transform__(self, data):
        s = [None for i in range(len(data) - 1)]
        d = [None for i in range(len(data) - 1)]
        dmi = [float('inf') for i in range(len(data) - 1)]
        min_value = 0
        max_value = 0
        for i in range(len(s)):
            s[i] = (data[i] + data[i + 1]) * self._s1
            d[i] = (data[i] - data[i + 1]) * self._s1
            if d[i] != 0:
                dmi[i] = d[i]

            if abs(d[i]) > abs(d[max_value]):
                max_value = i

            if abs(dmi[i]) < abs(dmi[min_value]):
                min_value = i

        return s, min_value


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


