real = float(input('Insira qual o valor em reais você possui na carteira. Use . para casas decimais: '))
#considerar o dolar a 3,27 (exercicio)
dolar = real / 3.27
print('{} é equivalente a {:.2f} de dólar' .format(real, dolar))