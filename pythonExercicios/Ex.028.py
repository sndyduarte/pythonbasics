"""Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
O programa deverá escrever na tela se o usuário venceu ou perdeu."""

from random import randint
from time import sleep #improve
pc = randint(0, 5)
print('~*~' * 20)
print('Adivinhe qual valor inteiro entre 0 e 5 eu estou pensando... ')
print('~*~' * 20)
num = int(input('Em qual número eu pensei??? '))
print('PROCESSANDO...')
sleep(3)
if num == pc:
    print('Você acertou!! Eu pensei no número {}!'.format(pc))
else:
    print('Você errou! Eu pensei no número {}.'.format(pc))
