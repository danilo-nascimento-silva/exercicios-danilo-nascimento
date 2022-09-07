palavra = input('Escreva sua palavra: ')
inverso = palavra[::-1]
if palavra.lower() == inverso.lower():
    print(f'{palavra} é um Palíndromo')
else:
    print(f'{palavra} não é um Palíndromo')