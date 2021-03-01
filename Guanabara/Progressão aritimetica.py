print('''
##### Progressão Aritmética ####

''')

pt = int(input('Defina o Primeiro Termo: '))
rz = int(input('Defina a Razão: '))


for c in range(pt,int(10 * pt / rz), rz):
        print(c)