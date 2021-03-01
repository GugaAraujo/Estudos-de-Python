import random
from string import ascii_letters, digits, punctuation

qnt = int(input('\n\nSua senha precisa de quantos dígitos?\n---> :'))

possibilidades = ascii_letters + digits + punctuation
seg = random.SystemRandom()
senha = ''.join(seg.choice(possibilidades) for i in range (qnt))

print('\nFoi gerado sua senha forte de {} digitos.\n\nAnote: {}'.format(len(senha), senha))