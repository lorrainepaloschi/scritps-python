import math

cateto_oposto = float(input('Insira o cateto oposto: '))
cateto_adjacente = float(input('Insira o cateto adjacente: '))
soma_dos_quadrados_dos_catetos = math.pow(cateto_oposto, 2) + math.pow(cateto_adjacente, 2)
hipotenusa = math.sqrt(soma_dos_quadrados_dos_catetos)
print('A hipotenusa tem o valor de {}' .format(hipotenusa))