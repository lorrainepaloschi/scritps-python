dias = int(input('Informe a quantidade de dia(s) alugado(s): '))
km = float(input('Informe a quantidade de Km rodados: '))
valor_aluguel = (dias * 60) + (km * 0.15)

print('O valor total a ser pago em aluguel do carro é de R${}' .format(valor_aluguel))