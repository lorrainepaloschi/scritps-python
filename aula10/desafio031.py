distancia = int(input('Insira a distancia da viagem em KM: '))
if distancia <= 200:
    valor_passagem = distancia * 0.50
else: valor_passagem = distancia * 0.45

print('O valor da passagem é de: {}R$' .format(valor_passagem))