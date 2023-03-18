# Elabore um programa de computador que realize o cálculo de notas.
# Este programa deverá solicitar o nome do aluno e quatro notas.
# Todo este conjunto deverá estar contido em um laço que confirme se deseja encerrar o programa ou continuar solicitando outros nomes e notas.
# Ao final da solicitação do nome e das notas deverá ser impresso o nome do aluno e a sua média, se a nota for  menor que 6 imprimir Reprovado, 
# senão, se a nota for igual ou maior que 6, imprimir aprovado.

quebrar_loop = False

while not quebrar_loop :
    nome = input("Insira seu nome: ")
    for i in range(1):
        nota = list(map(float, input("Insira suas quatro  notas, separadas por espaço: ").split()))
        media = sum(nota)/ len(nota)
        print(f"O aluno {nome} tem como média: {media}")
        
        if media < 6:
            print('Sua média não foi o suficiente, você foi reprovado.')
        else:
            print("Sua média foi maior que 6, parabéns você foi aprovado!")
            
    quebrador_Loop_Encerramento = False
            
    while not quebrador_Loop_Encerramento:
        encerrar_prog = input("Deseja encerrar o programa? (sim/não) ")
        if encerrar_prog.lower() == "sim":
            quebrar_loop = True
            quebrador_Loop_Encerramento = True
            break
        elif encerrar_prog.lower() == "não":
             quebrador_Loop_Encerramento = True
        else:
            print("Opção inválida. Digite 'sim' ou 'não'. ")
            continue
        
