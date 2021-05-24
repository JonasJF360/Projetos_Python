import random

"""
Esse prograna pega uma frase qualquer e substituir cada letra
alearóriamente por um novo caractere(letra, número ou simbolo)
da lista 'novas_letras' em seus indices correspondenter.
Isso irá ocorrer de letra por letra, que contida a mesma na
variável 'letras'.
o sínolo 'æ' seŕa colocado nos caracteres incompatíveis.

Futuramente pretendo criar algo para "desencriprar" essa minha
"criptografia" gerada a partir de frases.
"""

letras = "abcdefghijklmnopqrstuvwxyzáàâãéêíìóõôúç "

novas_letras = [
    ['ł', '?', '§', '.', '[', 'ä', 'ẗ', '”', '¿', 'n', '*'],  # 0 -  espaço
    ['F', '¢', '6', 'N', '{', 'ü'],  # 1 -  A,á,à,â,ã
    ['%', 'L', '8', 'g'],       # 2 -  B
    ['Z', '=', '¨', '$'],       # 3 -  C,ç
    ['5', ':', '>', 'T'],       # 4 -  D
    ['M', '1', '+', 'a', 'r'],  # 5 -  E,é,ê
    ['!', 'Y', 'C', 'b'],       # 6 -  F
    ['&', 'H', 'x', '<'],       # 7 -  G
    ['D', 't', '@', '"'],       # 8 -  H
    ['9', 'p', '~', 'A'],       # 9 -  I,í,ì
    ['e', '3', 'O', '^'],       # 10 - J
    ['Ú', 'q', '7', ','],       # 11 - K
    ['%', 'J', '_', '0'],       # 12 - L
    ['/', '#', 'V', 'B'],       # 13 - M
    ['l', '}', 'i', 'ø'],       # 14 - N
    ['2', 'W', ';', 'h', 's'],  # 15 - O,ó,õ,ô
    ['ß', 'G', 'k', 'ç'],       # 16 - P
    ['c', ']', 'u', 'I'],       # 17 - Q
    ['E', 'f', 'j', 'm'],       # 18 - R
    ['è', 'U', 'X', 'ô', '£'],  # 19 - S
    ['K', 'o', 'í', '('],       # 20 - T
    ['R', 'y', 'Ç', 'ã', 'ï'],  # 21 - U,ú
    ['4', 'ê', 'õ', 'S'],       # 22 - V
    ['P', 'ì', 'ù', 'º'],       # 23 - W
    [')', 'à', 'î', 'd'],       # 24 - X
    ['ú', 'þ', 'ŋ', '¬'],       # 25 - Y
    ['v', 'ṕ', 'û', '|'],       # 26 - Z
]
print("\nPrograma para gerar senhas a partir de frases",
      "\nNão use uma frase muito grande!\n")

while True:
    pre_senha = input("Digite a frase que será a senha: ").lower()
    if len(pre_senha) > 40:
        print('O máximo de caracteres é 40, tente novamente.\n')
        continue

    else:
        break

print(f'Essa frase tem {len(pre_senha)} caracteres')

