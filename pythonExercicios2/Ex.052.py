"""Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

tot = 0
num = int(input('Digite um número inteiro: '))
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[1;33m', end = ' ')
        tot += 1
    else:
        print('\033[34m', end = ' ')
    print(i, end = ' ')
print('\n\033[mO número {} foi divisível por {} números.'.format(num, tot))
if tot == 2:
    print('Sendo assim, {} é um número PRIMO!'.format(num))
else:
    print('Sendo assim, {} NÃO é um número primo.'.format(num))
