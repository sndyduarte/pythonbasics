"""Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles."""

from time import sleep
import emoji
for i in range(10, -1, -1):
    print(i)
    sleep(1)
print(emoji.emojize(':fireworks:\033[1;34m FELIZ ANO NOVO!!!!!!\033[m :fireworks:', language = 'alias'))
