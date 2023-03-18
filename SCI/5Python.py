
import sys


matriz = [["" for j in range(2)] for i in range(3)]


for i in range(3):
    
    nome = input("Informe o nome: ")
    matriz[i][0] = nome

    
    somaNota = 0
    for j in range(4):
        nota = float(input("Informe a {}ª nota: ".format(j+1)))
        somaNota += nota
    matriz[i][1] = str(somaNota/4)


menorNota = sys.float_info.max
maiorNota = sys.float_info.min
menorNotaS = ""
maiorNotaS = ""


for i in range(3):
    nota = float(matriz[i][1])
    if nota > maiorNota:
        maiorNotaS = matriz[i][0] + " tirou a maior nota, essa nota foi de " + matriz[i][1] + ""
        maiorNota = nota
    if nota < menorNota:
        menorNotaS = matriz[i][0] + " tirou a menor nota, essa nota foi de " + matriz[i][1] + ""
        menorNota = nota


for i in range(3):
    print(matriz[i][0], matriz[i][1])
print(menorNotaS)
print(maiorNotaS)
