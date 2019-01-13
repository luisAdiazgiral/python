# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 17:45:02 2018

@author: desha
"""


def suma(n1,n2):
    resultado = n1+n2
    print("el resultado de la suma es", resultado, "\n")
def resta(n1,n2):
    resultado=(n1-n2)
    print("el resultado de la resta es", resultado, "\n")
def multiplica(n1,n2):
    resultado=(n1*n2)
    print("el resultado de la multiplicacion es", resultado, "\n")
def divide(n1,n2):
    if (n2==0):
            print ("no se puede dividir por cero", "\n")
    else:
            resultado=(n1/n2)
            print("el resultado de la division es", resultado, "\n")
print("bienvenido al programa de operatorias")
print("1-- suma")
print("2-- resta")
print("3-- multiplicacion")
print("4-- division")
print("")
op=int(input("selecciones una opcion \n"))        
n1=int(input("ingrese un numero para la operacion seleccionada \n"))
n2=int(input("ingrese un numero para la operacion seleccionada \n"))
if (op==1):
    suma(n1,n2)
if (op==2):
    resta(n1,n2)
if (op==3):
    multiplica(n1,n2)
if (op==4):
    divide(n1,n2)
