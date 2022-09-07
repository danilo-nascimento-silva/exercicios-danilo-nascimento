list = [1, 2, 2, 1, 3, 3, 4, 5, 1, 3, 2]
valores_sr = []

for x in list:
    if x in valores_sr:
        continue
    else:
        valores_sr.append(x)
print(valores_sr)