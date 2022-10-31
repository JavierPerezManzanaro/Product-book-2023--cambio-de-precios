#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re
import os


PORCENTAJE = 1.05
PATRON_SIMPLE = '(>[0-9]* €)'
PATRON_COMPUESTO = '([0-9]*\.[0-9]* €)'

# https://docs.python.org/es/3/library/re.html#making-a-phonebook


def manipulado(valor):
    valor = valor * PORCENTAJE
    valor = math.ceil(valor)
    valor = valor + 2.5
    valor = valor - (valor % 5)
    valor = int(valor)
    return valor


if __name__ == '__main__':

    os.system('clear')

    nombre_fichero = input('Nombre del fichero "idms" para modificar (sin extensión): ')
    fichero = nombre_fichero + '.idms'

    contenido = list()

    with open(fichero, 'r') as archivo:
        for linea in archivo:

            # * menos de mil
            ocurrencia = re.findall(PATRON_SIMPLE, linea)
            if ocurrencia:
                cifra = ocurrencia[0].split()
                cifra = cifra[0][1:]
                cifra = int(cifra)
                print()
                cifra_manipulada = manipulado(cifra)
                cifra_manipulada = '>' + str(cifra_manipulada) + ' €'
                print(f'Se ha encontrado: {ocurrencia} y pasa a ser {cifra_manipulada}')
                #print(f'{ocurrencia[0]=}')
                linea = linea.replace(ocurrencia[0], cifra_manipulada)

            # * mas de mil
            ocurrencia = re.findall(PATRON_COMPUESTO, linea)
            if ocurrencia:
                cifra = ocurrencia[0].split()
                cifra = cifra[0].replace('.', '')
                cifra = int(cifra)
                print()
                cifra_manipulada = manipulado(cifra)
                cifra_manipulada = str(cifra_manipulada)
                if len(cifra_manipulada) > 5:
                    print('Error!!!!')
                cifra_manipulada = \
                    cifra_manipulada[0:(len(cifra_manipulada)-3)] + '.' + cifra_manipulada[-3:] + ' €'
                print(f'Se ha encontrado: {ocurrencia} y pasa a ser {cifra_manipulada}')
                linea = linea.replace(ocurrencia[0], cifra_manipulada)

            contenido.append(linea)

        fichero = nombre_fichero + ' mod.idms'
        with open(fichero, 'w') as archivo:
            archivo.write("".join(contenido))
            archivo.close()
