expr = input('Digite sua expressão aritimetica: ')
c1 = 0
c2 = 0

for x in expr:
    if x == '(': c1 += 1
    elif x == ')': c2 += 1
    else: pass

if c1 == c2: print(f'A expressão {expr} esta correta')
else: print(f'A expressão {expr} não esta correta')
