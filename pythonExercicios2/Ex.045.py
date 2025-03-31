"""Crie um programa que faça o computador jogar Jokenpô com você."""

print('~' * 25)
print('\033[1;35m  Vamos jogar Jokenpô?\033[m')
print('~' * 25)
from random import choice
lista = 'pedra', 'papel', 'tesoura'
pc = choice(lista)
usuario = str(input('\033[33mEscolha uma opção entre pedra, papel e tesoura: ')).strip()
usuario = usuario.lower()
if usuario == pc:
    print('\033[034mHAHA! Empatamos! Eu também escolhi {}. Tente novamente!'.format(pc))
elif usuario == 'pedra' and pc == 'papel' or usuario == 'papel' and pc == 'tesoura' or usuario == 'tesoura' and pc == 'pedra':
    print('\033[034mHÁÁÁÁ!! Ganhei de você! Eu escolhi {}!'.format(pc))
else:
    print('\033[1;35mVocê ganhou!!! Eu escolhi {}. PARABÉNS.'.format(pc))
