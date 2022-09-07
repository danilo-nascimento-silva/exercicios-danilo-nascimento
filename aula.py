n = int(input('Digite o numero: '))

if 0<=n<=25:
    intervalo = [0,25]
elif 26<=n<=50:
    intervalo = [25,50]
elif 51<=n<=75:
    intervalo = [50,75]
elif 76<=n<=100:
    intervalo = [75,100]
else:
    intervalo = [0, 100]

if 0<=n<=100:
    mensagem = print(f"{n} Pertence ao intervalo {intervalo}")
else:
    mensagem = print(f"Valor invalido, {n} não pertence ao intervalo {intervalo}")