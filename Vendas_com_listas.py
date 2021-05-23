import os

lista = []
a = 1
while a <= 2:
    temporario = []
    colaborador = input(f'\nNome do colaborador(a) {a}: ')
    temporario.append(colaborador.upper())
    salario = input('Salário do fixo colaborador: ').replace(',', '.')
    print()

    total_vendas = 0
    for i in range(1, 5):
        vendas = input(f'Total de vendas da semana 0{i}: ').replace(',', '.')
        total_vendas += float(vendas)

    temporario.append(round(total_vendas, 2))
    comissao = total_vendas * 0.1
    salario_total = float(salario) + comissao
    temporario.append(round(salario_total, 2))

    lista.append(temporario)
    a += 1

os.system('clear') or None
print(f'\n{"=" * 30}\nTecnos LTDA - Resumo do mes\n{"=" * 30}')
no_mes = 0
for c, t, s in lista:
    print(f'Nome do colaborador(a) : {c}',
          f'\nTotal de vendas: R$ {t}',
          f'\nSalário do mês: R$ {s}\n')
    no_mes += t
        
print(f'Faturamento total da loja:\nR$ {no_mes:.2f}\n{"=" * 30}')
