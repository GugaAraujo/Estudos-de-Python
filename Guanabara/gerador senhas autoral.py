import random
from string import digits, ascii_letters, punctuation, ascii_lowercase, ascii_uppercase

combo = digits + ascii_letters + punctuation

c1 = random.choice(combo)
c2 = random.choice(combo)
c3 = random.choice(combo)
c4 = random.choice(combo)
c5 = random.choice(ascii_lowercase)
c6 = random.choice(ascii_lowercase)
c7 = random.choice(ascii_uppercase)
c8 = random.choice(ascii_uppercase)
c9 = random.choice(digits)
c10 = random.choice(digits)
c11 = random.choice(punctuation)
c12 = random.choice(punctuation)

senha = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12]
senhas = ''.join(senha)

print('\n\nGerada sua senha forte com {} dígitos. Anote: {}\n\n'.format(len(senhas), senhas))