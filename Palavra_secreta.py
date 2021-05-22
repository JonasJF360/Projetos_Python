
from random import randint
## Lista de palávras a serem sorteadas.
lista = ['banana', 'floresta', 'jujuba','padaria', 'cerveja',
         'lampião', 'farinha', 'pimenta', 'batata', 'caveira',
         'juiz', 'cachorro', 'garo', 'periquito', 'janela',
         'caminhão', 'mosquito', 'legume', 'raiz', 'computador'
         'caloteiro','salafrario','abacaxi', 'sapato', 'sapo',
         'capacete', 'margarida', 'tijolo', 'tapioca', 'rolo',
         'geladeira', 'hospital', 'margarina', 'martelete', 'gema',
         'berinjela', 'tomate', 'navio', 'favela', 'calendario',
         'planilha', 'ervilha', 'onibus', 'carimbo', 'tela',
         'bandido', 'espirito', 'costela', 'barracão', 'remedio',
         'espirro', 'grilo', 'celular', 'lençol', 'parede']

while True:    
    fim = len(lista)  # Achar a contágem finál da lista.
    secreto = lista[randint(0, fim)]
    print(f'\nADIVINHE A PALAVRA SECRETA\nA PALAVRA TEM {len(secreto)} LETRAS.')
    print('"Você pode errar apenas 03 vezes".')
    secreto = secreto.upper()
    digitadas = []
    chances = 3
    
    while True:
        letra = input('\nDigite uma letra: ')
        letra = letra.upper()
    
        if len(letra) > 1:
            print('Ahhh, assim não vale! Digite apenas uma letra.\n')
            continue
    
        if not letra:
            print('Você não digitou nada\n')
            continue
    
        digitadas.append(letra)
        if letra in secreto:
            print(f'UHUUULLL, existe "{letra}" na palavra secreta.')
    
        else:
            print(f'AFFFzz, não existe "{letra}" na palavra secreta.')
            digitadas.pop()
    
        secreto_temporario = ''
        for letra_secreta in secreto:
            if letra_secreta in digitadas:
                secreto_temporario += letra_secreta
            else:
                secreto_temporario += '*'
    
        if secreto_temporario == secreto:
            print(f'\nQue legal, VOCÊ GANHOU!!! A palavra secreta era "{secreto_temporario.upper()}".')
            break

        if letra not in secreto:
            chances -= 1

        if chances != -1:
            print(f'A palavra está assim: [{secreto_temporario}]')

        if chances == 0:
            print('Você não pode mais errar!')

        if chances < 0:
            print('Infelizmente você perdeu!')
            print(f'A palavra secreta era {secreto}')
            break

        if chances > 0:
            print(f'Você pode errar só mais {chances} veze(s).')


    continuar = input('\nQuer jogar novamente? S/N: ')
    continuar = continuar.upper()
    if continuar == 'S':
        print('-' * 40)
        continue
        
    else:
        print('Ok entāo, finde jogo!')
        break
