from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('~~' * 12)
print('Vamos jogar JOKENPO????')
print('~~' * 12)
print('''Selecione uma opção:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua joggada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
if computador == 0:
      if jogador == 0:
            print('EMPATE!!')
      elif jogador == 1:
            print('PARABÉNS! VOCÊ ME VENCEU!')
      elif jogador == 2:
            print('AHÁÁÁÁÁ´!! EU VENCII!!!!')
      else:
            print('JOGADA INVÁLIDA. Tente novamente.')
elif computador == 1:
      if jogador == 0:
            print('AHÁÁÁÁÁ´!! EU VENCII!!!!')
      elif jogador == 1:
            print('EMPATE!!')
      elif jogador == 2:
            print('PARABÉNS! VOCÊ ME VENCEU!')
      else:
            print('JOGADA INVÁLIDA. Tente novamente.')
elif computador == 2:
      if jogador == 0:
            print('PARABÉNS! VOCÊ ME VENCEU!')
      elif jogador == 1:
            print('AHÁÁÁÁÁ´!! EU VENCII!!!!')
      elif jogador == 2:
            print('EMPATE!!')
      else:
            print('JOGADA INVÁLIDA. Tente novamente.')
print('=' * 24)
print('''Jogador escolheu {} \nComputador escolheu {}'''.format(itens[jogador], itens[computador]))
print('=' * 24)