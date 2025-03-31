frase = 'Curso em Vídeo Python'
print(frase[::2])
#Colocando a string em maiúsculo e contando uma letra
print(frase.upper().count('O'))
#Quantos espaços possui a string?
print(len(frase))
#Substituindo uma palavra da string
print(frase.replace('Python','Android'))
#A substituição só será efetiva se a string receber o replace.
frase = frase.replace('Python', 'Android')
print(len(frase))
#Essa palavra está na frase?
print('Curso' in frase)
#Onde?
print(frase.find('Vídeo'))
#Cortando frases
print(frase.split())
#Utilizando a lista
dividido = frase.split()
print(dividido[0]) #Ao dividir, cada palavra vira um item na lista.
print(dividido[0][3]) #Mostrar no item 0, a 3ª letra
#Juntando novamente, diferente
print('*'.join(dividido))
print(dividido[1].islower())
