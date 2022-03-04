velocidade = float(input('Insira a velocidade atual: '))
if velocidade > 80:
    print('Opa, você está acima da velocidade!')
    multa = (velocidade - 80) * 7
    print('Você foi multado em {:.2f}R$, pois passou {}km/h acima da velocidade permitida' .format(multa, (velocidade - 80)))
print('Tenha um bom dia, dirija com segurança!')