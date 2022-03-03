import math
#from math import sqrt (importar somente a função de raiz quadrada)
#from math import sqrt, floor (raiz quadrada e arredondamento para cima)
num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print('A raiz de {} é igual a {:.2f}' . format(num, raiz))