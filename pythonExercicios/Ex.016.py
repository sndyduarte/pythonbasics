from math import floor
num = float(input('\033[1;35mDigite um número qualquer: \033[m'))
i = floor(num)
#i = int(num)
print('\033[34mA porção inteira do número \033[1;35m{} \033[mé \033[32m{}\033[m.'.format(num, i))

from math import trunc
print('\033[33mA porção inteira do número digitado é \033[32m{}\033[m.'.format(trunc(num)))

