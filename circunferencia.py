xc = float(input('Qual o valor de "x" da circunferencia? '))
yc = float(input('Qual o valor de "x" da circunferencia? '))
raio = float(input('Qual o valor do raio da circunferencia? '))

xp = float(input('Qual o valor de "x" do ponto? '))
yp = float(input('Qual o valor de "y" do ponto? '))

calculo = (xp - xc)**2 + (yp - yc)**2

if calculo == raio**2:
    print(f'{xp}, {yp} Pertence à circunferencia de centro ({xc}, {yc}) e raio {raio}')
else:
    print(f'{xp}, {yp} não pertence à circunferencia de centro ({xc}, {yc}) e raio {raio}')