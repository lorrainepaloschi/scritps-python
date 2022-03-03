num = int(input('Insira um valor entre 0 e 9999: '))
n = str(num)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('unidade: {}\ndezena: {}\ncentena: {}\nmilhar: {}'.format(u, d, c, m))
