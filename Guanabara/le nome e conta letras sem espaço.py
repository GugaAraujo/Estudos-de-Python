nome = input('Digite o nome:')
print(nome.upper())
print(nome.lower())
print(len(nome))
print('numero de espaços: {}'.format(nome.count(" ")))

print((len(nome) - (nome.count(' '))))
nomesemespaco = nome.replace(" ","")
print('nome sem espaços tem {} caracteres. Se liga ----> {}'.format(len(nomesemespaco) , nomesemespaco))