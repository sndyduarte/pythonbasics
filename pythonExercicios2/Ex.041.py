"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:
-Até 9 anos: MIRIM
-Até 14 anos: INFANTIL
-Até 19 anos: JUNIOR
-Até 20 anos: SENIOR
-Acima: MASTER"""

from datetime import date
nasc = int(input('Informe seu ano de nascimento: '))
ano = date.today().year
idade = ano - nasc
if idade <= 9:
    print('Sua categoria é MIRIM.')
elif 9 < idade <= 14:
    print('Sua categoria é INFANTIL.')
elif 14 < idade <= 19: #aqui pode colocar apenas o <= 19 pq já passou pelo primeiro "teste"
    print('Sua categoria é JUNIOR.')
elif idade == 20:
    print('Sua categoria é SENIOR.')
else:
    print('Sua categoria é MASTER.')
