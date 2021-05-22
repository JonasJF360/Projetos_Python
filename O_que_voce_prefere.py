# Define um estilo para o título.
def titulo(self):
    qt = 40
    ln = '=' * qt
    x = (qt - len(self)) / 2
    cent = round(x) * ' '
    print('\n%s\n%s%s\n%s' % (ln, cent, self, ln))

titulo('PEGANDO NO PESADO.')
# Pergunta 01
print('Se fosse para você trabalhar pesado\ndurante 30 dias, o que você preferia?\n')
print('01) Ganhar 1000.00 reais todos os dias\ndurante 30 dias. ou,\n02) Ganhar 1 centavo dobrando o valor\ntodos os dias por 30 dias?')
# Resposta
errou = 'sim'
while errou == 'sim':
    escolha = input('(1 ou 2) R: ')
    if escolha.isdigit() == True:
        escolha = int(escolha)
        if escolha == 1:
            break
        elif escolha == 2:
            break
        else:
            print('\nOPÇÃO INVÁLIDA.')
            errou = 'sim'
    else:
        print('\nOPÇÃO INVÁLIDA.')
        errou = 'sim'
# Exemplo
dias = 10
print('\nVeja um exemplo trabalhando %i dias' % dias)
print('ganhando 1 centavo Vs. 1000.00 reais.\n%s' % ('-' * 40))
pagar = 0.01
mil = 1000
vezes = 0
while dias > 0:
    vezes += 1
    ganho1 = pagar
    pagar = pagar * 2
    ganho2 = mil
    mil = ganho2
    mil += 1000
    dias -= 1
    print('Dia %i: R$ %1.2f Vs. R$ %1.2f' % (vezes, ganho1, ganho2))
# Pergunta 02
print('%s\nCom base no exemplo acima você ainda\ndeseja permanecer com sua escolha?' % ('-' * 40))
# Resposta
errou = 'sim'
while errou == 'sim':
    simnao = input('(S ou N) R: ')
    simnao = simnao.upper()
    if simnao.isdigit() == False:
        if simnao == 'S':
            break
        elif simnao == 'N':
            if escolha == 1:
                escolha = 2
                break
            else:
                escolha = 1
                break
        else:
            print ('\nOPÇÃO INVÁLIDA.')
            errou = 'sim'
    else:
        print ('\nOPÇÃO INVÁLIDA.')
        errou = 'sim'
# Valor para 1000 reais
if escolha == 1:
    dias = 30
    pagar = 1000 # Reais
    vezes = 0
    while dias > 0:
        vezes += 1
        ganho1 = pagar
        pagar = ganho1
        pagar += 1000
        dias -= 1
        print('Dia %i - Ganho: %1.f' % (vezes, ganho1))
    print('%s\nVocê ganhou R$ %1.2f\nSe tivesse escolhido a segunda opção\nteria ganho R$ %1.2f' % (('-' * 40), ganho1, 5368709.12))
# Valor para 01 centavo.
else:
    dias = 30
    pagar = 0.01 # 01 centavo
    vezes = 0
    while dias > 0:
        vezes += 1
        ganho2 = pagar
        pagar = pagar * 2
        dias -= 1
        print('Dia %i - Ganho: %1.2f' % (vezes, ganho2))
    print ('%s\nVocê ganhou R$ %1.2f\nSe tivesse escolhido a pimeira opção\nteria ganho R$ %1.2f' % (('-' * 40), ganho2, 30000.00))
print('=' * 40)
