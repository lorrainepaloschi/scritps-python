comprimento = float(input('Insira o comprimento de sua parede: '))
altura = float(input('Insira a altura de sua parede: '))
area = comprimento * altura
tinta = area / 2
print('Para pintar esta parede será necessário {} litros de tinta' .format(tinta))
