frase = 'Curso em Vídeo Python'

print(frase[3:13]) #exibe de tal a tal casa
print(frase[:15]) #exibe da casa 0 até o ultimo valor
print(frase[:15:2])  #exibe da casa 0 até o ultimo valor pulando de 2 em 2
print(frase[::2]) #exibe todos os caracteres pulando de 2 em 2
print(frase.count('o')) #diferencia-se maiusculas de minusculas
print(len(frase)) #len-length (tamanho)
print(frase.replace('Python', 'Android')) #substitui (mas não salva, p/ salvar -> frase = frase.replace('Python', 'Android')
print(frase.find('Vídeo')) #mostra qual a posição do caracter, diferencia-se maius de minusc. se não encontrar a resposta será -1
print(frase.split())

# """ texto longo """ fará com que as quebras de linhas originais sejam respeitadas
print("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley
of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap
into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus
PageMaker including versions of Lorem Ipsum.""")
