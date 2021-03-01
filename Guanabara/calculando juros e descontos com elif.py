soma = 327
print('\n\nTotal a pagar: R${:.2f}.'.format(soma))

metodo = input('''
A vista (10% de desconto):         Digite 1 
Débito (3% de desconto):           Digite 2
Crédito (2% de juros acima de 4x): Digite 3

Informe o meio de pagamento: ''')

if metodo == '1':
    total = soma - (soma * 10 / 100)
    print(total)
elif metodo == '2':
    total = soma - (soma * 3 / 100)
    print(total)
elif metodo == '3':
    parcelas = input('''
Digite a quantidade de parcelas:

    1x      4x
    2x      5x
    3x      6x
    
:''')

    if parcelas <= '4':
        total = soma
        print(total)
    elif parcelas <='6':
        total = soma + (soma * 2 / 100)
        print(total)
    else: print('\nOpção inválida')


else: print('\nOpção não cadastrada')


print('\n\n')