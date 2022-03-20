# Calcular aumento de salário

a = float(input('Qual é o seu salário? '))

if a > 1250:
    novo_salario = 1250 + (1250 * 0.01)
    print('Seu novo salário é: {}'.format(novo_salario))
if a < 1250:
    novo_salario = 1250 + (1250 * 0.15)
    print('Seu novo salário é: {}'.format(novo_salario))

