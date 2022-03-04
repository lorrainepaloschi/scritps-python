'''nome = str(input('Qual é o seu nome? '))
if nome == 'Lorraine':
    print('Que lindo nome você tem!')
else:
    print('seu nome é tão normal...')
print('Bom dia, {}!' .format(nome))'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A média foi: {:.1f}' .format(m))
if m >= 6:
    print('Parabéns!')
else:
    print('Precisa estudar mais...')