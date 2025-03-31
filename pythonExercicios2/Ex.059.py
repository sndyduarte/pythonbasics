"""Crie um programa que leia dois valores e mostre um menu na tela:
[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""

from time import sleep
r = 0
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
while r != 5:
    print('''O que você deseja fazer com estes números?
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    r = int(input('Digite sua resposta: '))
    if r == 1:
        print('{} + {} = {}.'.format(n1, n2, n1+n2))
    elif r == 2:
        print('{} x {} = {}.'.format(n1, n2, n1 * n2))
    elif r == 3:
        if n1 > n2:
            print('O número {} é maior que o número {}'.format(n1, n2))
        else:
            print('O número {} é maior que o número {}'.format(n2, n1))
    elif r == 4:
        print('=-' * 20)
        n1 = int(input('Digite um novo número: '))
        n2 = int(input('Digite outro número: '))
    elif r == 5:
        print('\033[033mFINALIZANDO...\033[m')
    else:
        print('Resposta inválida! Tente novamente.')
    print('=-' * 20)
    sleep(1)
print('===== FIM =====')
