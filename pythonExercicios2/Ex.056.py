'''Desenvolva um programa que leia o nome, idade e o sexo de 4 pessoas. No final do programa, mostre:
A média de idade do grupo.
Qual é o nome do homem mais velho.
Quantas mulheres tem menos de 20 anos.'''

idade = []
somaidade = 0
homem = 0
mulher = 0
for p in range(1, 5):
    n = str(input('Nome: ')).strip()
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).upper()
    idade += [i]
    somaidade += i
    if s == 'M':
        if p == 1:
            homem = i
        else:
            if i > homem:
                homem = i
                nomeh = n
    else:
        if s == 'F':
            if i < 20:
                mulher += 1
print('O homem mais velho se chama {} e tem {} anos.'.format(nomeh, homem))
print('Dentre as mulheres, {} possuem menos de 20 anos.'.format(mulher))
media = somaidade/4
print('A média entre as idades dos participantes é {}'.format(media))
