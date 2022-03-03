nome = input('Insira seu nome completo: ').strip()
split = nome.split()
lenght = int(len(split))
print('Seu nome completo é: {}\nPrimeiro nome: {}\nUltimo nome: {}' .format(nome, split[0], split[lenght-1]))