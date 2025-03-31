"""Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80 km/h, motre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7.00 por cada km acima do limite."""

velocidade = int(input('Qual a velocidade do veículo em km/h? '))
if velocidade > 80:
    print('Você foi multado no valor de {}.'.format((velocidade - 80) * 7))
