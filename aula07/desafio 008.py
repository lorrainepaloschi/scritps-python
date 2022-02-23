medida = float(input('Insira a medida em metros: '))
if(medida == 1):
    print('{} metro é igual a {} centimetros ou {} milimetros' .format(medida, (medida*100), (medida*1000)))
else:
    print('{} metros é igual a {} centimetros ou {} milimetros' .format(medida, (medida*100), (medida*1000)))