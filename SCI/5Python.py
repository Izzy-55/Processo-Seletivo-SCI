#Crie uma matriz bidimensional.
# Deverá ser solicitado três nomes de alunos e quatro notas.
# Após solicitação dos nomes e das notas deverá ser impresso os nomes acompanhados da média geral de cada aluno,
# deverá ser impresso também o nome do aluno que obteve a maior média e o nome do aluno que obteve a menor média.


import numpy as np

# Criação da Matriz como numpy array
Matriz = np.zeros((3, 6), dtype=object)

for i in range(3):
    nome = input("Insira nome do aluno: ")
    Matriz[i, 0] = nome  #Colocando os nomes na Matriz
    
    notas_aluno = []
    for j in range(4):
        notas = float(input("Insira a {}° nota do aluno {}: ".format(j+1, nome)))
        notas_aluno.append(notas)
        Matriz[i, j+1] = notas  # Colocando as notas na Matriz
    
    media = np.mean(notas_aluno)
    Matriz[i, 5] = media  #Colocando as médias na Matriz
    
    #Impressão para fácil entendimento do usuário
    print("O aluno {} teve as seguintes notas: {}".format(nome, notas_aluno))
    print("A média do aluno {} é: {}\n".format(nome, media))
 
#Cálculo da maior e menor média, juntamento com colocando dita média na Matriz   
indice_menor_media = np.argmin(Matriz[:, 5])
menor_media = Matriz[indice_menor_media, 5]
aluno_menor_media = Matriz[indice_menor_media, 0]

indice_maior_media = np.argmax(Matriz[:, 5])
maior_media = Matriz[indice_maior_media, 5]
aluno_maior_media = Matriz[indice_maior_media, 0]


#Impressão do aluno com maior e menor média em modo de fácil entendimento ao usuário
print(" O aluno com menor média foi {}, essa média foi de {}".format(aluno_menor_media, menor_media))
print(" O aluno com maior média foi {}, essa média foi de {} \n ".format(aluno_maior_media, maior_media))

#Impressão da Matriz
print(Matriz)
        