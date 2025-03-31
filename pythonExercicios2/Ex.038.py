"""Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
-O primeiro valor é maior
-O segundo valor é maior
-Não existe valor maior, os dois são iguais."""

from time import sleep
print('-=' * 17)
print('\033[1;33m   Comparando números inteiros\033[m')
print('-=' * 17)
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
print('\033[1;35mANALISANDO...\033[m')
sleep(2)
if num1 > num2:
    print('O primeiro número é maior!')
elif num2 > num1:
    print('O segundo número é maior!')
elif num1 == num2:
    print('Não existe número maior, os dois são iguais.')
