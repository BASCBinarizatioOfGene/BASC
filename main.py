"""
============================================================
Authors: Helber Giovanny Sissa Becerra
         Tatiana Andrea Higuera Munevar
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Calling BASC algorithms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
main menu
============================================================
"""

import sys
import random
import BASCA, BASCB, Basc_Wavelet, Basc_Wavelet2

methods = ["BA", "BB", "BAH1", "BAH2", "ALL"]


def vector(N):
    v = []
    for k in range(N):
        v.append(round(random.uniform(0, 1), 3))
    return v


def main(method, lenVector):
    v = vector(lenVector)
    print("Vector: ", v)
    if method == "BA":
        algorithm = BASCA.BASCA(v)
    elif method == "BB":
        algorithm = BASCB.BASCB(v)
    elif method == "BAH1":
        algorithm = Basc_Wavelet.Basc_Wavelet(v)
        algorithm.bw_reconstruction()
    elif method == "BAH2":
        algorithm = Basc_Wavelet2.Basc_Wavelet2(v)
        algorithm.bw_reconstruction()
    if not method == "ALL":
        print("Vector Binario: ",algorithm.uBinario)
        print("Threshold: ",algorithm.t)
    else:
        algorithm = BASCA.BASCA(v)
        print("BASC A")
        print("Vector Binario: ", algorithm.uBinario)
        print("Threshold: ", algorithm.t)
        algorithm = BASCB.BASCB(v)
        print("BASC B")
        print("Vector Binario: ", algorithm.uBinario)
        print("Threshold: ", algorithm.t)
        algorithm = Basc_Wavelet.Basc_Wavelet(v)
        algorithm.bw_reconstruction()
        print("BASC HAAR 1")
        print("Vector Binario: ", algorithm.uBinario)
        print("Threshold: ", algorithm.t)
        algorithm = Basc_Wavelet2.Basc_Wavelet2(v)
        algorithm.bw_reconstruction()
        print("BASC HAAR 2")
        print("Vector Binario: ", algorithm.uBinario)
        print("Threshold: ", algorithm.t)

if len(sys.argv) == 3:

    if sys.argv[1] in methods:

        if sys.argv[2].isdigit():
            main(sys.argv[1], int(sys.argv[2]))
        else:
            print("The second parameter must be an integer")
    else:
        print("The first parameter must be a method of the following options: BA, BB, BAH1, BAH2, ALL")

else:
        print("This program needs two parameters: method and lenVector")
