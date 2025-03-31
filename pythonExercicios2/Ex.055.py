'''Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o mmaior e o menor pesos lidos.'''

maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input('Qual é o peso da {}ª pessoa? '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido é {}Kg, e o menor peso lido é {}Kg.'.format(maior, menor))
