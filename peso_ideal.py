print('\nCALCULAR PESO IDEAL\n')
sexo = input('Qual o seu gênero? (M / F): ').upper()
altura = input('Qual a sua altura: ').replace(',', '.')
peso_ideal, altura = '', float(altura)

# Para homem = (72.7 * altura) - 58
if sexo == 'M':
    peso_ideal = str(round(72.7 * altura - 58, 2)).replace('.', ',')
    print(f'Como você é um homem seu peso peso_ideal é: {peso_ideal}\n')
    
# Para mulher = (62.1 * altura) - 44.7
elif sexo == 'F':
    peso_ideal = str(round(62.1 * altura - 44.7, 2)).replace('.', ',')
    print(f'Como você é uma mulher seu peso peso_ideal é: {peso_ideal}\n')

# Para o cado do usuário digirar um genero inválido
else:
    homem = 72.7 * altura - 58
    mulher = 62.1 * altura - 44.7
    peso_ideal = str(round((homem + mulher) / 2, 2)).replace('.', ',')
    print(f'Você mede {str(altura).replace(".", ",")}',
          f'\nPorém digitou um gênero inválido',
          f'\nSendo assim sua média de peso é: {peso_ideal}\n')