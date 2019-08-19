import sys
from decimal import Decimal

time = round(Decimal(1/100), 2)
words = []
results = []

try:
    repeats = int(input('Quantidade total de testes? '))
except ValueError:
    print('Seu valor não é númerico, por favor digite o número corretamente!')


for idx in range(0, repeats):
    word = input('Digite a palavra desejada: ')
    if(len(word) < 9 or len(word) > 1000):
        print("""A palavra deve conter entre 9 a 1000 caracteres
              , você digitou uma palavra com {0} caracteres""".format(len(word)))
        sys.exit(1)

    words.insert(idx, word)
    results.insert(idx, str(len(word)*time))

## Resultado
print(dict(zip(words,results)))
