from time import time

import sys

from src import BASCA
from src import BASCB
from src import Basc_Wavelet as bw
from src import Basc_Wavelet2 as bw2

import random


def vector(i, N, a):
    f = open("test_" + str(i) + ".in", "a")
    f.seek(0)
    for j in range(a):
        for k in range(N):
            f.write(str(round(random.uniform(0, 1), 3)) + " ")

        f.write("\n")




def encontrar_diferencias(strbinario1, strbinario2):
    diff = bin(int(strbinario1,2) ^ int(strbinario2,2))
    r = len(strbinario1) - diff.count("1")
    return r


def parseStr(tmp):
    resp = ""
    for i in tmp:
        resp += str(i)
    return resp


def stepFuntions(i):
    #cant = [(2 ** 5), (2 ** 6), (2 ** 7), (2 ** 8), (2 ** 9), (2 ** 10), (2 ** 11), (2 ** 12), (2 ** 13), (2 ** 14),(2 ** 15), (2 ** 16)]
    cant = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000]
    print(len(cant))
    cont = 5
    for n in cant:
        vector(i, n, cont)


#stepFuntions("tiempo")

def prueba(i):

    """
    # Archivo para guardar las comparaciones
    f1 = open("test_BASCAvsBASCB_" + str(i) + ".out", "w")
    f1.write("Prueba " + str(i) + "  --> BASCA vs BASCB" + "\n")
    f1.write("caso  ;   th BASCA     ;  th BASCB    ;   logintud vector ;   diff   ;  time_BASCA   ; time_BASCB" + "\n")

    f2 = open("test_BASCAvsBASCHAAR1_" + str(i) + ".out", "w")
    f2.write("Prueba " + str(i) + "  --> BASCA vs BASCHAAR1" + "\n")
    f2.write("caso  ;   th BASCA    ;   th BASCHAAR1    ;   logintud vector ;   diff  ;  time_BASCA   ; time_BASCHAAR1" + "\n")


    f3 = open("test_BASCAvsBASCHAAR2_" + str(i) + ".out", "w")
    f3.write("Prueba " + str(i) + "  --> BASCA vs BASCHAAR2" + "\n")
    f3.write("caso   ;  th BASCA    ;   th BASCHAAR2    ;   logintud vector ;   diff  ;  time_BASCA   ; time_BASCHAAR2" + "\n")


    f1.close()
    f2.close()
    f3.close()

    """
    #stepFuntions(i)
    test = 421

    #Archivo que contiene los step funtions
    archivo = open("test_" + str(i) + ".in", "r")

    #archivos que guarda las comparaciones

    for linea in archivo.readlines():
        f1 = open("test_BASCAvsBASCB_" + str(i) + ".out", "a")
        f2 = open("test_BASCAvsBASCHAAR1_" + str(i) + ".out", "a")
        f3 = open("test_BASCAvsBASCHAAR2_" + str(i) + ".out", "a")
        contenido = [float(x) for x in linea.strip().split()]
        print(contenido)
        #llamado a todos metodos
        try:
            #BASCA
            tiempo_inicial = time()
            a = BASCA.BASCA(contenido)
            tiempo_final = time()
            tiempo_ejecucion_BASCA = tiempo_final - tiempo_inicial

            #BASCB
            tiempo_inicial = time()
            b = BASCB.BASCB(contenido)
            tiempo_final = time()
            tiempo_ejecucion_BASCB = tiempo_final - tiempo_inicial

            #BASCHAAR1
            tiempo_inicial = time()
            bwa = bw.Basc_Wavelet(contenido)
            bwa.bw_reconstruction()
            tiempo_final = time()
            tiempo_ejecucion_BASCHAAR1 = tiempo_final - tiempo_inicial

            #BASCHAAR2
            tiempo_inicial = time()
            bwb = bw2.Basc_Wavelet2(contenido)
            bwb.bw_reconstruction()
            tiempo_final = time()
            tiempo_ejecucion_BASCHAAR2 = tiempo_final - tiempo_inicial


        except:
            print(str(sys.exc_info()[0])+" error "+str(test))

        #COMPARACIONES
        try:

            #BASCA vs BASCB
            f1.write(str(test) + "     ;"+str(round(a.t,3)) + "           ;"+str(round(b.t, 3)) + "         ;" + str(len(contenido)) + "                 ;"
                     + str(encontrar_diferencias(parseStr(a.uBinario), parseStr(b.uBinario)))+ "    ;   " +
                     str(tiempo_ejecucion_BASCA) + "    ;   " + str(tiempo_ejecucion_BASCB) + "\n")

            #BASCA vs BASCHAAR1
            f2.write(str(test) + "     ;" + str(round(a.t,3)) + "          ;" + str(round(bwa.t, 3)) + "              ;" + str(len(contenido)) + "                 ;"
                     + str(encontrar_diferencias(parseStr(a.uBinario), parseStr(bwa.uBinario))) + "    ;   " +
                     str(tiempo_ejecucion_BASCA) + "    ;   " + str(tiempo_ejecucion_BASCHAAR1) + "\n")

            #BASCA vs BASCHAAR2
            f3.write(str(test) + "     ;" + str(round(a.t,3)) + "          ;" + str(round(bwb.t, 3)) + "              ;" + str(len(contenido)) + "                 ;"
                     + str(encontrar_diferencias(parseStr(a.uBinario), parseStr(bwb.uBinario))) +  "    ;   " +
                     str(tiempo_ejecucion_BASCA) + "    ;   " + str(tiempo_ejecucion_BASCHAAR2) + "\n")
        except:
            pass
        test += 1
        f1.close()
        f2.close()
        f3.close()



def main():
    name_file = "tiempo"

    #Calcula
    stepFuntions(name_file)

    prueba(name_file)


main()