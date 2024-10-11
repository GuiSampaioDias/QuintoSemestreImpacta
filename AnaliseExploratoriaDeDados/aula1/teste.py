import random
from collections import Counter
i = 0

lista = []
while i < 100000:
    dadoA = random.randint(1, 6)
    dadoB =random.randint(1, 6)
    somaDados = dadoA + dadoB
    lista.append(somaDados)
    i +=1
contagem = Counter(lista)

for item in sorted(contagem.keys()):
    resp = contagem[item] / 100000
    print(f'{item} = {resp:.4f}')

print(contagem)
