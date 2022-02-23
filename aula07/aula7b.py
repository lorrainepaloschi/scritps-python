n1 = int(input('Insira um numero: '))
n2 = int(input('Insira outro numero: '))

s = n1 + n2 #soma
m = n1 * n2 #multiplicação
d = n1 / n2 #divisao
di = n1 // n2 #divisao inteira
e = n1 ** n2 #potencia
print(' A soma é {}\n o produto é {}\n e a divisão é {:.3f}' .format(s, m, d), end=' ') #end é oq acontece ao acabar a linha, nesse caso, será inserido espaço
print(' Divisão inteira {} e potencia {}' .format(di, e))