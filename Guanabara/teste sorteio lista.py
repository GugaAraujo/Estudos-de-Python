import random , time

a1 = ('Zeca Urubu')
a2 = ('Zeca Camargo')
a3 = ('Zeca Baleiro')
a4 = ('Zé Carioca')

#Refiz com metodo choise
zeca = [a1, a2, a3, a4]
choise = random.choice(zeca)
print('O Zeca escolhido é : {}'.format(choise))

random.shuffle(zeca)
print(zeca)