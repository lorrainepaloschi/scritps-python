import random

aluno1 = input('Insira o nome do 1º aluno: ')
aluno2 = input('Insira o nome do 2º aluno: ')
aluno3 = input('Insira o nome do 3º aluno: ')
aluno4 = input('Insira o nome do 4º aluno: ')

list = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(list)
print('o nome sorteado foi: {}' .format(escolhido))

