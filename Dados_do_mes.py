"""
Este programa calcua os ganhos e os
gartos do mês e dá um resumo do que
resta ou falta de dinheiro no orçamento.
"""
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


def mudar_str(valor):
    valor = str(round(valor, 2))
    return valor.replace('.', ',')


# Início do programa:
tc1, tc2 = '-' * 25, '=' * 25
print(f'{tc2}\n{"GANHOS MENSÁL" :^25}\n{tc2}')

# Informações de ganho.
salario = (input('SALÁRIO: ')).replace(',', '.')
custos = (input('AJUDA DE CUSTOS: ')).replace(',', '.')
horas_extra = (input('HORAS EXTRAS: ')).replace(',', '.')
outos_ganhos = (input('OUTROS: ')).replace(',', '.')
soma_sch = float(salario) + float(custos) + float(horas_extra)

# Loop de pergunta sobre I.N.S.S
total_ganho = 0
while True:
    pergunta = input(f'{tc1}\nIRÁ DESCONTAR O I.N.S.S?\nS/N: ')
    if is_number(pergunta):
        print('\nOPÇÃO INVÁLIDA,\nRESPONDA "S" PARA SIM\nOU "N" PARA NÃO.')
        continue

    else:
        pergunta = pergunta.upper()

        # Verificar se a resposta foi sim 'S'.
        if pergunta == 'S':
            inss = soma_sch * 8 / 100
            total_ganho = soma_sch + float(outos_ganhos) - inss
            print(f'{tc1}\nTOTAL GANHO: {mudar_str(total_ganho + inss)}\nI.N.S.S: -{mudar_str(inss)}')
            break

        # Verificar se a resposta foi diferente de não 'N'.
        elif pergunta != 'N':
            print('\nOPÇÃO INVÁLIDA,\nRESPONDA "S" PARA SIM\nOU "N" PARA NÃO.')
            continue

        # Se a resposta foi 'n'(Não), executará o código abaixo.
        else:
            total_ganho = soma_sch + float(outos_ganhos)
            print(f'{tc1}\nTOTAL GANHO: {mudar_str(total_ganho)}\n')
            break

# Referente aos gastos do mês.
print(f'{tc2}\n{"GASTOS MENSÁL" :^25}\n{tc2}')
gastos = ['SEGURO', 'COMPRAS', 'ENERGIA', 'ÁGUA', 'INTERNET',
          'PLANO VIVO', 'TRANSPORTE', 'FACULDADE', 'ADRIELE', 'RAÇÃO', 'OUTRAS']

# Circulo para os gastos do mês.
giro = 0
indice_gastos = 0
soma_gastos = 0
while giro < len(gastos):
    soma_dos_gastos = (input(f'{gastos[indice_gastos]}: ')).replace(',', '.')
    soma_gastos += float(soma_dos_gastos)
    indice_gastos += 1
    giro += 1

# CARTÃO DE CRÉDITO:
# Este código irá salver e apresentar valors
# para calcular o gasto do cartão de crédito.
print(f'{tc2}\n{"GASTOS COM CARTÃO" :^25}\n{tc2}',
      f'\nDIGITE "0" PARA PARAR\n{tc1}')
# Circulo que vai ate 10 ou até que se dige 'ZERO' (0).
conta = 1
soma_cartao = 0
while True:
    valor_conta = input(f'VALOR 0{conta}: ').replace(',', '.')
    if not is_number(valor_conta):
        print('VOCÊ DIGITOU UM VALOR\nINVÁLIDO.')
        continue
    else:
        valor_conta = float(valor_conta)
        if valor_conta == 0:
            break

        else:
            while True:
                parcela = input('QTD PARCELAS: ')
                if is_int(parcela):
                    parcela = int(parcela)
                    pagar = valor_conta / parcela
                    print(f'A pagar: {mudar_str(pagar)}\n{tc1}')
                    soma_cartao += pagar
                    conta += 1
                    break
                else:
                    print('VOCÊ DIGITOU UM VALOR\nINVÁLIDO.')
                    continue

# Calcular valor a pagar
print(f'{tc1}\nTOTAL A PAGAR: {mudar_str(soma_cartao)}')

soma_tudo = soma_gastos + soma_cartao
# RESUMO DOS GANHOS VS GASTOS.
print(f'{tc2}\nGANHO LIVRE: {mudar_str(total_ganho)}\nTOTAL GASTO: {mudar_str(soma_tudo)}',
      f'\n{tc1}\nDISPONÍVEL: {mudar_str(total_ganho - soma_tudo)}\n{tc2}')
