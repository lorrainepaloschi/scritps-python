salario = float(input('Insira o seu salário: '))
if salario > 1250:
    salario_novo = salario + (salario * 0.10)

    print('O salario antigo era: {}R$, o salario com reajuste é de {}R$'.format(salario, salario_novo))
else:
    salario_novo = salario + (salario * 0.15)

    print('O salario antigo era: {}R$, o salario com reajuste é de {}R$'.format(salario, salario_novo))
