import time, random

time.sleep(1)
print(
    '''
\033[33mPalíndromo, do grego palin (\033[mnovo\033[33m) e dromo (\033[mpercurso\033[33m), 
é toda palavra ou frase que pode ser lida de trás pra 
frente e que, independente da direção, mantém o seu sentido.\033[m''')
time.sleep(5)
print('''
Para analisar se uma frase é um palíndromo, digite 1.
Para ver exemplos de palíndromos, digite 2
''')
inicio = int(input('--->: '))

pal = ['A sacada da casa', 'Apos a sopa', 'A torre da derrota', 'Anotaram a data da maratona', 'Socorram-me subi no onibus em Marrocos']
if inicio == 2:
    print('\n\033[35m',random.choice(pal),'\033[m\n')
else:
    print('\n')
time.sleep(1)
entrada = str(input('Digite uma frase para analisarmos.\n--->: ')).strip().upper()
semhifen = entrada.replace('-', ' ')
palavras = semhifen.split()
junto = ''.join(palavras)

inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    resposta = 'Temos um \033[4;33mpalíndromo\033[m!'
else:
    resposta = 'A frase digitada \033[4;31mnão\033[m é um palíndromo.'

print('''
Ao ler normalmente: {}
lendo ao contrário: {}

{}
'''.format(junto, inverso, resposta))
