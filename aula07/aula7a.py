#formatações = 20 quantidade de espaços
# ^ = centralizar
# > a direita
# < a esquerda
# simbolo antes do ^ preencherá o espaço "restante" com o simbolo#
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:20}!' .format(nome))
print('Prazer em te conhecer {:^20}!' .format(nome))
print('Prazer em te conhecer {:>20}!' .format(nome))
print('Prazer em te conhecer {:<20}!' .format(nome))
print('Prazer em te conhecer {:=^20}!' .format(nome))