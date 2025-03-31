"""Desenvolva um programa que leia seis números inteiros e mostre a soma
apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o."""

s = 0
for i in range(1, 7):
    valor = int(input('Digite um número inteiro: '))
    if valor % 2 == 0:
         s += valor
print('A somatória de todos os números PARES dentre os citados é igual a {}.'.format(s))
