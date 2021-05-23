import random


"""
Esse projeto ainda está incompleto, mas quando tiver pronto
irá pegar uma frase qualquer e substituir cada letra que 
contida na variável 'letras' abaixo por outra que será gerada
alearóriamente de uma vatiável que contem 4 caractéres
(letras, números e simbolos).

Futuramente pretendo criar algo para "desencriprar" essa minha
"criptografia" gerada a partir da frase.
"""
letras = "abcdefghijklmnopqrstuvwxyzáàâãéêíìóõôúç"

print("Programa para gerar senhas a partir de frases",
      "\nNão use uma frase muito grande!\n")

pre_senha = input("Digite a frase que será a senha: ").lower()
print(f'Essa palavra tem {len(pre_senha)} caracteres')

temporario = ''
for i in pre_senha:
    troca = []
    if i in letras:
        if i == 'a' or i == 'á' or i == 'à' or i == 'â' or i == 'ã':
            troca = ['F', 'd', '6', 'N']
            b = troca[random.randint(0, len(troca) - 1)]
            temporario += b

        elif i == 'b':
            troca = ['%', 'L', '8', 'g']
            b = troca[random.randint(0, len(troca) - 1)]
            temporario += b

        elif i == 'c' or i == 'ç':
            troca = ['Z', '=', 'n', '$']
            b = troca[random.randint(0, len(troca) - 1)]
            temporario += b

        elif i == 'd':
            troca = ['5', ':', '>', 'T']
            b = troca[random.randint(0, len(troca) - 1)]
            temporario += b

        elif i == 'e' or i == 'é' or i == 'ê':
            troca = ['M', '1', '+', 'a']
            b = troca[random.randint(0, len(troca) - 1)]
            temporario += b

        elif i == 'f':
            troca = ['!', 'Y', 'Ç', 'b']
            b = troca[random.randint(0, len(troca) - 1)]
            temporario += b

        elif i == 'g':
            troca = ['&', 'H', 'x', '<']
            b = troca[random.randint(0, len(troca) - 1)]
            temporario += b

        elif i == 'h':
            troca = ['D', 't', '@', 'z']
            b = troca[random.randint(0, len(troca) - 1)]
            temporario += b

        elif i == 'i' or i == 'í' or i == 'ì':
            troca = ['9', 'p', '~', 'A']
            b = troca[random.randint(0, len(troca) - 1)]
            temporario += b

        else:
            temporario += i

    else:
        temporario += '*'

print(f'\nNova senha: {temporario} com {len(temporario)} caracteres')
