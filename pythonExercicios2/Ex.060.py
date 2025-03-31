"""Faça um programa que leia um número qualquer e mostre o seu fatorial."""

n = int(input('Digite um número inteiro para calcular seu fatorial: '))
f = n
while n != 1:
    n = n-1
    f = f * n
print("{}! = {}".format(n, f))

"""or 
from math import factorial
n = int(input('Digite um número para calcular seu fatorial: ))
f = factorial(n)
print('O fatorial de {} é {}.'. format(n, f)"""