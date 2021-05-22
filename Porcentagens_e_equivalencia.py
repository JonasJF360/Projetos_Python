#-*-coding:utf8;-*-
#qpy:console

# Define um estilo para o título.
def titulo(self):
    ln = '=' * 25
    print('\n%s\n# %s\n%s\n' % (ln,self,ln))

# Mosta a porcentagem entre dois valores.
def sb_porct(x, y):
    return (x / y) *100

# Calcula a porcentagem de um valor.
def vl_porct(x, y):
    return (x * y) / 100

# Mostra o valor inicial de um valor
# com base no resultado e a porcentagem.
def vl_inicial(x, y):
    return (x * 100) / y

# Mantem a equvalencia de dois valores
# ou medidas para mudança de escala.
def equiv(x, y, z):
    return (z * y) / x

titulo('Calcular porcentagem')
print('Escolha uma das opções\n%s' % ('-' * 25))
print('01 - Saber a porcentagem.')
print('02 - Valor da Porcentagem.')
print('03 - Saber o valor inicial\nreferente a porcentagem.')
print('04 - Manter a equivalência.')
tipo = int(input('%s\nOpcão: ' % ('-' * 25)))

if tipo == 1:
    vlx = float(input('\nValor menor: '))
    vly = float(input('Valor maior: '))
    result = str('A porcentagem é: %1.2f' % sb_porct(vlx, vly))
    
if tipo == 2:
    vlx = float(input('\nValor: '))
    vly = float(input('Porcentagem: '))
    result = str('O valor da porcentagem é: %1.2f' % vl_porct(vlx, vly))
    
if tipo == 3:
    vlx = float(input('\nValor: '))
    vly = float(input('Porcentagem: '))
    result = str('O valor inicial é: %1.2f' % vl_inicial(vlx, vly))
    
if tipo == 4:
    vlx = float(input('\nValor 01: '))
    vly = float(input('Valor 02: '))
    vlz = float(input('Novo Valor: '))
    result = str('A equivalencia é: %1.2f' % equiv(vlx, vly, vlz))
    
titulo('Resultado')
print(result)