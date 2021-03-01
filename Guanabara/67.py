print('\n======= Tabuada 3.0 =======\n')

while True:
    n = int(input('Digite um número: '))
    if n < 0: break
    print('\n')
    for t in range(0, 11, 1):
        print(f'{n:^2} x {t:^2} = {n * t:^2}')
    print('\n')
print('\n\n~~~~~ F I M ~~~~~\n\n')
