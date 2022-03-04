import random
import time
print('Estou pensando em um número de 0 a 5... será que você consegue adivinhar?')
random = random.randint(0, 5)
print('PENSANDO..........')
time.sleep(3)
num = int(input('Insira um numero e vamos ver se você adivinhou o que o computador pensou: '))
if num == random:
    time.sleep(3)
    print('Parabéns! Você é um gênio!!')
else:
    time.sleep(3)
    print('Infelizmente não foi desta vez :(, eu pensei em {} '.format(random))