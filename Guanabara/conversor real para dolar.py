print('\n#### Conversor de Real para Dólar e Euro ####\n')
real = float(input('Quantos reais deseja converter? '))

dolar = real * 5.46
euro = real * 6.63

print('\nR${:.2f} é equivalente a U${:.2f} ou {:.2f}€.'.format(real, dolar, euro))


