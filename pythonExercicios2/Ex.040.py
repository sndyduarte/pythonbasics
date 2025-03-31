"""Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
-Média abaixo de 5.0: REPROVADO
-Média entre 5.0 e 6.9: RECUPERAÇÃO
-Média 7.0 ou superior: APROVADO"""

print('-=-' * 20)
print('Calcule a sua média e saiba sua situação de aprovação:')
print('-=-' * 20)
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('REPROVADO. \nO resultado da sua média foi {}. Estude mais!'.format(media))
elif 5.0 <= media < 7.0:
    print('RECUPERAÇÃO. \nO resultado da sua média foi {}. Estude mais!.'.format(media))
else:
    print('APROVADO! \nO resultado da sua média foi {}! PARABÉNS!!!'.format(media))
