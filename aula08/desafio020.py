import random
'''alunos = input("informe os alunos separados por virgula: ")
alunos_list = alunos.split(",")
random.shuffle(alunos_list)
print('A ordem de apresentação é {}'.format(alunos_list))'''

aluno1 = input('Insira o nome do 1º aluno: ')
aluno2 = input('Insira o nome do 2º aluno: ')
aluno3 = input('Insira o nome do 3º aluno: ')
aluno4 = input('Insira o nome do 4º aluno: ')

list  = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(list)
print('A ordem de apresentação será: ')
print(list)