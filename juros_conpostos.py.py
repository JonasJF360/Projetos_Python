print(f'\nCalcular juros compostos\nsobre um valor aplicado.\n')

c = float(input("Valor aplicado: ")) # Capital
i = float(input('Taxa de jutos: '))
m_d = input ('Taxa em [M]ese ou [A]no?: ')
m_d = m_d.upper()
if m_d == 'M':
    i = i / 100 / 12 # Taxa
elif m_d == 'A':
    i = i / 100
else:
    i = 0
t = float(input ('Período da aplicação: ')) # Tempo
m = c * (1 + i) ** t  # Montante

r = m - c # Rendimiento
print(f'\nRendimento bruto: {round(r, 2)}')

print ('\nDesconto de IR:')
print('1 para 0% # Sem desconto')
print('2 para 22,5% # Ate 180 dias')
print('3 para 20% # Ate 360 dias')
print('4 para 17,5% # Ate 720 dias')
print('5 para 15% # Acimas de 720 dias')
ir = int(input('Opção: '))
if ir == 2:
    desc = r * 0.225
    r -= desc

elif ir == 3:
    desc = r * 0.2
    r -= desc

elif ir == 4:
    desc = r * 0.175
    r -= desc

elif ir == 5:
    desc = r * 0.15
    r -= desc

else:
    r == r

print(f'\nRendimento: {round(r, 2)}\nTotal: {round(c + r, 2)}')
