import random
import re


def is_int(val):
    if isinstance(val, int):
        return True
    if re.search(r'^-?[0-9]+$', val):
        return True
    return False


# Programa:
print('\nADIVINHE O NÚMERO ALEATÓRIO!',
      '\nO número está entre "0" e "100"\n')
num_rand = random.randint(0,100)

cont = 5
while True:
    while True:
        resp_user = input("DIGITE UM NÚMERO: ")
    
        if is_int(resp_user) == True:
            resp_user = int(resp_user)
            if resp_user < 0 or resp_user > 100:
                print('\nVocê digitou um valor inválido!',
                      '\nO número tem que ser de "0" a "100"',
                      '\nTente novamente.\n')
                continue
            else:
                break
        
        else:
            print('\nVocê digitou um valor inválido!',
                  '\nTente novamente.\n')
            continue
        
    if resp_user != num_rand:
        cont -= 1
        if resp_user > num_rand:
            print("O seu numero é MAIOR, tente de novo.")
            print(f"Voce  tem {cont} tentativas\n")
        else:
            print("O seu numero é MENOR, tente de novo.")
            print(f"Voce  tem {cont} tentativas\n")

    if cont == 0:
        print ("Suas chances acabaram. :(")
        print(f'O número era: {num_rand}')
        break
        
    if resp_user == num_rand:
        print("PARABÉNS! Voce acertou! :D")
        break

