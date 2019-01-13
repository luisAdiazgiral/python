#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo que contiene funciones para crear la serie de Fibonacci
Permite ejecutar el módulo como script

@author: Roberto Muñoz
"""


def suma(x,y):
    """ Imprime en pantalla la serie Fibonacci hasta n """
    suma=x+y
    print(suma)
   
x = int(input("difgite un numero 1 :  "))
y = int(input("difgite un numero 2 :  "))
suma(x,y)