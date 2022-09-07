salario = float(input('Digite o salario atual: '))

if salario < 500.0: print(f'Seu salário de {salario} teve um reajuste de {(salario*15)/100} Totalizando {((salario*15)/100)+salario}')
if 500.0 < salario < 1000.0: print(f'Seu salário de {salario} teve um reajuste de {(salario*10)/100} Totalizando {((salario*10)/100)+salario}')
if salario > 1000.0: print(f'Seu salário de {salario} teve um reajuste de {(salario*5)/100} Totalizando {((salario*5)/100)+salario}')