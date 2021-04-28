import random, time
sorteio = []
while len(sorteio) != 6:
    aleatorio = random.randint(1, 60)
    while aleatorio not in sorteio:
        sorteio.append(aleatorio)
ordemCrescente = str(sorted(sorteio)).replace(', ',' - ')

print('''
--- \033[33mSua sorte de hoje é:\033[m ---''')
time.sleep(1)
print('''
=============================
\033[33m{}\033[m
=============================


-------- \033[33mBoa sorte!!\033[m --------
'''.format(ordemCrescente))


