import re
import random


def is_float(val):  # Verifica se o número é de ponto flutuante
    if isinstance(val, float):
        return True
    if not re.search(r'^-?[0-9]+\.[0-9]+$', val):
        return False
    return True


def is_int(val):  # Verifica se é um número inteiro
    if isinstance(val, int):
        return True
    if re.search(r'^-?[0-9]+$', val):
        return True
    return False


def is_number(val):  # Verifiva se é de fato um número
    return is_int(val) or is_float(val)


"""
Esse programa irá apresentar a tabuada do 1 ao 10 se você 
digitar a letra 'T' ou a tabuada de algum número que for
digitado ao invés de 'T'.
Caso o valor digitado não seja nem um número e nem a letra
'T' será apresentada uma menságem de erro e uma tabuada
gerada aleatóriamente entre 1 e 10.
"""
def tabuada(x):
    print('-' * 12)
    for y in range(1, 11):
        z = x * y
        print(f'{x} x {y} = {z}')
        if y == 10:
                print('-' * 12)


print('Digite [t] para ver a tabuada do 1 ao 10',
      '\nou digite um número qualquer para ver a')
i = input('tabuada desse número: ')
i = i.upper()
if not is_number(i):
    while True:
        if i != 'T':
            w = random.randint(1,10)
            print('\nVocê diditou um valor inválido!',
                  f'\nMas veja a tabuada do "{w}" para',
                  '\nnão sair daqui sem nada.')
            tabuada(w)
            break

        else:
            print('-' * 12)
            for x in range(1, 11):
                for y in range(1, 11):
                    z = x * y
                    print(f'{x} x {y} = {z}')
                    if y == 10:
                        print('-' * 12)
            break
    
else:
    if is_int(i):
        i = int(i)
        tabuada(i)

    else:
        i = float(i)
        tabuada(round(i, 2))
