from random import randint

linha = '-' * 24
print (f'{linha}\n   APOSTAS ALEATORIAS\n{linha}')

while True:

    lista = []
    apostas = 6
    while apostas > 0:
    
        menor_numero = 1
        maior_numero = 60
        
        num_aleatorio = randint(menor_numero, maior_numero)
        
        if num_aleatorio in lista:
            continue
    
        else:
            lista += [num_aleatorio]
            apostas -= 1
    for n in lista:
        n = str(n)
        if len(n) == 1:
            n = '0' + n
        print(n, end='  ')
        
    print(f'\n{linha}')
    
    pergunta = input('Gerar outa aposta?\n(S)im (N)ão: ')
    pergunta = pergunta.upper()
        
    if pergunta == 'S':
        continue
            
    elif pergunta == 'N':
        print('\nOk, fim do programa.')
        break
            
    else:
        print('\nValor inválido!\nFim do programa.')
        break