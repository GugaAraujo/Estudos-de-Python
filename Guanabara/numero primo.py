x = int(input('\nInsira um número para sabermos se é um número primo: '))
print('\n')
div = 0
for contagem in range (1, x + 1):
    if x % contagem == 0:
        print('\033[30m{}'.format(contagem), end=' ')
        div += 1
    else:
        print('\033[32m{}'.format(contagem), end=' ')

print('\n\033[m')
print('O número {} é divisível por {} números. Por este motivo, o número {} '.format(x, div, x), end='')
if div == 2:
    print('é um número primo.')
else:
    print('não é um número primo.')