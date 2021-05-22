print('''
CALCULADORA DE IMC E PESO IDEAL:
Baixo peso, muito grave = abaixo de 16.
Baixo peso, grave = entre 16 e 16,99.
Baixo peso = entre 17 e 18,49.
Peso normal = entre 18,50 e 24,99.
Sobrepeso = entre 25 e 29,99.
Obesidade grau I = entre 30 e 34,99.
Obesidade grau II = entre 35 e 39,99.
Obesidade grau III = maior que 40 (Obesidade mórbida).
''')

genero = input('Qual seu gênero? [F/M]: ').upper()
if genero != 'M' and genero != 'F':
    print('Você digitou um gênero inválido!\nPor padrão será selecinado o gênero masculino.')
    genero = 'M'

altura = input('\nQual a sua altura? ').replace(',', '.')
altura = float(altura)
peso = input('Qual o seu peso? ').replace(',', '.')
peso = float(peso)
"""
# Hamwi
# Homens: 48,1kg para cada 1,52m de estatura + 0,9kg para cada centímetro acima de 1,52m (±10%)
if genero == 'M':
    peso_base = 48.1
    altura_base = 152
    adicional = 0.9
    if altura * 100 <= altura_base:
        ideal = altura_base / peso_base * (altura * 100)
    else:
        ideal = ((altura * 100) - altura_base) * adicional + peso_base
    print(ideal)
# Mulheres: 45,5kg para cada 1,52m de estatura + 1,1kg para cada centímetro acima de 1,52m (±10%)
else:
    peso_base = 45
    altura_base = 152
    adicional = 1.1
    if altura * 100 <= altura_base:
        ideal = altura_base / peso_base * (altura * 100)
    else:
        ideal = ((altura * 100) - altura_base) * adicional + peso_base
    print(ideal)
# Devine
# 50 para cada 152 cm + 0,9 para cada cm adicional  # homem
if genero == 'M':
    peso_base = 50
    altura_base = 152
    adicional = 0.9
    if altura * 100 <= altura_base:
        ideal = altura_base / peso_base * (altura * 100)
    else:
        ideal = ((altura * 100) - altura_base) * adicional + peso_base
    print(ideal)

# 45,5 para cada 152 cm + 0,9 para cada cm adicional  # mulher
else:
    peso_base = 45.5
    altura_base = 152
    adicional = 0.9
    if altura * 100 <= altura_base:
        ideal = altura_base / peso_base * (altura * 100)
    else:
        ideal = ((altura * 100) - altura_base) * adicional + peso_base
    print(ideal)

# Robinson
# 52 para cada 152 cm + 0,74 para cada cm adicional  # homem
if genero == 'M':
    peso_base = 52
    altura_base = 152
    adicional = 0.74
    if altura * 100 <= altura_base:
        ideal = altura_base / peso_base * (altura * 100)
    else:
        ideal = ((altura * 100) - altura_base) * adicional + peso_base
    print(ideal)
# 49 para cada 152 cm + 0,67 para cada cm adicional  # mulher
else:
    peso_base = 49
    altura_base = 152
    adicional = 0.67
    if altura * 100 <= altura_base:
        ideal = altura_base / peso_base * (altura * 100)
    else:
        ideal = ((altura * 100) - altura_base) * adicional + peso_base
    print(ideal)"""

# Calculo do IMC
imc = peso / altura ** 2

print(f'\nSeu IMC é: {round(imc, 2)}.')

# Peso ideal - Fórmula usada:

if 18.5 <= imc < 25:
    print('PARABÉNS,', end=' ')

else:
    if genero == 'F':
        mulher = round((altura - 1) * 100 * 0.85, 2)
        menor = str(mulher - .5).replace('.', ',')
        maior = str(mulher + 4.5).replace('.', ',')
        print(f'Seu peso ideal está entre {menor} e {maior}.')
    else:
        homem = round((altura - 1) * 100 * 0.90, 2)
        menor = str(homem - .5).replace('.', ',')
        maior = str(homem + 4.5).replace('.', ',')
        print(f'Seu peso ideal está entre {menor} e {maior}.')

# Os resultados do IMC são interpretados da seguinte forma:
if imc < 16:
    print('Baixa de peso muito grave.')

elif imc < 17:
    print('Baixo peso grave.')

elif imc < 18.5:
    print('Baixo peso.')

elif imc < 25:
    print('Peso normal.')

elif imc < 30:
    print('Sobrepeso.')

elif imc < 35:
    print('Obesidade grau I')

elif imc < 40:
    print('Obesidade grau II')

else:
    print('Obesidade grau III (obesidade mórbida)')

# # Hammond
# if genero == 'M':  # 48 para cada 150 cm + 1,1 para cada cm adicional  # homem
#     peso_base = 48
#     altura_base = 150
#     menor = peso_base / altura_base * (altura * 100)
#
# else:  # 45 para cada 150 cm + 0,9 para cada cm adicional  # mulher
#     peso_base = 45
#     altura_base = 150
#     menor = peso_base / altura_base * (altura * 100)
# # Miller
# if genero == 'M':  # 55,7 para cada 152 cm + 0,5 para cada cm adicional  # homem
#     peso_base = 55.7
#     altura_base = 152
#     maior = peso_base / altura_base * (altura * 100)
#
# else:  # 53 para cada 152 cm + 0,5 para cada cm adicional  # mulher
#     peso_base = 53
#     altura_base = 152
#     maior = peso_base / altura_base * (altura * 100)
