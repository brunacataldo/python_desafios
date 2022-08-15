def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'fizzbuzz, {n} é divisível por 3 e 5'
    if n % 3 == 0:
        return f'fizz, {n} é divisível por 3'
    if n % 5 == 0:
        return f'buzz, {n} é divisível por 5'
    return n

from random import randint

for i in range(100):
    aleatorio = randint(0,100)
    print(fb(aleatorio))
