n = int(input('Digite o primeiro termo da sua P.A: '))
r = int(input('Digite a razão da sua P.A: '))
c = 0
print(n)
total = 0
resp = 10
while resp != 0:
    total = total + resp
    while c < total - 1:
        n = n + r
        print(n)
        c +=1
    resp = int(input('Quantos termos a mais você deseja ver? '))