b = ''
temporario = ''
troca = 0
for i in pre_senha:
    if i in letras:
        if i == ' ':
            troca = 0
            b = novas_letras[troca][random.randint(0, len(novas_letras[troca][:]) - 1)]
            temporario += b

        elif i == 'a' or i == 'á' or i == 'à' or i == 'â' or i == 'ã':
            troca = 1
            b = novas_letras[troca][random.randint(0, len(novas_letras[troca][:]) - 1)]
            temporario += b

        elif i == 'b':
            troca = 2
            b = novas_letras[troca][random.randint(0, len(novas_letras[troca][:]) - 1)]
            temporario += b

        elif i == 'c' or i == 'ç':
            troca = 3
            b = novas_letras[troca][random.randint(0, len(novas_letras[troca][:]) - 1)]
            temporario += b

        elif i == 'd':
            troca = 4
            b = novas_letras[troca][random.randint(0, len(novas_letras[troca][:]) - 1)]
            temporario += b

        elif i == 'e' or i == 'é' or i == 'ê':
            troca = 5
            b = novas_letras[troca][random.randint(0, len(novas_letras[troca][:]) - 1)]
            temporario += b

        elif i == 'f':
            troca = 6
            b = novas_letras[troca][random.randint(0, len(novas_letras[troca][:]) - 1)]
            temporario += b

        elif i == 'g':
            troca = 7
            b = novas_letras[troca][random.randint(0, len(novas_letras[troca][:]) - 1)]
            temporario += b

        elif i == 'h':
            troca = 8
            b = novas_letras[troca][random.randint(0, len(novas_letras[troca][:]) - 1)]
            temporario += b

        elif i == 'i' or i == 'í' or i == 'ì':
            troca = 9
            b = novas_letras[troca][random.randint(0, len(novas_letras[troca][:]) - 1)]
            temporario += b

        elif i == 'j':
            troca = 10
            b = novas_letras[troca][random.randint(0, len(novas_letras[troca][:]) - 1)]
            temporario += b

        elif i == 'k':
            troca = 11
            b = novas_letras[troca][random.randint(0, len(novas_letras[troca][:]) - 1)]
            temporario += b

        elif i == 'l':
            troca = 12
            b = novas_letras[troca][random.randint(0, len(novas_letras[troca][:]) - 1)]
            temporario += b

        elif i == 'm':
            troca = 13
            b = novas_letras[troca][random.randint(0, len(novas_letras[troca][:]) - 1)]
            temporario += b

        elif i == 'n':
            troca = 14
            b = novas_letras[troca][random.randint(0, len(novas_letras[troca][:]) - 1)]
            temporario += b

        elif i == 'o':
            troca = 15
            b = novas_letras[troca][random.randint(0, len(novas_letras[troca][:]) - 1)]
            temporario += b

        elif i == 'p':
            troca = 16
            b = novas_letras[troca][random.randint(0, len(novas_letras[troca][:]) - 1)]
            temporario += b

        elif i == 'q':
            troca = 17
            b = novas_letras[troca][random.randint(0, len(novas_letras[troca][:]) - 1)]
            temporario += b

        elif i == 'r':
            troca = 18
            b = novas_letras[troca][random.randint(0, len(novas_letras[troca][:]) - 1)]
            temporario += b

        elif i == 's':
            troca = 19
            b = novas_letras[troca][random.randint(0, len(novas_letras[troca][:]) - 1)]
            temporario += b

        elif i == 't':
            troca = 20
            b = novas_letras[troca][random.randint(0, len(novas_letras[troca][:]) - 1)]
            temporario += b

        elif i == 'u':
            troca = 21
            b = novas_letras[troca][random.randint(0, len(novas_letras[troca][:]) - 1)]
            temporario += b

        elif i == 'v':
            troca = 22
            b = novas_letras[troca][random.randint(0, len(novas_letras[troca][:]) - 1)]
            temporario += b

        elif i == 'w':
            troca = 23
            b = novas_letras[troca][random.randint(0, len(novas_letras[troca][:]) - 1)]
            temporario += b

        elif i == 'x':
            troca = 24
            b = novas_letras[troca][random.randint(0, len(novas_letras[troca][:]) - 1)]
            temporario += b

        elif i == 'y':
            troca = 25
            b = novas_letras[troca][random.randint(0, len(novas_letras[troca][:]) - 1)]
            temporario += b

        elif i == 'z':
            troca = 26
            b = novas_letras[troca][random.randint(0, len(novas_letras[troca][:]) - 1)]
            temporario += b

        else:
            temporario += i

    else:
        temporario += 'æ'

print(f'{"-" * (14 + len(pre_senha))}\nSenha gerada: {temporario}\n{"-" * (14 + len(pre_senha))}')
