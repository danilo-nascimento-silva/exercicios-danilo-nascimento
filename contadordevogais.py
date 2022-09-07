txt = input('Digite o texto: ')
a = 0
u = 0
o = 0
i = 0
e = 0

for y in txt.lower():
    if y == 'a': a+=1
    elif y == 'e': e+=1
    elif y == 'i': i+=1
    elif y == 'o': o+=1
    elif y == 'u': u+=1
    else: pass

print(f'A quantidade de vogal na frase foi de:\n'
      f'A = {a} \n'
      f'E = {e} \n'
      f'I = {i} \n'
      f'O = {o} \n'
      f'U = {u} ')