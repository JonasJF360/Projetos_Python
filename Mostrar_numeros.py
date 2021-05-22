#-*-coding:utf8;-*-
#qpy:console
import androidhelper
droid = androidhelper.Android()

# Define um estilo para o título.
def titulo(self):
    ln = '=' * 38
    x = (38 - len(self)) / 2
    cent = round(x) * ' '
    print('\n%s\n%s%s\n%s\n' % (ln,cent,self,ln))

valor = droid.dialogGetInput('MOSTRAR SÓ OS NÚMEROS', 'Cole ou digite o valor aqui:').result

lista = []
x = len(valor)
z = 0
while z < x:
    teste = valor[z]
    if teste.isdigit() == True:
        lista += [teste]
        z += 1
    else:
        z += 1

unir = ''
for valor in lista:
    unir += valor
titulo('RESULTADO')
print(unir)