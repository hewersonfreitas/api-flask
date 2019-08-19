try:
    qty = int(input('Quantidade total de testes? '))
except ValueError:
    print('Seu valor não é númerico, por favor digite o número corretamente!')
result = []

for idx, value in enumerate(qty):
    word = input('Digite a palavra desejada: ')
    if(len(word) < 9 or len(word) > 1000):
        print("""A palavra deve conter entre 9 a 1000 caracteres
              , você digitou uma palavra com {0} caracteres""".format(len(word)))
    print(idx)
