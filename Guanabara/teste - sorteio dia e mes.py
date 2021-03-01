dia = input('diga os dias')
mes = input('diga os meses')

dividedia = dia.split()
dividemes = mes.split()

import random


print(random.choice(dividedia), 'da', random.choice(dividemes))
print(''.join(mes))


