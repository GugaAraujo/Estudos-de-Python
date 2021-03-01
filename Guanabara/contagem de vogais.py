texto = input('Cole o texto --->')


a = texto.count('a')
e = texto.count('e')
i = texto.count('i')
o = texto.count('o')
u = texto.count('u')

vogais = a + e + i + o + u



print('\n\nLetras A: {}; \nLetras E: {}; \nLetras I: {}; \nLetras O: {}; \nLetras U: {}; \nVogais: {}'.format(a, e, i, o ,u, vogais))

print('adelio' in texto)

print(texto.replace('novembro', 'agosto'))

print(texto.split())

listas = texto.split()
import random
random.shuffle(listas)
print(listas)


#trocadata = texto.replace('7','14')
#trocames = trocadata.replace('novembro','agosto')

#print(trocames)