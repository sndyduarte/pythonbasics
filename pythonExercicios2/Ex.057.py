"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto."""

s = str(input('Digite o seu gênero [M/F/NB]: '))
if s != 'M' and s != 'F' and s != 'NB':
    s = ''
    while s != 'M' and s != 'F' and s != 'NB':
        s = str(input('Resposta inválida. Digite o seu gênero [M/F/NB]: ')).upper()
