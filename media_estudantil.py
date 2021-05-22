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


# Início
print('-' * 30,'\nCALCULAR MÉDIA ESTUDANTIL','\n' + '-' * 30)
quant_alunos = input('Quantidade de alunos: ')
if not is_number(quant_alunos):
        print('Você digitou um valor inválido!')
        quant_alunos = 0
        quant_alunos = int(quant_alunos)
        
elif int(quant_alunos) < 1:
        print('Você digitou um valor inválido!')
        quant_alunos = 0
        quant_alunos = int(quant_alunos)
        
else:
    quant_alunos = int(quant_alunos) + 1
    print()
# Informaçôes de entrada
for i in range(1, quant_alunos):
    nome = 'nome' + str(i)
    vars()[nome] = input(f'Nome do aluno 0{i}: ').upper()

    erro = 'ok'
    for i in range(1, 5):
        nota = 'nota' + str(i)
        vars()[nota] = input(f'Informe a nota 0{i}: ').replace(',', '.')

        if not is_number(vars()[nota]):
            erro = 'erro'
            break
        
        else:
            vars()[nota] = float(vars()[nota])
            
        if (vars()[nota]) < 0:
            print('Valor substituído por "0"')
            vars()[nota] = 0
            
        if vars()[nota] > 10:
            print('Valor substituído por "10"')
            vars()[nota] = 10
    
    if erro == 'erro':
        print('\nVocê digitou um valor inválido!')
        quant_alunos = 0
        quant_alunos = int(quant_alunos)
        break
            
    media = 0
    for i in range(1, 5):
        nota = 'nota' + str(i)
        media += vars()[nota]

    media = media / 4
    if media < 4:
        situacao = 'REPROVADO'
    elif media < 6:
        situacao = ' de RECUPERAÇÃO'
    elif media < 9:
        situacao = 'APROVADO'
    else:
        situacao = 'APROVADAÇO'

    # Informações de saida.
    print('-' * 30)
    print(f'Aluno: {vars()[nome]}')
        
    for i in range(1, 5):
        nota = 'nota' + str(i)
        print(f'Nota 0{i}: {vars()[nota]}')

    print(f'Média: {media:.2f}')
    print(f'O aluno está {situacao}.')
    print('-' * 30)

fim = input('fim do programa!\n')
quit()
