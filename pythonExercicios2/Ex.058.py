"""Melhore o jogo do DESAFIO 28 onde o computador vai "pensar em um número de 0 a 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários."""

from random import randint
print('=-' * 5,'\033[1;33mVou pensar num número de 0 a 10, tente adivinhar!\033[m','=-' * 5)
pc = randint(0, 10)
jogador = int(input('Qual é o seu palpite? '))
if jogador == pc:
    print('\033[1;35mPARABÉNS, VOCÊ ACERTOU! E de primeira!')
else:
    jogador = 0
    cont = 1
    while jogador != pc:
        jogador = int(input('Errou! Tente novamente: '))
        cont += 1
    print('\033[1;35mPARABÉNS! VOCÊ ACERTOU! Mas foram necessárias {} tentativas.'.format(cont))
