"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
-Abaixo de 18.5: Abaixo do Peso
-Entre 18.5 e 25: Peso ideal
-25 até 30: Sobrepeso
-30 até 40: Obesidade
-Acima de 40: Obesidade mórbida"""

print('~*~ Vamos calcular seu IMC? ~*~')
altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso em Kg: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC é {:.2f}. Você está abaixo do peso.'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é {:.2f}. Você está com o peso ideal'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é {:.2f}. Você está com Sobrepeso.'.format(imc))
elif 30 <= imc <= 40:
    print('Seu IMC é {:.2f}. Você está com Obesidade.'.format(imc))
else:
    print('Seu IMC é {:.2f}. Você apresenta um caso de Obesidade mórbida.'.format(imc))
