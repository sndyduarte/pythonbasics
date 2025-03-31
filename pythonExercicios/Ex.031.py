"""Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0.50 por Km para viagens até 200Km e 0.45 para viagens mais longas."""

distância = float(input('Qual a distância da sua viagem em Km? '))
if distância <= 200 :
    print('O valor da passagem é R${}.'.format(distância * 0.50))
else:
    print('O valor da passagem é R${}.'.format(distância * 0.45))
 '''ou:
 preço = distância * 0.50 if distância <= 200 else distância * 0.45
 print('O preço da sua passagem será de R$(:.2f)'.format(preço))'''
