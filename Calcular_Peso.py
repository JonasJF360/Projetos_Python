""""
Este programa irá salvar e apresentar valores
para calcular a quantidade e o peso dos produtos
para calcular o valor final.
"""
#Módulos e verificadores.
import math
import re


def is_float(val):
    if isinstance(val, float):
        return True
    if not re.search(r'^-?[0-9]+\.[0-9]+$', val):
        return False
    return True


def is_int(val):
    if isinstance(val, int):
        return True
    if re.search(r'^-?[0-9]+$', val):
        return True
    return False


def is_number(val):
    return is_int(val) or is_float(val)


# Início do programa:
tc1 = '-' * 25
tc2 = '=' * 25
print(f'{tc2}\n{("CALCULAR PESO"):^25}\n{tc2}')
print(f'\nDIGITE "N" OU "0" PARA\nFINALIZAR.\n{tc1}')

# Loop infinito até que se pare com (0) ou (n) em "vlc".
incremento = 1
soma_pesos = 0
while True:
    if incremento < 10:
        quantia_produto = input(f'QUANTIDADE 0{incremento}: ')
    else:
        quantia_produto = input(f'QUANTIDADE {incremento}: ')
        
    if not is_number(quantia_produto): # Verifica se se o valor não é um número.
        quantia_produto = quantia_produto.upper()
        if quantia_produto != 'N':
            print(f'\nVALOR INVÁLIDO\nTENTE NOVAMENTE\n{tc2}')
            continue
        
        else:
            break

    else:
        quantia_produto = float(quantia_produto)
        if not quantia_produto: # Verifica se o valor digitado foi (0).
            break
        else:
            peso_produto = float(input('PESO UNITÁRIO: '))
            total_peso_produto = quantia_produto * peso_produto
            print(f'RESULTADO: {total_peso_produto:.2f}\n{tc1}')
            incremento += 1
            soma_pesos += total_peso_produto
            
# Calculo final.
valor_em_tonelada = soma_pesos / 1000
pagar_chapa = valor_em_tonelada * 18
print(f'\n{tc2}\nTOTAL: {valor_em_tonelada:.2f} TONELADA(S)')
print(f'TOTAL A PAGAR: {pagar_chapa:.2f}\n{tc1}')

# Divisão e verificação.
quantidade_chapas = input('QTD CHAPAS: ')
if not is_int(quantidade_chapas):
    print('VALOR PARA 01 CHAPA.')
    quantidade_chapas = int(1)
    
else:
    quantidade_chapas = int(quantidade_chapas)
    if quantidade_chapas == 0:
        print('VALOR PARA 01 CHAPA.')
        quantidade_chapas += 1
    
valor_pagar_chapas = math.ceil(pagar_chapa/quantidade_chapas)
print(f'VLR CADA: {valor_pagar_chapas:.2f}\n{tc2}')

fim = input('\nPRESSIONE "ENTER" \nPARA FINALIZAR.')
quit()

# Fim do programa.
