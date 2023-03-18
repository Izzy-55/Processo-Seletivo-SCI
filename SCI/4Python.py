#Criar um vetor de cinco posições, solicitar  cinco números e ao fim, imprimir o valor apresentado na posição três.
alcance = int(input("Quantos elementos você deseja que a lista tenha? "))
vetor = [] 
for i in range(alcance):  
    numero = list(map(float, input("Insira os elementos desejados, separados por espaço: ").split()))
    vetor.append(numero)
    if len(numero) >= 3:
        print("O valor na posição três é:", vetor[i][2])
        break
    else:
        print("A lista não tem pelo menos 3 elementos")
        break
        