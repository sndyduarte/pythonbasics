'''Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

from datetime import date
maior = 0
menor = 0
for i in range(1, 8):
    nasc = int(input('Qual o ano de nascimento da {}ª pessoa? '.format(i)))
    ano = date.today().year
    if ano - nasc >= 21:
        maior += 1
    else:
        menor += 1
print('Das pessoas informadas, {} atingiram a maioridade e {} ainda são menores de idade.'.format(maior, menor))
