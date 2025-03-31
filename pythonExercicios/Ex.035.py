"""Desenvolva um programa que leia o comprimento de três retas e
diga ao usuário se elas podem ou não formar um triângulo."""

print('Descubra abaixo se as medidas de três retas podem formar um triângulo!')
reta1 = float(input('Qual o comprimento da primeira reta? '))
reta2 = float(input('Qual o comprimento da segunda reta? '))
reta3 = float(input('Qual o comprimento da terceira reta? '))
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('Estas três retas podem formar um triângulo!')
else:
    print('Esta três retas não podem formar um triãngulo.')
