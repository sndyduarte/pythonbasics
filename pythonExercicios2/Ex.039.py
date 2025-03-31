"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
-Se ele ainda vai se alistar ao serviço militar
-Se é a hora de se alistar
-Se já possou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

from datetime import date
nasc = int(input('Qual é o seu ano de nascimento? '))
ano = date.today().year
idade = ano - nasc
if idade == 18:
    print('Você deve se alistar ao serviço militar neste ano!')
elif idade == 17:
    print('Você deverá se alistar ao serviço militar em um ano.')
elif idade < 18:
    print('Você deverá se alistar ao serviço militar em {} anos.'.format(18 - idade))
    print('Seu alistamento será no ano de {}.'.format(ano + (18- idade)))
elif idade == 19:
    print('Seu momento de se alistar foi a um ano atrás, em {}.'.format(ano - 1))
elif idade > 18:
    print('Seu momento de se alistar foi a {} anos atrás, no ano de {}.'.format(idade - 18, ano - idade - 18))

