"""
Faça um programa que pergunte o nome do produto, valor do produto e a quantidade de produtos e imprima o nome do produto e o valor a ser pago em python
"""
# Produtos em estoque e seu respectivos valores.
estoque = {'SAPATO':135.5, 'CHINELO':25.68,'SANDALIA': 176.20, 'TAMANCO': 88.30, 'TENIS': 212.15, 'BOTA': 86.82,
            'CAMISETA': 55.43, 'CUECA':9.98, 'CALSA JEANS': 113.97, 'JAQUETA': 215.15, 'VESTIDO':150.92, 'BLUSINHA': 43.22,
            'CALSINHA': 12.99, 'TOALHA': 22.00, 'CINTO MASCULINO': 45.93, 'CINTO FEMININO': 33.88}

print('-' * 30)

while True:
    ver_lista = input ('Digite [L] para ver a lista\nou [C] para ir as compras: ')
    ver_lista = ver_lista.upper()
    if ver_lista == 'L':
        print()
        for k, v in estoque.items():
            print(f'{k}: R${v}')
        break
    elif ver_lista == 'C':
        print('\nOk, boas compras!')
        break
    else:
        print ('Algo está errado!\n')
        True
  
print('-' * 30)
produto = ''
while True:
  produto = input('\nQual produto você deseja\ncomprar?: ')
  produto = produto.upper()

  if produto in estoque:
      print(f'{produto} custa R${estoque[produto]}')
      produto = produto
      break

  else:
    print('Valor não encontrado, verifique\na lista e digite novamente.')
    True

quantidade = 0
while True:
  try:
    quantidade = int(input('\nQual a quantidade desejada?: '))
    if quantidade < 1:
      print('Digite um valor maior que zero!')
      continue

    quantidade = quantidade
    break

  except ValueError:
    print('Digite apenas números inteiros!')
    True

print('\n' + '-' * 30)
preco = quantidade * estoque[produto]
print(f'Produto comprado: {produto}'
      f'\nQuandidade: {quantidade}'
      f'\nValor unitário: R${estoque[produto]}'
      f'\nTotal a pagar: R${round (preco, 2)}'
)
print('-' * 30)
