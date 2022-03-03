import math

angulo = int(input('Insira um ângulo: '))
ang = math.radians(angulo)
cos = math.cos(ang)
sen = math.sin(ang)
tang = math.tan(ang)

print('Ângulo = {}\nCosseno = {}\nSeno = {}\nTangente = {}' .format(angulo, cos, sen, tang))