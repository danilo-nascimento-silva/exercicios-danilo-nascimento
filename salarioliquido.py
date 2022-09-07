salariobruto = float(input('Informe o seu salario bruto: '))

if salariobruto<=1903.98:
    imposto = 0
elif 1903.98 < salariobruto < 2826.65:
    imposto = ((salariobruto*7.5)/100)
elif 2826.65 < salariobruto < 3751.05:
    imposto = (salariobruto*15)/100
elif 3751.05 < salariobruto < 4664.68:
    imposto = (salariobruto*22.5)/100
elif 4664.68 < salariobruto:
    imposto = (salariobruto*27.5)/100

print(f'Salario Liquido é {salariobruto - imposto}')