a = int(input('Insira o primeiro numero: '))
b = int(input('Insira o segundo numero: '))
c = int(input('Insira o terceiro numero: '))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

menor = a
if b < a and b < c:
   menor = b
if c < a and c < b:
    menor = c

print('o maior numero é {}, e o menor numero é {}' .format(maior, menor))