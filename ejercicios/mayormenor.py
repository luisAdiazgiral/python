# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 19:50:53 2018

@author: desha
"""

def max(n1,n2):
    if (n1>n2):
        print ("El numero " , n1 , " es mayor que el numero ", n2, "\n")
    else:
        if (n2>n1):
            print ("El numero " , n2 , " es mayor que el numero ", n1, "\n") 
        else:
            print ("Los numeros son iguales \n")

print ("Programa de comparacion mayor menor \n")
n1=int(input("Ingrese un numero para comparar \n"))
n2=int(input("Ingrese un numero para comparar \n"))
max(n1,n2)