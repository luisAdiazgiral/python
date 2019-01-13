#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo que contiene funciones para crear la serie de Fibonacci
Permite ejecutar el módulo como script

@author: Roberto Muñoz
"""


def suma(x,y):
    """ Imprime en pantalla la serie Fibonacci hasta n """
    sumar=x+y
    return sumar 

def multi(x,y):
    multiplicar = x * y
    return multiplicar

def divi(x,y):
    dividir = int(x / y)
    return dividir

x = int(input("difgite un numero 1 :  "))
y = int(input("difgite un numero 2 :  "))
resultado=suma(x,y)
res_multi=multi(x,y)
res_divi = divi(x,y)

print ("El resultado de la suma es : " , resultado)
print ("el resultado de la multiplicacion es : " ,  res_multi)
print ("El resultado de la division es : " , res_divi)