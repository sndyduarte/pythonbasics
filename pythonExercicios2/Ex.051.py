"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão."""

t = int(input('Digite o primeiro termo da P.A que você quer gerar: '))
r = int(input('Agora, digite a razão da P.A que você quer gerar: '))
print('Os primeiros 10 termos da P.A gerada são:')
print(t)
for i in range(1, 10):
    t += r
    print(t)
