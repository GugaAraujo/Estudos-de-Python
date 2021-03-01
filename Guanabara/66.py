quan = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    quan += 1
    soma += n
print(f'\nForam informados {quan} números.\n'
      f'A soma de todos eles é {soma}\n')