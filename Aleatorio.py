"""
gerar numeros aleatórios da Mega Cena.
"""
from random import randint

repete = lambda x: x * 29
print(f'\n{repete("=")}')
print('NÚMEROS DA MEGA SENA.\n')
print(f'\n{repete("=")}')


while True:
    a = 1
    b = 60
    
    numero_1 = randint(a, b)  # 01
    
    numero_2 = numero_1  # 02
    while numero_2 == numero_1:
        aleatorio = randint(a, b)
        numero_2 = aleatorio
    
    numero_3 = numero_1  # 03
    while numero_3 == numero_1 or numero_3 == numero_2:
        aleatorio = randint(a, b)
        numero_3 = aleatorio
    
    numero_4 = numero_1  # 04
    while numero_4 == numero_1 or numero_4 == numero_2 or numero_4 == numero_3:
        aleatorio = randint(a, b)
        numero_4 = aleatorio
    
    numero_5 = numero_1  # 05
    while numero_5 == numero_1 or numero_5 == numero_2 or numero_5 == numero_3 or numero_5 == numero_4:
        aleatorio = randint(a, b)
        numero_5 = aleatorio
    
    numero_6 = numero_1  # 06
    while numero_6 == numero_1 or numero_6 == numero_2 or numero_6 == numero_3 or numero_6 == numero_4 or numero_6 == numero_5:
        aleatorio = randint(a, b)
        numero_6 = aleatorio
    
    # Display
    print('(' + str(numero_1), numero_2, numero_3, numero_4, numero_5, str(numero_6) + ')', sep=') (')
    print(repete('='))
    
    pergunta = input('Gerar outa aposta\n(S)im (N)ão: ')
    
    if not pergunta.isnumeric():
        pergunta = pergunta.upper()
        
        if pergunta == 'S':
            print(repete('='))
            continue
            
        elif pergunta == 'N':
            print('Ok, fim do programa.')
            print(repete('='))
            break
            
        else:
            print('Valor inválido!\nFim do programa.')
        print(repete('='))
        break
        
    else:
        print('Valor inválido!\nFim do programa.')
        print(repete('='))
        break
